---
name: find-sources
description: Find and verify scholarly references for a thesis (journals, books, official reports) and build an APA 7 reference list. Use for "find journals", "cari jurnal", "find references for the theory of ...", "previous studies", "literature", "reference list", "daftar pustaka", "check citations", "APA format". Every reference is checked to exist; never invents titles, authors, DOIs, or pages.
---

# Find sources and APA 7 citations

## Step 0: read the thesis profile

Look for `thesis-profile.md` in the thesis working folder (the folder Claude runs in). If it is missing, copy the template `${CLAUDE_PLUGIN_ROOT}/templates/thesis-profile.md` into the working folder and ask the author to fill in the blanks. Never guess the title, method, or research questions from memory or from file names.

**Language:** write every deliverable (drafts, tables, slides, scripts, lists) in the thesis language from the profile, **English by default**. Talk to the author in the language they use in chat.

Used from the profile: topic, key variables or concepts, and the campus citation style (APA 7 by default).

## Flow

1. **Define the need.** Which claim or concept needs support? Write 3-6 keywords in English (plus Indonesian when local studies matter).
2. **Search.**
   - TinyFish `search` with `domain_type: "research_paper"` for journals; normal web search for official reports (statistics agencies, ministries, industry associations).
   - Metadata from OpenAlex (`https://api.openalex.org/works?search=...`) or Crossref (`https://api.crossref.org/works?query=...`).
   - Prefer reputable journals (Scopus-indexed, or SINTA for Indonesian journals) and work from the last 10 years, except classic theory.
3. **Verify every reference before use.**
   - Title, authors, year, and journal or publisher match the original source.
   - The DOI or URL actually opens (not a 404).
   - Read the abstract or the relevant section and note the sentence that supports the claim. A reference whose content does not support the claim is not used.
4. **Build APA 7.** For references with a DOI, take the entry from the DOI service instead of typing it:
   `curl -LH "Accept: text/x-bibliography; style=apa" https://doi.org/<DOI>`
   (in PowerShell write `curl.exe`, not `curl`), then tidy it if needed (title capitalization, italic journal name once in Word).
5. **Deliver** a table: APA reference, DOI/URL, supporting quote, claim supported, verification status.

## Rules

- In-text citations and the reference list must pair up (no orphans).
- References that cannot be verified are marked `[UNVERIFIED]` and stay out of the manuscript.
- Do not send thesis text to outside services without the author's permission; send keywords only.
- TinyFish `search` and `fetch_content` are enough here. If browser automation is unavoidable, close its session (`close_browser_session`) afterwards because it is billed.
