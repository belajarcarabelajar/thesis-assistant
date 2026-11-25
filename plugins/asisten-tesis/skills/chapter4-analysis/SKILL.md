---
name: chapter4-analysis
description: Help draft Chapter 4 (Results and Discussion) of a master's thesis from the author's own data, quantitative (questionnaires, Excel, descriptive statistics, validity and reliability tests, correlation, regression), qualitative (interview transcripts, thematic coding), or mixed methods. Use for "Chapter 4", "Bab 4", "analyze my data", "olah data", "questionnaire analysis", "interview results", "discussion", "managerial implications". Never invents data, respondents, or references.
---

# Chapter 4: from data to a discussion draft

Flow: raw data → tables and charts → draft narrative → checked by the author. The author stays the author; this skill prepares a draft they check, understand, and change.

## Step 0: read the thesis profile

Look for `thesis-profile.md` in the thesis working folder (the folder Claude runs in). If it is missing, copy the template `${CLAUDE_PLUGIN_ROOT}/templates/thesis-profile.md` into the working folder and ask the author to fill in the blanks. Never guess the title, method, or research questions from memory or from file names.

**Language:** write every deliverable (drafts, tables, slides, scripts, lists) in the thesis language from the profile, **English by default**. Talk to the author in the language they use in chat.

Required before starting: research questions, method (Chapter 3), and where the data lives.

## Step 1: inventory the data

1. List every data file (name, type, rows or respondents, variables or columns).
2. Compare with Chapter 3: same sample size, instrument, and variables? Report any mismatch to the author; never fix it silently.
3. Replace personal data (names, phone numbers, identifiable job titles) with codes (R01, R02, Informant A) before analysis.

## Step 2: compute with code, not in your head

- Compute every number in one script, `analysis/analysis.py`, run through uv so its libraries install automatically:
  `uv run --with pandas --with scipy --with statsmodels --with openpyxl python analysis/analysis.py`
  Save results in `analysis/results/` (CSV or XLSX) so they can be rerun and checked by the supervisor. Do not use `pip install` or folders outside the thesis folder.
- If `uv` is not installed, stop and tell the author (installation is in the plugin README). Never compute by hand.
- State the test used, its assumptions (normality, multicollinearity, and so on), and the result of each assumption check. Tests follow Chapter 3; if the data do not fit the Chapter 3 test, report it and ask first.
- Qualitative: transcript → initial codes → categories → themes. Each theme gets short quotes with informant codes. Keep the coding table in `analysis/coding.xlsx` or `.md`.

## Step 3: outline Chapter 4 by research question

1. Overview of the research object and the respondent or informant profile.
2. One section per research question: findings (numbered tables or figures with their data source), then interpretation.
3. Discussion: relate findings to the theory and prior studies in Chapter 2. Cite only sources from Chapter 2 or ones verified with the `find-sources` skill.
4. Managerial implications (required for business or MBA theses): what the findings mean for the company or organization studied.

Show this outline to the author and get approval before writing the narrative.

## Step 4: write the draft

- Do only the sections requested; do not add analyses beyond Chapter 3 unless asked (mention them as suggestions).
- Write the draft in Markdown first (`chapter4-draft-<date>.md`). Produce .docx only when the author asks.
- One section per write. Follow the campus writing guide in the profile.
- Mark gaps: `[NEEDS DATA: ...]`, `[NEEDS SOURCE: ...]`, `[AUTHOR CHECK: ...]`.
- Association stays association (associated ≠ affects unless the design is causal). Non-significant ≠ no effect. Significant ≠ important.
- Never overwrite the original Word manuscript. Save the .docx as a new file. Choose the Word tool and any online mirror per `${CLAUDE_PLUGIN_ROOT}/references/document-tools.md`.

## Step 5: check before handing over

- Every number in the narrative matches the script output (compare one by one).
- Tables and figures are numbered in order and referenced in the text.
- Every research question is answered.
- Close with a short list: parts the author must check, marked gaps, and questions for the supervisor.

## Integrity

Follow the campus rules on AI use (see the guide in the thesis profile; disclose AI use when required). Never create data, respondents, interview quotes, or references that do not exist.
