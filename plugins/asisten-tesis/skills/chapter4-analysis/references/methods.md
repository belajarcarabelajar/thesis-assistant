# Method notes for chapter4-analysis

Read only the sections that match the method in Chapter 3. These notes describe how to do each analysis honestly; they do not replace what Chapter 3 and the supervisor decided.

## Contents

1. Quantitative survey data
2. SEM-PLS and other tool output
3. Secondary and company data
4. Qualitative data (interviews, FGD, observation, documents)
5. Business issue analysis frameworks
6. Root cause analysis
7. Solution selection (AHP, Kepner-Tregoe)
8. Financial feasibility
9. Implementation plan
10. Mixed methods

## 1. Quantitative survey data

- Respondent profile, then descriptive statistics per item and variable (mean, standard deviation, category per the scale in Chapter 3).
- Validity and reliability as Chapter 3 specifies (for example item-total correlation, Cronbach's alpha).
- Assumption checks before inference (normality of residuals, multicollinearity, heteroscedasticity for regression), each with its result.
- Report coefficients, standard errors, test statistics, p-values, and R² from the script output. Interpret direction and size, not only significance.

## 2. SEM-PLS and other tool output

- When Chapter 3 uses SmartPLS, SPSS, AMOS, NVivo, or similar, ask the author for the exported output (report, Excel, or PDF) and work from it.
- SEM-PLS reporting order: measurement model (outer loadings, AVE, composite reliability, discriminant validity such as HTMT), then structural model (R², path coefficients, bootstrapped t and p values, f² or Q² if reported).
- Do not re-estimate the model in Python with a different algorithm. Quote the tool's numbers and flag values outside common thresholds for the author to check.

## 3. Secondary and company data

- Record for each dataset: source (department, document, publisher), period, unit, definitions, and gaps. Note revisions or breaks in the series.
- Trends: show the actual series (table or chart), then the change in absolute and percentage terms. Seasonality or one-off events are described from evidence (documents, interviews), not guessed.
- Ratios (margin, turnover, growth) use the formula stated in the text.
- Forecasts only if Chapter 3 includes them: state the method and its assumptions, show the fit on past data, and label the result as a projection.

## 4. Qualitative data (interviews, FGD, observation, documents)

- Keep a source list with codes (Informant A, FGD-1, Obs-2, Doc-3) and the date of each.
- Coding: transcript or notes → initial codes → categories → themes. Keep the coding table in `analysis/coding.xlsx` or `.md`.
- Each theme gets short verbatim quotes or document excerpts with their codes.
- Triangulate: say where interviews, documents, observation, and data agree or disagree. Disagreement is a finding, not something to smooth over.

## 5. Business issue analysis frameworks

Typical: PESTLE, Porter's Five Forces, competitor analysis (external); VRIO, value chain, resources and capabilities (internal); SWOT summarising both and TOWS turning it into strategy options.

- Every entry names its evidence (informant code, document, data file, or a verified external source). An entry without evidence becomes `[NEEDS DATA: ...]`.
- Keep entries specific to the company and period studied. Remove generic statements that would fit any company.
- SWOT items come from the external and internal analyses above; TOWS strategies combine named SWOT items (for example S2 + O1).

## 6. Root cause analysis

- Fishbone (Ishikawa): categories as used in Chapter 3 (for example people, process, technology, environment); each cause linked to evidence.
- 5 whys: each "why" step supported by an interview, document, or data point.
- Pareto: only from counted data (complaints, defects, lost orders); show the counts and cumulative percentages.
- FMEA: severity, occurrence, and detection ratings come from the author's team or experts as recorded in the data; compute RPN from those ratings.
- End with the root causes the thesis will address and why (impact, controllability), as Chapter 3 defines.

## 7. Solution selection

**AHP**
- Pairwise comparison judgments come only from real respondents (expert judgment forms in the data). Never fill in a missing judgment.
- Compute priority weights with the principal eigenvector and report λmax, the consistency index CI = (λmax − n) / (n − 1), and the consistency ratio CR = CI / RI, with Saaty's random index (n = 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45).
- CR above 0.10 means the judgments are inconsistent: report it per respondent and ask the author whether to re-ask that respondent. Do not silently drop or adjust the matrix.
- Several experts: aggregate individual judgments with the geometric mean (unless Chapter 3 says otherwise) and report the CR of the aggregate as well.
- numpy (installed with pandas) is enough: `numpy.linalg.eig`.

**Kepner-Tregoe decision analysis**
- Musts (pass/fail) and wants (weighted) as defined with the stakeholders in the data; each score has a source. Report the weighted totals and the risks of the leading alternative.

## 8. Financial feasibility

- Start with an assumptions table: each figure (investment, revenue, costs, growth, horizon, tax, discount rate or WACC, terminal value) with its source (company data, quotation, market data, or a management estimate labelled as such).
- A missing figure, especially the discount rate, is `[NEEDS DATA: ...]` and a question for the author. Never choose a rate yourself.
- Compute NPV, IRR, payback period, and profitability index in the script (IRR with `scipy.optimize.brentq` on the NPV function). Show the cash flow table.
- Sensitivity analysis on the main drivers named in Chapter 3 (for example ±10% and ±20% on price, volume, cost), and scenarios if Chapter 3 includes them.

## 9. Implementation plan

- A table of activities with owner, start and end (or a simple Gantt table), resources or budget, KPIs with targets, and risks with mitigation.
- Each activity traces back to a root cause or selected solution element. Budget figures come from the financial analysis or labelled estimates.

## 10. Mixed methods

- State the design from Chapter 3 (for example explanatory sequential: quantitative first, then qualitative to explain it) and keep that order in the chapter.
- Show where the strands meet, for example a joint display table placing each quantitative result beside the qualitative explanation.
