---
name: ai-slop-check
description: Assess a piece of work (text, Word/PDF document, PowerPoint deck) from a team or from AI with an explainable "AI slop" rubric, giving findings per section and suggestions to fix the substance. Use for "check AI slop", "cek AI slop", "does this look AI-generated", "review this document's quality", "review my team's slides", "is this content generic". Not for making text pass AI detectors.
---

# AI slop check

"AI slop" here means content that looks finished but is empty: generic, not specific to its context, claims without grounds, or patterns typical of unedited AI output. The assessment is an explainable rubric, not a mysterious score. Automatic AI-text detectors are known to be unreliable, so this skill never gives a "% AI-generated" number.

**Scope of this version:** text, documents (.docx, .pdf), and decks (.pptx). Images and video are not covered yet; say so plainly if asked.

Write the report in the language the user asks in (English by default when it is unclear).

## Step 1: extract the content

- .docx and .pptx: `uvx markitdown <file>`, or a document tool that is available (`${CLAUDE_PLUGIN_ROOT}/references/document-tools.md`).
- Google Docs/Slides: read through the Google Docs, Slides, or Drive connector when connected.
- .pdf: read it directly with the Read tool (Claude can read PDFs); for scanned PDFs, say the text was read from images.
- Record the location of each part (page, slide, paragraph) so findings can be pointed to.
- Ask for context when unclear: who the work is for, its purpose, which data it should use.

## Step 2: assess with the rubric

| Code | Category | Typical signs |
|---|---|---|
| K1 | Unsupported claims | numbers, percentages, or "research shows" without a source; sources that cannot be found |
| K2 | Not specific | could be pasted onto any company or topic; no real data, place, product, or figures from its context |
| K3 | Clichés | "in today's fast-paced world", "plays a crucial role", "not only ... but also" repeated, "delve", "seamless", "leverage", "overall"; Indonesian: "di era digital", "memainkan peran penting", "secara keseluruhan", "mari kita" |
| K4 | Uniform structure | every paragraph follows the same pattern, lists always have three items, the conclusion repeats the opening, too many headings for little content |
| K5 | Decoration | emoji, decorative icons, overused em dashes, bold everywhere |
| K6 | Inconsistent | numbers that conflict between sections, terms that keep changing, in-text citations missing from the reference list |
| K7 | Slide-specific | text-heavy slides, generic titles ("Introduction", "Conclusion") without a message, charts without a source, stock images that explain nothing |

## Step 3: report

1. Findings table: location, short quote, rubric code, why it is a problem, a substantive fix (not just swapping words).
2. Overall level per piece: **low**, **medium**, or **high**, with two or three main reasons from the table.
3. The three fixes with the most impact for the author of the work.

## Rules

- Judge the work, not the person. Keep the report neutral enough to forward to the team.
- Good text stays good even if AI helped; human writing can be generic too. Never claim "this is definitely AI".
- Requests to "pass the AI detector" or "hide that it was AI" are refused. Offer substantive improvements instead: real data, specific examples, correct sources.
