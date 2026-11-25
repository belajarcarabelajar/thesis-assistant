---
name: supervisor-feedback
description: Turn feedback from the thesis supervisor or examiners (notes, WhatsApp chats, comments in a Word file, transcripts of supervision recordings) into a trackable revision list, then help carry out and report the revisions. Use for "supervisor feedback", "masukan dosen", "revisions from my advisor", "supervision notes", "defense results", "what do I need to revise", "revision report".
---

# Supervisor feedback → revision list

## Step 0: read the thesis profile

Look for `thesis-profile.md` in the thesis working folder (the folder Claude runs in). If it is missing, copy the template `${CLAUDE_PLUGIN_ROOT}/templates/thesis-profile.md` into the working folder and ask the author to fill in the blanks. Never guess the title, method, or research questions from memory or from file names.

**Language:** write every deliverable (drafts, tables, slides, scripts, lists) in the thesis language from the profile, **English by default**. Talk to the author in the language they use in chat.

## Flow

1. **Collect the feedback as given.** Save the original text in `revisions/feedback-<date>.md` (quote verbatim, in its original language, and name the source: chat, Word comment, recording). Read Word comments with the tool available (`${CLAUDE_PLUGIN_ROOT}/references/document-tools.md`), for example WordCraft `inspect_document`, or Google Docs comments when the manuscript lives there. Voice recordings: ask for a transcript first; never guess the content.
2. **Split into items.** One piece of feedback = one row in `revisions/revision-list.md`:

   | No | Chapter/page | Feedback (verbatim) | Interpretation | Action | Status | Evidence after revision |
   |---|---|---|---|---|---|---|

   Status: `open`, `in progress`, `done`, `ask supervisor`.
3. **Flag ambiguity.** Feedback that can be read more than one way gets status `ask supervisor` plus one short question ready to send (in the language the supervisor uses).
4. **Work item by item** once the author agrees with the interpretation. Never overwrite the original manuscript: revise in a new copy and record the resulting page or section in the evidence column.
5. **Report for the next supervision.** Summarize: items done (with pages), items still open and why, questions for the supervisor. Polite, short, from the author's point of view.

## Rules

- Never soften or drop uncomfortable feedback; every item goes on the list.
- Feedback that conflicts between supervisors or examiners is flagged and taken to the author, not decided by you.
- Changes to substance (data, method, conclusions) are always confirmed by the author first; language and formatting changes can be made directly in the copy.
