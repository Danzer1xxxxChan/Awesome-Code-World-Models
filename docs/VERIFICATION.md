# Verification record

[← Main collection](../README.md) · [Machine-readable record](../data/verification.json)

**Checked on 2026-10-22.** This initial edition contains **154 unique references**: 147 papers, 3 technical reports, 2 implementations, and 2 official reports. Eight references are surveys/perspectives and are kept separate from original-method categories.

## What was checked again

1. **Identity:** current exact title, canonical paper identifier, and primary-source correspondence. All **145 arXiv identities** were checked against the official paper pages. The other nine records were checked against publisher, author, or official project pages.
2. **Dates:** first posting and updated dates were extracted from official citation metadata when present. Unknown release dates are left unspecified. A first arXiv posting date is not a conference date or a code-release date.
3. **Scope and role:** records were reviewed against the executable-world workflow. Complete systems, components, evaluation resources, and surveys are distinguished. Pose/trajectory evaluation references are not classified as complete world models.
4. **Supporting links:** **124 additional resource and media URLs** received HTTP-header checks. The primary paper checks are separate from these supporting-link checks. A successful response is evidence of reachability, not that an entire system is available or reproducible.
5. **Technical evidence:** existing targeted reading notes were retained with their reading-depth labels; selected current official READMEs and project pages were inspected again. This is not a claim that all papers were newly read in full or independently reproduced.

arXiv's metadata API rate-limited the initial request sequence. Verification therefore used the official article pages and their citation metadata; the catalog does not claim a successful API sweep.

## Material corrections and updates

| Item | What changed | Primary evidence |
|---|---|---|
| SolarRenderer | Added the newly linked canonical paper, arXiv:2610.28630; its first posting is 2026-10-20. | [Paper](https://arxiv.org/abs/2610.28630), [official repository](https://github.com/Enderfga/SolarRenderer) |
| Generative Rendering | Added the canonical arXiv identity 2312.01409 to the existing project record. | [Paper](https://arxiv.org/abs/2312.01409) |
| AgentGarten | Used the current official project address and checked the renderer's current backbone/codec description. | [Project](https://mirros-lab.github.io/agent-garten), [README](https://github.com/MirroS-Lab/AgentGarten) |
| Matrix-Game 4.0 | Rechecked the current implementation and hardware-specific instructions; the catalog does not turn reported throughput into a universal real-time claim. | [Implementation](https://github.com/SkyworkAI/Matrix-Game/tree/main/Matrix-Game-4) |
| PROWBench | Used the current formal paper title, without presenting the old ROWBench label as a separate work. | [Paper](https://arxiv.org/abs/2610.02205) |
| EgoControl / 3DTrajMaster | Included their camera/body and trajectory evaluation protocols as evaluation references, rather than treating control vectors alone as executable worlds. | [EgoControl](https://arxiv.org/abs/2511.18173), [3DTrajMaster](https://arxiv.org/abs/2412.07759) |
| RoleWorld project link | Omitted an author-linked project address that returned HTTP 404; retained the verified paper. | [Paper](https://arxiv.org/abs/2610.13172) |
| Streaming CWM video attachment | Omitted an unavailable GitHub attachment instead of publishing a broken video embed; retained the implementation. | [Repository](https://github.com/TingtingLiao/streaming-code-world-model) |

## How to interpret the records

Each item in [`papers.json`](../data/papers.json) records the checked source, date, scope note, and technical-reading provenance. Source-response hashes preserve the identity of the pages used for this edition. Raw full papers and third-party abstracts are not redistributed in this repository.

The top-level count is a count of **references**, not complete systems or newly reproduced experiments. Published results remain author-reported unless explicitly stated otherwise. Code, models, datasets, and complete environment backends can have different release states.

## Maintenance checks

`python3 tools/validate.py` checks unique identifiers, date consistency, category roles, local links, media provenance, and the freshness of generated indexes. HTTP checks are a dated snapshot; later link failures should be reported as corrections rather than silently interpreted as invalid research.
