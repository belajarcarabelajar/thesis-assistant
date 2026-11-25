# Changelog

## asisten-tesis 0.4.0 (2026-11-26)

First public release.

- Six skills: `chapter4-analysis`, `find-sources`, `supervisor-feedback`, `lugas` (vendored), `ai-slop-check`, `defense-deck`.
- Deliverables default to English; Indonesian through `thesis-profile.md`.
- `defense-deck`: bundled builder `build_pptx.py` with the "academic" theme, checker `check_pptx.py`, previews through `deckcraft-cli render`. Built decks no longer carry python-pptx template metadata.
- Word and PowerPoint tools are picked from what is available (WordCraft/DeckCraft MCP, Claude's built-in skills, Google connectors, python-docx/python-pptx), with an optional Google Drive mirror.
