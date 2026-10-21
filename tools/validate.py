#!/usr/bin/env python3
"""Validate identifiers, scope roles, local references, and generated-file freshness."""
from pathlib import Path
from urllib.parse import urlparse,unquote
from datetime import date
from collections import Counter
import json,re,hashlib,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from build import CATEGORIES

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    records=json.loads((ROOT/'data/papers.json').read_text());media=json.loads((ROOT/'data/media.json').read_text());report=json.loads((ROOT/'data/verification.json').read_text())
    ids=[r['id'] for r in records];assert len(ids)==len(set(ids)),'Duplicate reference IDs'
    arxiv=[r['arxiv_id'] for r in records if r.get('arxiv_id')];assert len(arxiv)==len(set(arxiv)),'Duplicate arXiv identities'
    assert len(records)==report['reference_count'],'Incorrect reference count'
    assert len(arxiv)==report['arxiv_identity_checks'],'Incorrect arXiv verification count'
    for r in records:
        assert r['category'] in CATEGORIES,(r['id'],'unknown category')
        assert r['title'].strip() and r['summary'].strip() and r['scope_note'].strip(),r['id']
        assert r['source_type'] in {'paper','technical-report','implementation','official-report'},r['id']
        assert r['verification']['identity']=='primary-source-checked',r['id']
        checked=date.fromisoformat(r['verification']['checked_on'])
        for field in ['first_published','updated']:
            if r.get(field):assert date.fromisoformat(r[field])<=checked,(r['id'],field,'future date')
        if r.get('arxiv_id'):
            assert re.fullmatch(r'\d{4}\.\d{4,5}',r['arxiv_id']),r['id']
            assert r['arxiv_id'] in r['links']['paper'],(r['id'],'paper URL identity mismatch')
        for u in [r['verification']['source'],*r['links'].values()]:
            assert u.startswith('https://') and urlparse(u).netloc,(r['id'],'non-HTTPS/malformed URL',u)
            assert not any(x in u for x in ['localhost','127.0.0.1','/Users/','token=']),u
        if r.get('evaluation_reference'):assert r['category']=='evaluation',r['id']
    for item in media['showcase']:
        assert item['paper_id'] in ids,item['id']
        for key in ['video_url','thumbnail_url','source_url']:assert item[key].startswith('https://'),item['id']
    assert len(media['showcase'])>=4,'Missing representative demos'
    generated=[ROOT/'README.md',ROOT/'references.bib',ROOT/'data/papers.csv',ROOT/'docs/READING_NOTES.zh-CN.md',*(ROOT/folder/'README.md' for _,folder,_ in CATEGORIES.values()),*sorted((ROOT/'assets/readme').glob('*.svg'))]
    before={str(p):digest(p) for p in generated}
    subprocess.run([sys.executable,str(ROOT/'tools/build.py')],check=True)
    changed=[p for p,h in before.items() if digest(Path(p))!=h]
    assert not changed,'Generated files were stale: '+str(changed)
    errors=[]
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:continue
        text=path.read_text()
        targets=re.findall(r'\]\(([^\s)]+)(?:\s+[^)]*)?\)',text)+re.findall(r'(?:href|src)="([^"]+)"',text)
        for target in targets:
            if target.startswith(('https://','http://','mailto:','#','data:')):continue
            local=unquote(target.split('#')[0].split('?')[0])
            if local and not (path.parent/local).exists():errors.append((str(path.relative_to(ROOT)),target))
        for bad in [r'/Users/[^\s]+',r'gh[pousr]_[A-Za-z0-9]{20,}',r'Bearer\s+[A-Za-z0-9._-]{20,}']:
            assert not re.search(bad,text),'Local path/credential pattern in '+str(path)
    assert not errors,'Missing local links: '+str(errors)
    print(json.dumps(dict(references=len(records),arxiv_identities=len(arxiv),categories=dict(Counter(r['category'] for r in records)),showcase_videos=len(media['showcase']),checks='Identifiers, dates, category roles, source URLs, media provenance, local links, and generated-file freshness passed.'),indent=2))

if __name__=='__main__':main()
