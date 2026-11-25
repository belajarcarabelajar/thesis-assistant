# Choosing tools for Word and PowerPoint files

Used by the `chapter4-analysis`, `supervisor-feedback`, `defense-deck`, and `ai-slop-check` skills. Pick tools by what is actually available in this session; never assume.

## Step 1: check what is available

Look at the MCP tools in this session (names such as `wordcraft`, `deckcraft`, `Google_Slides`, `Google_Docs`, `Google_Drive`, Microsoft 365, OneDrive), then read the "Document tools" line in `thesis-profile.md`. If a connector exists but asks for sign-in, tell the author and offer another tool; do not stop.

## Step 2: choose the main tool

The order below is the default. If the thesis profile or the author names another choice, follow it.

| Need | Options, use the first one available |
|---|---|
| Word manuscript (.docx) | 1. WordCraft MCP (`wordcraft-cli mcp --automation-read-root <folder> --automation-write-root <folder>`) 2. Claude's built-in Word skill (docx) or a Microsoft 365 connector when connected 3. A script with `uv run --with python-docx` |
| Slides (.pptx) | 1. DeckCraft MCP (`deckcraft-cli mcp --automation-read-root <folder> --automation-write-root <folder>`) 2. Claude's built-in PowerPoint skill (pptx) 3. Google Slides connector, when the author wants to work in Google Slides 4. The bundled builder of the `defense-deck` skill (python-pptx through uv) |
| Documents worked on together online | Google Docs or Google Slides connector |

State in the report which tool was used and why.

## Step 3: mirror (online copy), when asked

Make a mirror only when the author asks or the thesis profile says "mirror: yes".

1. The main file stays local (.docx/.pptx), because that is what the supervisor and campus open in Word/PowerPoint.
2. Upload a copy to Google Drive with the Google Drive connector (`create_file` with the file content; Drive converts it to Google Docs/Slides unless `disableConversionToGoogleType` is `true`). Keep it in a thesis folder and give the link.
3. Converting to Google Docs/Slides can shift formatting. The mirror is for reading, sharing, or comments, not the final manuscript.
4. If the author or supervisor edits the mirror, those edits do not flow back to the local file automatically. Download again, compare, and move the changes into the main file with the author's approval.
5. Never share the mirror with anyone without the author's permission.

The reverse also works: when the author works in Google Slides/Docs, the local .pptx/.docx is the copy (download with File > Download in Google, or the Google Drive connector), and that file is checked in PowerPoint/Word before it goes to campus.
