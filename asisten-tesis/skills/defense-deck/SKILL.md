---
name: defense-deck
description: Prepare thesis defense slides that stay editable in PowerPoint, a per-slide practice script, and mock Q&A with examiners, based on the author's thesis manuscript. Use for "defense slides", "PPT sidang", "thesis presentation", "viva", "presentation script", "defense practice", "likely examiner questions". Slides must not look AI-made, which means little text, no emoji, and numbers identical to the manuscript.
---

# Defense deck, practice script, and mock Q&A

## Step 0: read the thesis profile

Look for `thesis-profile.md` in the thesis working folder (the folder Claude runs in). If it is missing, copy the template `${CLAUDE_PLUGIN_ROOT}/templates/thesis-profile.md` into the working folder and ask the author to fill in the blanks. Never guess the title, method, or research questions from memory or from file names.

**Language:** write every deliverable (drafts, tables, slides, scripts, lists) in the thesis language from the profile, **English by default**. Talk to the author in the language they use in chat.

Needed: the latest manuscript (Chapters 1-5), the presentation length, and the campus or supervisor PowerPoint template if there is one.

## Step 1: storyline first, slides later

Draft an outline of 10-15 slides and get the author's approval:
background and problem → research questions and objectives → brief theoretical framework → method → findings per research question → discussion and managerial implications → conclusions, recommendations, limitations.

Each slide title is a message sentence, for example "Spare-part price drives purchase decisions most", not "Results".

## Step 2: build an editable .pptx

- Choose the slide tool and any online mirror per `${CLAUDE_PLUGIN_ROOT}/references/document-tools.md`: DeckCraft MCP when available, Claude's built-in PowerPoint skill, or Google Slides when the author works there; mirror to Google Drive when asked.
- Without DeckCraft or a built-in tool, use the builder bundled with this plugin; **do not write a new builder**:
  1. Write the slide content to `defense/slides.json` (format: `${CLAUDE_SKILL_DIR}/references/slides-format.md`).
  2. `uv run --with python-pptx python ${CLAUDE_SKILL_DIR}/scripts/build_pptx.py defense/slides.json defense/defense-deck.pptx --script defense/presentation-script.md [--template <campus template>.pptx]`
  3. `uv run --with python-pptx python ${CLAUDE_SKILL_DIR}/scripts/check_pptx.py defense/defense-deck.pptx` must exit 0.
  Later revisions only change `slides.json` and rerun. Do not use `pip install`.
- Without a campus template the builder applies the restrained "academic" theme (dark-blue gradient on the title and closing slides, an almost-white gradient behind content, navy and teal accents, slide numbers). Use `"theme": "plain"` for no styling. With a campus template, the template's own design is used.
- Use the campus or supervisor template when there is one (its masters and layouts, not pasted as images). Text goes in real text boxes, tables as tables, charts as PowerPoint charts. Never paste text or charts as images.
- Numbers on slides come from the manuscript or from `analysis/` output (skill `chapter4-analysis`), checked one by one.
- Save as a new file; never overwrite the original campus file.

## Step 3: look rules that avoid an "AI" feel

- About 30 words per slide at most; the rest goes to the speaker notes.
- No emoji, decorative icons, rainbow gradients, or stock images that explain nothing. A subtle two-tone background gradient from the theme is fine.
- No decorative accent lines (lines under titles, side stripes on boxes, gradient dividers). Shapes only when they carry content, such as boxes and arrows in the research model diagram.
- One idea per slide. Charts state their data source. Bar and column axes start at zero.
- Run the `ai-slop-check` skill on the final file before handing it over.

## Step 4: practice script

- Each slide's speaker notes (`notes` in `slides.json`) hold a 45-90 second script in the author's own spoken style (ask how they speak; avoid stiff prose).
- `--script` copies all notes to `defense/presentation-script.md` with an estimated total duration. Adjust the slide count if it runs over.

## Step 5: mock Q&A

1. Draft 15-20 likely examiner questions from the manuscript: why this topic, method and sample, validity and reliability, generalization, novelty or contribution, limitations, managerial implications.
2. For each: answer points from the manuscript (chapter and page), plus traps to avoid.
3. Simulation: ask one question at a time, wait for the author's answer, give brief feedback (accurate? too long? contradicts the manuscript?).

## Final check

- Look at the rendered slides before handing over (required; the structure check does not catch titles colliding with content or misleading chart axes):
  1. DeckCraft: `deckcraft-cli render defense/defense-deck.pptx --all --scale 1 defense/preview/`, then open each `slide-NN.png` with the Read tool.
  2. Without DeckCraft: render with another available tool (LibreOffice, or a Google Slides mirror per `${CLAUDE_PLUGIN_ROOT}/references/document-tools.md` if the author agrees to upload the file).
  3. Check: clipped or colliding text, titles larger than body text, chart axes from zero, numbers matching the manuscript. Fix `slides.json`, rebuild, render again.
  4. If nothing can render, say so plainly and ask the author to open it in PowerPoint.
- DeckCraft renders are previews; PowerPoint can look slightly different (for example, pie labels with category names may only show in PowerPoint). DeckCraft is still alpha: open the final file in Microsoft PowerPoint before the defense and make last fixes there.
