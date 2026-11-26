# Changelog

## asisten-tesis 0.5.0 (2026-11-26)

- `chapter4-analysis` no longer assumes a questionnaire or interview study. It follows the method in Chapter 3 and the campus chapter map: primary data (interviews, FGD, observation, questionnaires, expert judgment) and secondary data (company records, financial statements, industry reports, statistics); business issue analysis (PESTLE, Five Forces, VRIO, SWOT/TOWS), root cause analysis, solution selection (AHP with consistency ratio, Kepner-Tregoe), financial feasibility (NPV, IRR, payback, sensitivity), and implementation plans. Method notes moved to `skills/chapter4-analysis/references/methods.md`.
- Output from the author's own tools (SPSS, SmartPLS, NVivo, Excel models) is treated as the record and interpreted, not recomputed.
- `thesis-profile.md` gains thesis type, chapter map, and data sources (with provenance and confidentiality).

## asisten-tesis 0.4.0 (2026-11-26)

First public release.

- Six skills: `chapter4-analysis`, `find-sources`, `supervisor-feedback`, `lugas` (vendored), `ai-slop-check`, `defense-deck`.
- Deliverables default to English; Indonesian through `thesis-profile.md`.
- `defense-deck`: bundled builder `build_pptx.py` with the "academic" theme, checker `check_pptx.py`, previews through `deckcraft-cli render`. Built decks no longer carry python-pptx template metadata.
- Word and PowerPoint tools are picked from what is available (WordCraft/DeckCraft MCP, Claude's built-in skills, Google connectors, python-docx/python-pptx), with an optional Google Drive mirror.
