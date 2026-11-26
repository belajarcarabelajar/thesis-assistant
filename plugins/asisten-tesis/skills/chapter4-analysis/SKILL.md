---
name: chapter4-analysis
description: Help draft Chapter 4 (results, findings, or business solution) of a master's thesis from the author's own data, following the method in Chapter 3, such as quantitative (questionnaires, statistics, regression, SEM-PLS output), qualitative (interviews, FGD, observation, document analysis), mixed methods, secondary data (company records, financial statements, industry reports), business analysis (root cause, PESTLE, Five Forces, VRIO, SWOT/TOWS), solution selection (AHP, Kepner-Tregoe), financial feasibility (NPV, IRR, sensitivity), and implementation plans. Use for "Chapter 4", "Bab 4", "analyze my data", "olah data", "business solution", "root cause", "AHP", "feasibility study", "discussion", "managerial implications". Never invents data, respondents, quotes, weights, or assumptions.
---

# Chapter 4: from data to a draft the author checks

Flow: the author's data and Chapter 3 method → analysis by script or from the author's tool output → outline in the campus chapter structure → draft narrative → checked by the author. The author stays the author; this skill prepares a draft they check, understand, and change.

## Step 0: read the thesis profile

Look for `thesis-profile.md` in the thesis working folder (the folder Claude runs in). If it is missing, copy the template `${CLAUDE_PLUGIN_ROOT}/templates/thesis-profile.md` into the working folder and ask the author to fill in the blanks. Never guess the title, method, or questions from memory or from file names.

**Language:** write every deliverable (drafts, tables, slides, scripts, lists) in the thesis language from the profile, **English by default**. Talk to the author in the language they use in chat.

Required before starting: thesis type, chapter map (what Chapter 4, and Chapter 5 if relevant, are called in the campus guide), research or business questions, the method in Chapter 3, and the data sources. If Chapter 3 is available, read it; it overrides the profile when they disagree (report the difference).

## Step 1: inventory every source

1. List every source the thesis uses, not only data files:
   - primary: questionnaire data, interview and FGD transcripts or notes, observation notes, expert judgment forms (for example AHP pairwise comparisons);
   - secondary: company documents and internal data (sales, operations, HR, financial statements), industry reports, government statistics, publications;
   - output already produced by the author's tools (SPSS, SmartPLS, NVivo, Excel models).
   For each: what it is, file, where it came from, period covered, size (rows, respondents, informants, pages), confidential or not.
2. Compare with Chapter 3: same sources, sample, instruments, variables, period? Report any mismatch to the author; never fix it silently.
3. Replace personal data (names, phone numbers, identifiable job titles) with codes (R01, Informant A) before analysis. Confidential company data stays in the thesis folder: never upload, share, or mirror it without the author's permission.

## Step 2: analyse the way Chapter 3 says

- Read the sections of `references/methods.md` that match the method in Chapter 3 (statistics, qualitative analysis, business analysis frameworks, solution selection, financial feasibility, implementation plan, mixed methods). If Chapter 3 does not say how something is analysed, ask before choosing.
- Compute every number in one script, `analysis/analysis.py`, run through uv so its libraries install automatically:
  `uv run --with pandas --with scipy --with statsmodels --with openpyxl python analysis/analysis.py`
  Save results in `analysis/results/` (CSV or XLSX) so they can be rerun and checked by the supervisor. Do not use `pip install` or folders outside the thesis folder. If `uv` is not installed, stop and tell the author (installation is in the plugin README). Never compute by hand.
- If Chapter 3 names a tool (SPSS, SmartPLS, NVivo, an Excel model), the author's exported output from that tool is the record: read and interpret it, and do not recompute it with a different algorithm. Point out numbers in the output that look wrong.
- State each test or technique, its assumptions, and the result of each assumption check. If the data do not fit the Chapter 3 technique, report it and ask first.
- Every claim in a framework (SWOT, PESTLE, fishbone, and so on) points to its evidence: an informant code, a document, or a data file. No evidence → `[NEEDS DATA: ...]`, never generic textbook entries.

## Step 3: outline Chapter 4 in the campus structure

Use the chapter map for headings and order. Typical shapes, to adapt, not to impose:

- **Research thesis:** research object and respondent or informant profile → findings per research question (numbered tables or figures with their data source) → discussion against Chapter 2 theory and prior studies → managerial implications.
- **Business solution / final project:** business situation and evidence → root cause analysis → alternative solutions → selected solution with the selection method and its result → implementation plan (when the chapter map puts it in Chapter 4; otherwise leave it for Chapter 5).

Cite only sources from Chapter 2 or ones verified with the `find-sources` skill. Show this outline to the author and get approval before writing the narrative.

## Step 4: write the draft

- Do only the sections requested; do not add analyses beyond Chapter 3 unless asked (mention them as suggestions).
- Write the draft in Markdown first (`chapter4-draft-<date>.md`). Produce .docx only when the author asks.
- One section per write. Follow the campus writing guide in the profile.
- Mark gaps: `[NEEDS DATA: ...]`, `[NEEDS SOURCE: ...]`, `[AUTHOR CHECK: ...]`.
- Association stays association (associated ≠ affects unless the design is causal). Non-significant ≠ no effect. Significant ≠ important. A management estimate is labelled as an estimate.
- Never overwrite the original Word manuscript. Save the .docx as a new file. Choose the Word tool and any online mirror per `${CLAUDE_PLUGIN_ROOT}/references/document-tools.md`.

## Step 5: check before handing over

- Every number in the narrative matches the script output or the author's tool output (compare one by one).
- Every framework entry, root cause, weight, and financial assumption has a source.
- Tables and figures are numbered in order and referenced in the text.
- Every research or business question is answered.
- Close with a short list: parts the author must check, marked gaps, and questions for the supervisor.

## Integrity

Follow the campus rules on AI use (see the guide in the thesis profile; disclose AI use when required). Never create data, respondents, interview quotes, expert judgments, financial assumptions, or references that do not exist.
