# asisten-tesis (v0.4.0)

A Claude Code plugin for writing a master's thesis. Every skill reads `thesis-profile.md` in the thesis working folder (template: `templates/thesis-profile.md`). Deliverables are in **English by default**; set "Thesis language" in the profile to Indonesian to switch.

| Skill | What it does |
|---|---|
| `chapter4-analysis` | Data (questionnaires, interviews) → tables and charts from a script → Chapter 4 draft per research question, checked by the author |
| `find-sources` | Find and verify journals (TinyFish, OpenAlex, Crossref), APA 7 reference list |
| `supervisor-feedback` | Supervisor feedback → tracked revision list → report for the next supervision |
| `lugas` | Edit, paraphrase, and translate academic text between English and Indonesian without changing numbers, citations, or claim strength |
| `ai-slop-check` | "AI slop" rubric for text, documents, and decks (images and video not yet) |
| `defense-deck` | Editable defense slides (builder `scripts/build_pptx.py` from `slides.json`, "academic" theme, checker `scripts/check_pptx.py`, preview via `deckcraft-cli render`), per-slide practice script, mock examiner Q&A |

## Prerequisites (Windows)

| Tool | For | How to install (official source) |
|---|---|---|
| Git for Windows | Claude Code uses its Bash and `curl` | https://git-scm.com/download/win |
| uv | Runs Python scripts (data analysis, slides, markitdown) without installing Python by hand | `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` (https://docs.astral.sh/uv/) |
| TinyFish MCP | Source search (`find-sources`) | https://docs.tinyfish.ai/mcp-integration |
| DeckCraft (optional, recommended) | Slide previews as images (`deckcraft-cli render`) and a slide MCP | https://github.com/storytold/deckcraft/releases (Windows: `.msi` or `-portable.zip`) |

## Install

From the public repo [`belajarcarabelajar/thesis-assistant`](https://github.com/belajarcarabelajar/thesis-assistant) (no GitHub account needed):

```
/plugin marketplace add belajarcarabelajar/thesis-assistant
/plugin install asisten-tesis@belajarcarabelajar-tesis
```

Update later with `/plugin marketplace update belajarcarabelajar-tesis`. From a local copy: `/plugin marketplace add <path to the thesis-assistant folder>`.

Try without installing: `claude --plugin-dir <path to the asisten-tesis folder>`.

Word/PowerPoint tools are chosen dynamically from what is available (`references/document-tools.md`): WordCraft/DeckCraft MCP (github.com/storytold, still alpha), Claude's built-in Word/PowerPoint skills, the claude.ai Google Docs/Slides/Drive connectors, or python-docx/python-pptx scripts through uv. An online mirror to Google Drive is made when asked. Final files are always checked in Microsoft Word/PowerPoint.

## Attribution

This plugin is licensed under the Apache License 2.0 (`LICENSE`, `NOTICE`). `skills/lugas/` is copied unchanged from [rezaprama/Lugas](https://github.com/rezaprama/Lugas) (commit `d6a7b3c396c3acef18234b21de891b088bc80b1a`), together with the upstream root `LICENSE`, `NOTICE`, `THIRD_PARTY_NOTICES.md`, and `LICENSES/`: Skill code Apache-2.0, `assets/patterns.json` CC BY 4.0. The other skills were written for this plugin, drawing on patterns from public thesis and academic-writing skill repositories on GitHub (no code copied).
