"""Generate original SVG artwork used by the README. No third-party artwork is copied."""
from pathlib import Path
from html import escape

ROOT=Path(__file__).resolve().parents[1]
ASSETS=ROOT/'assets/readme'

PALETTE={'systems':'#68dec2','construction':'#9abbe8','dynamics':'#d6b27d','rendering':'#b5abed','evaluation':'#98c690','surveys':'#dca3ae'}

def banner():
    code=''.join(f'<rect x="{772+(i%3)*11}" y="{83+i*13}" width="{[104,76,122,89,113,65,98,120][i]}" height="4" rx="2" fill="{["#78cbb1","#93a6c5","#59738d"][i%3]}" opacity=".85"/>' for i in range(8))
    tiles=[]
    for row in range(5):
        for col in range(5):
            x=849+col*37-row*22;y=260+row*15+col*8
            tiles.append(f'<path d="M{x} {y}l37 8-22 15-37-8z" fill="{["#234539","#294c40","#1d3b33"][(row+col)%3]}" stroke="#4b846e" stroke-width=".7"/>')
    blocks='''<path d="M883 239l42 9 0-57-42-9z" fill="#507ca1"/><path d="M925 248l25-17 0-57-25 17z" fill="#35536f"/><path d="M883 182l42 9 25-17-42-9z" fill="#8ca9c2"/><path d="M980 273l32 7 0-34-32-7z" fill="#6b9a85"/><path d="M1012 280l22-15 0-34-22 15z" fill="#385c4b"/><path d="M980 239l32 7 22-15-32-7z" fill="#a0c0a1"/><circle cx="955" cy="258" r="13" fill="#e0ba7b"/><path d="M950 271v22m10-22v22m-10-17-9 8m19-8 8 8" stroke="#e0ba7b" stroke-width="5" stroke-linecap="round"/>'''
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="414" viewBox="0 0 1280 414" role="img" aria-labelledby="title desc"><title id="title">Awesome Code World Models</title><desc id="desc">A research collection connecting executable world programs, scene execution, generative rendering, and evaluation.</desc><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#14283a"/><stop offset="1" stop-color="#101b27"/></linearGradient><linearGradient id="light" x2="0" y2="1"><stop stop-color="#6ed6b6" stop-opacity=".1"/><stop offset="1" stop-color="#6ed6b6" stop-opacity="0"/></linearGradient></defs><rect width="1280" height="414" rx="22" fill="url(#bg)"/><path d="M682 0h598v414H682z" fill="url(#light)"/><path d="M708 47v320" stroke="#385265"/><g font-family="Arial,Helvetica,sans-serif"><text x="56" y="57" fill="#8ec7b5" font-size="12" font-weight="700" letter-spacing="3">A LIVING RESEARCH COLLECTION</text><text x="52" y="122" fill="#9db5c5" font-size="29" font-weight="600" letter-spacing="6">AWESOME</text><text x="51" y="184" fill="#f3f4ed" font-size="50" font-weight="700" letter-spacing="-1.8">CODE WORLD</text><text x="51" y="245" fill="#f3f4ed" font-size="50" font-weight="700" letter-spacing="-1.8">MODELS</text><text x="55" y="284" fill="#afc1c9" font-size="17">Executable worlds. Generative observations.</text><g font-size="11" font-weight="600" letter-spacing="1"><rect x="55" y="326" width="92" height="31" rx="5" fill="#214d43"/><text x="73" y="346" fill="#8ce6c9">PROGRAM</text><text x="159" y="346" fill="#617f8d">→</text><rect x="181" y="326" width="91" height="31" rx="5" fill="#283d50"/><text x="198" y="346" fill="#b5c9e6">EXECUTE</text><text x="285" y="346" fill="#617f8d">→</text><rect x="307" y="326" width="90" height="31" rx="5" fill="#36334f"/><text x="326" y="346" fill="#cbc1fa">RENDER</text><text x="410" y="346" fill="#617f8d">→</text><rect x="433" y="326" width="104" height="31" rx="5" fill="#3b4032"/><text x="449" y="346" fill="#c7d5a5">EVALUATE</text></g><rect x="750" y="56" width="188" height="149" rx="9" fill="#0c1924" stroke="#3f5d6c"/>{code}<text x="767" y="73" fill="#8da9a7" font-size="9" letter-spacing="1.5">EXECUTABLE WORLD</text>{''.join(tiles)}{blocks}<path d="M1048 128h139v190h-139z" fill="#132535" stroke="#58738a"/><path d="M1061 282l27-56 28 13 28-68 31 111z" fill="#314f46"/><path d="M1061 282l39-38 26 17 21-36 28 57z" fill="#577d58"/><circle cx="1151" cy="163" r="16" fill="#d7bd83"/><path d="M1116 318l9-36 8-28 9-31" fill="none" stroke="#c9b58f" stroke-width="11"/><text x="1050" y="343" fill="#91b4c2" font-size="10" letter-spacing="1.2">GENERATED OBSERVATION</text><path d="M962 118h49m-7-5 7 5-7 5" stroke="#73c9ad" stroke-width="2" fill="none"/><path d="M1021 283h18m-6-5 6 5-6 5" stroke="#93acc9" stroke-width="2" fill="none"/></g></svg>'''
    (ASSETS/'banner.svg').write_text(svg)

def card(slug,title,subtitle,count,number):
    color=PALETTE[slug]
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="350" height="112" viewBox="0 0 350 112" role="img" aria-labelledby="t"><title id="t">{escape(title)} — {count} entries</title><rect x="1" y="1" width="348" height="110" rx="9" fill="#f6f8f4" stroke="#d8e1d7"/><rect x="1" y="1" width="6" height="110" rx="3" fill="{color}"/><g font-family="Arial,Helvetica,sans-serif"><text x="24" y="29" fill="#64796f" font-size="11" letter-spacing="1.4">{number:02} / {count} ENTRIES</text><text x="23" y="58" fill="#243f36" font-size="20" font-weight="700">{escape(title)}</text><text x="24" y="83" fill="#65766c" font-size="11">{escape(subtitle)}</text><text x="319" y="58" fill="#708d7c" font-size="19">↗</text></g></svg>'''
    (ASSETS/(slug+'.svg')).write_text(svg)

def main(counts):
    ASSETS.mkdir(parents=True,exist_ok=True);banner()
    labels=[('systems','World Systems','Code + engine + generated observations'),('construction','World Construction','Create, reconstruct, and edit worlds'),('dynamics','Programmatic Dynamics','Executable rules, mechanisms, and planning'),('rendering','Generative Rendering','Scene execution to controllable visuals'),('evaluation','Data & Evaluation','General and world-specific evidence'),('surveys','Surveys & Perspectives','Definitions, context, and synthesis')]
    for i,(slug,title,sub) in enumerate(labels,1):card(slug,title,sub,counts.get(slug,0),i)

if __name__=='__main__':
    import json
    from collections import Counter
    data=json.loads((ROOT/'data/papers.json').read_text())
    main(Counter(r['category'] for r in data))
