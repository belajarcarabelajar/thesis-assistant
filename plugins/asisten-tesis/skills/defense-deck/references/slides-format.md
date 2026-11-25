# `slides.json` format for `scripts/build_pptx.py`

```json
{
  "wpm": 120,
  "theme": "academic",
  "slides": [
    {"layout": "title", "title": "Thesis title", "subtitle": "Name · Student ID · Programme · Defense date", "notes": "Opening script..."},
    {"layout": "bullets", "title": "Message sentence for this slide", "bullets": ["Short point", {"text": "Sub-point", "level": 1}], "notes": "..."},
    {"layout": "table", "title": "...", "table": {"header": ["Variable", "Cronbach's alpha"], "rows": [["Service Quality", "0.847"]]}, "caption": "Source: data analysis, 2026", "notes": "..."},
    {"layout": "chart", "title": "...", "chart": {"type": "column", "categories": ["SQ", "P"], "series": [{"name": "Coefficient", "values": [0.239, 0.265]}], "number_format": "0.000"}, "caption": "Source: ...", "notes": "..."},
    {"layout": "diagram", "title": "Research model", "boxes": [{"id": "X1", "text": "Service Quality (X1)", "col": 0}, {"id": "X2", "text": "Price (X2)", "col": 0}, {"id": "Y", "text": "Satisfaction (Y)", "col": 1}], "arrows": [["X1", "Y", "H1"], ["X2", "Y", "H2"]], "notes": "..."},
    {"layout": "bullets", "style": "dark", "title": "Thank you", "bullets": ["Questions and feedback are welcome"], "notes": "..."}
  ]
}
```

- `layout`: `title`, `bullets`, `table`, `chart` (`column`, `bar`, `line`, `pie`), `diagram` (boxes from the left column to the right column, labelled arrows).
- `theme`: `academic` (default; subtle gradients, navy and teal, slide numbers) or `plain`. Ignored when `--template` is used, because the campus template's design wins.
- `style: "dark"` gives a content slide the dark title-slide background (for example the closing slide).
- Table numbers are written as text exactly as in the manuscript. Chart values are numbers; bar and column axes start at zero.
- `notes` = the spoken script for that slide; `--script` copies it to a script file with an estimated duration.
- `--template` uses the masters and layouts of the campus template (layouts are picked automatically from their placeholders).
- Older Indonesian keys (`judul`, `poin`, `tabel`, `grafik`, `kolom`, `tema`, `gaya: gelap`, `--naskah`) are still accepted.
