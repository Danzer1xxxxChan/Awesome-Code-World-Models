# Contributing

Corrections and additions are welcome. Start with an original paper, an author-maintained project page, or an official repository. Community indexes help discovery but are not substitutes for primary evidence.

1. Check [the scope](docs/SCOPE.md). State whether the contribution concerns executable-world construction, dynamics, visual realization, or evaluation.
2. Add or edit one record in `data/papers.json`. Preserve existing IDs. Use a new descriptive ID for a new work.
3. Include the exact current title, canonical identifier, primary source, date where reported, category, a short original summary, and a scope note. Separate a paper from an implementation or architecture report.
4. Record what you actually checked and when. Do not describe a metadata check as full technical review or reproduction. Do not infer that every checkpoint or component is released from the presence of a repository.
5. For models, hardware, latency, and throughput, cite the relevant paper section or official implementation/version. Distinguish content FPS, model throughput, and end-to-end interactive latency.
6. For media, use an author-provided demo with attribution and a reachable official source. Add its provenance to `data/media.json`; preserve third-party ownership and licensing.

Regenerate and validate with Python 3.10 or newer; no extra packages are required:

```bash
python3 tools/build.py
python3 tools/validate.py
```

Please include the reason for a category or scope change in your pull request. A general evaluation protocol may be relevant even when the method that introduced it is outside the executable-world method scope.
