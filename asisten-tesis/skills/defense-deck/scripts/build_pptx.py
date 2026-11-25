"""Build an editable thesis-defense deck (.pptx) from a JSON spec.

Usage:
  uv run --with python-pptx python build_pptx.py slides.json out.pptx [--template campus.pptx] [--script script.md]

Text goes into layout placeholders (title, body) so the theme and fonts can be changed in PowerPoint.
No decorative lines, icons, or images. Tables are PowerPoint tables, charts are PowerPoint charts.
Without --template the restrained "academic" theme is applied (set "theme": "plain" to turn it off).
Spec format: ../references/slides-format.md (Indonesian keys from older specs are still accepted).
"""
import argparse, json, sys
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR, PP_PLACEHOLDER
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor

# "academic" theme: two related colours (navy + teal), subtle background gradient, no accent lines.
THEMES = {
    "academic": {
        "dark_bg": ("17304F", "24507A"),    # title/closing slides: dark-blue gradient
        "light_bg": ("FFFFFF", "EDF2F7"),   # content slides: white to pale blue-grey, barely visible
        "title": "17304F", "text": "2B2B2B", "muted": "6B7785", "light": "FFFFFF", "light_sub": "C9D6E3",
        "palette": ["1F4E79", "2A8C8C", "C9A227", "8A99A8"],
        "table_head": "1F4E79", "table_rows": ("FFFFFF", "E8EEF4"),
    },
}

TITLE_TYPES = {PP_PLACEHOLDER.TITLE, PP_PLACEHOLDER.CENTER_TITLE}
BODY_TYPES = {PP_PLACEHOLDER.BODY, PP_PLACEHOLDER.OBJECT}


def ph_types(layout):
    return [p.placeholder_format.type for p in layout.placeholders]


def pick_layout(prs, kind):
    layouts = list(prs.slide_layouts)
    def score(l):
        t = ph_types(l)
        has_title = any(x in TITLE_TYPES for x in t)
        has_center = PP_PLACEHOLDER.CENTER_TITLE in t
        n_body = sum(1 for x in t if x in BODY_TYPES)
        has_sub = PP_PLACEHOLDER.SUBTITLE in t
        if kind == "title":
            return (has_center or (has_title and has_sub)) * 10 - n_body
        if kind == "bullets":
            return has_title * 5 + (n_body == 1) * 10 - has_center * 3
        return has_title * 5 + (n_body == 0) * 10 - has_center * 3 - has_sub * 2
    return max(layouts, key=score)


def title_ph(slide):
    for p in slide.placeholders:
        if p.placeholder_format.type in TITLE_TYPES:
            return p
    return None


def remove_empty_placeholders(slide, keep):
    for p in list(slide.placeholders):
        if p not in keep and not (p.has_text_frame and p.text_frame.text.strip()):
            p._element.getparent().remove(p._element)


def content_box(prs, slide):
    t = title_ph(slide)
    margin = Inches(0.6)
    top = (t.top + t.height + Inches(0.2)) if t is not None else Inches(1.4)
    return margin, top, prs.slide_width - 2 * margin, prs.slide_height - top - Inches(0.5)


def add_caption(slide, prs, text):
    if not text:
        return
    left = Inches(0.6)
    tb = slide.shapes.add_textbox(left, prs.slide_height - Inches(0.55), prs.slide_width - 2 * left, Inches(0.4))
    tb.text_frame.text = text
    for para in tb.text_frame.paragraphs:
        for r in para.runs:
            r.font.size = Pt(12)


def rgb(h):
    return RGBColor.from_string(h)


def gradient(slide, colors, angle=90):
    fill = slide.background.fill
    fill.gradient()
    fill.gradient_angle = angle
    stops = fill.gradient_stops
    stops[0].color.rgb, stops[0].position = rgb(colors[0]), 0
    stops[1].color.rgb, stops[1].position = rgb(colors[1]), 1.0


def color_text(shape, color, bold=None):
    if not shape.has_text_frame:
        return
    for para in shape.text_frame.paragraphs:
        for r in para.runs:
            r.font.color.rgb = rgb(color)
            if bold is not None:
                r.font.bold = bold


def apply_theme(slide, s, kind, th, number, total):
    dark = kind == "title" or s.get("style") == "dark"
    gradient(slide, th["dark_bg"] if dark else th["light_bg"], 45 if dark else 90)
    t = title_ph(slide)
    for sh in slide.shapes:
        if sh == t:
            color_text(sh, th["light"] if dark else th["title"], bold=True)
        elif sh.has_text_frame and not getattr(sh, "is_placeholder", False) and sh.shape_type == 17:
            # free text box: caption/source
            color_text(sh, th["light_sub"] if dark else th["muted"])
        elif sh.has_text_frame and getattr(sh, "is_placeholder", False):
            color_text(sh, th["light_sub"] if dark else th["text"])
        if sh.has_table:
            tb = sh.table
            for r in range(len(tb.rows)):
                for c in range(len(tb.columns)):
                    cell = tb.cell(r, c)
                    cell.fill.solid()
                    cell.fill.fore_color.rgb = rgb(th["table_head"] if r == 0 else th["table_rows"][r % 2])
                    for para in cell.text_frame.paragraphs:
                        for run in para.runs:
                            run.font.color.rgb = rgb(th["light"] if r == 0 else th["text"])
                            run.font.bold = r == 0
        if sh.has_chart:
            ch = sh.chart
            plot = ch.plots[0]
            if ch.chart_type == XL_CHART_TYPE.PIE:
                pie_colors = [th["palette"][0], th["palette"][3], th["palette"][1], th["palette"][2]]
                for i, pt in enumerate(plot.series[0].points):
                    pt.format.fill.solid(); pt.format.fill.fore_color.rgb = rgb(pie_colors[i % 4])
            elif len(plot.series) == 1:
                for i, pt in enumerate(plot.series[0].points):
                    pt.format.fill.solid(); pt.format.fill.fore_color.rgb = rgb(th["palette"][i % 4])
            else:
                for i, ser in enumerate(plot.series):
                    ser.format.fill.solid(); ser.format.fill.fore_color.rgb = rgb(th["palette"][i % 4])
    for sh in slide.shapes:
        if sh.shape_type == 1 and s.get("layout") == "diagram":  # diagram box
            idx = s["boxes"][[b["text"] for b in s["boxes"]].index(sh.text_frame.text)].get("col", 0) if sh.text_frame.text in [b["text"] for b in s["boxes"]] else 0
            sh.fill.solid(); sh.fill.fore_color.rgb = rgb(th["palette"][1] if idx == 1 else th["palette"][0])
            color_text(sh, th["light"])
    if not dark and number > 1:
        # slide number: lets examiners refer to "slide 7"
        prs_w, prs_h = slide.part.package.presentation_part.presentation.slide_width, slide.part.package.presentation_part.presentation.slide_height
        tb = slide.shapes.add_textbox(prs_w - Inches(1.1), prs_h - Inches(0.55), Inches(0.7), Inches(0.4))
        tb.text_frame.text = f"{number}/{total}"
        para = tb.text_frame.paragraphs[0]
        from pptx.enum.text import PP_ALIGN
        para.alignment = PP_ALIGN.RIGHT
        for r in para.runs:
            r.font.size = Pt(12); r.font.color.rgb = rgb(th["muted"])


def build(spec, out, template=None):
    prs = Presentation(template) if template else Presentation()
    if not template:
        # python-pptx's default template is 4:3; widen to 16:9 and stretch master/layout placeholders to match
        k = Inches(13.333) / prs.slide_width
        prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
        # read every position (including ones inherited from the master) first, then write all four;
        # setting only left turns an inherited placeholder's top/height into 0
        geo = []
        for holder in [prs.slide_master] + list(prs.slide_layouts):
            for sh in holder.shapes:
                if None not in (sh.left, sh.top, sh.width, sh.height):
                    geo.append((sh, sh.left, sh.top, sh.width, sh.height))
        for sh, l, t, w, h in geo:
            sh.left, sh.top, sh.width, sh.height = int(l * k), t, int(w * k), h
    for i, s in enumerate(spec["slides"], 1):
        kind = s.get("layout", "bullets")
        lay_kind = kind if kind in ("title", "bullets") else "blank"
        slide = prs.slides.add_slide(pick_layout(prs, lay_kind))
        keep = []
        t = title_ph(slide)
        if t is not None:
            t.text_frame.text = s["title"]
            t.text_frame.word_wrap = True
            size = Pt(40) if kind == "title" else Pt(36)
            if len(s["title"]) > (60 if kind == "title" else 50):
                size = Pt(34) if kind == "title" else Pt(30)
            for para in t.text_frame.paragraphs:
                for r in para.runs:
                    r.font.size = size
            keep.append(t)
        if kind == "title":
            sub = next((p for p in slide.placeholders if p.placeholder_format.type in (PP_PLACEHOLDER.SUBTITLE, PP_PLACEHOLDER.BODY)), None)
            if sub is not None and s.get("subtitle"):
                sub.text_frame.text = s["subtitle"]
                keep.append(sub)
        elif kind == "bullets":
            body = next((p for p in slide.placeholders if p.placeholder_format.type in BODY_TYPES), None)
            if body is None:
                l, tp, w, h = content_box(prs, slide)
                body = slide.shapes.add_textbox(l, tp, w, h)
            tf = body.text_frame
            for j, b in enumerate(s.get("bullets", [])):
                para = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
                text, level = (b, 0) if isinstance(b, str) else (b["text"], b.get("level", 0))
                para.text, para.level = text, level
                for r in para.runs:
                    r.font.size = Pt(24) if level == 0 else Pt(20)
            keep.append(body)
        elif kind == "table":
            tbl = s["table"]
            rows, cols = len(tbl["rows"]) + 1, len(tbl["header"])
            l, tp, w, h = content_box(prs, slide)
            row_h = Inches(0.5)
            shape = slide.shapes.add_table(rows, cols, l, tp, w, row_h * rows)
            for c, head in enumerate(tbl["header"]):
                shape.table.cell(0, c).text = str(head)
            for r, row in enumerate(tbl["rows"], 1):
                for c, val in enumerate(row):
                    shape.table.cell(r, c).text = str(val)
            for r in range(rows):
                for c in range(cols):
                    for para in shape.table.cell(r, c).text_frame.paragraphs:
                        for run in para.runs:
                            run.font.size = Pt(20)
        elif kind == "chart":
            ch = s["chart"]
            data = CategoryChartData()
            data.categories = ch["categories"]
            for ser in ch["series"]:
                data.add_series(ser["name"], ser["values"])
            ctype = {"bar": XL_CHART_TYPE.BAR_CLUSTERED, "column": XL_CHART_TYPE.COLUMN_CLUSTERED,
                     "line": XL_CHART_TYPE.LINE_MARKERS, "pie": XL_CHART_TYPE.PIE}[ch.get("type", "column")]
            l, tp, w, h = content_box(prs, slide)
            gf = slide.shapes.add_chart(ctype, l, tp, w, h - Inches(0.4), data)
            chart = gf.chart
            chart.has_legend = len(ch["series"]) > 1  # pie uses direct labels, not a legend
            if chart.has_legend:
                chart.legend.position, chart.legend.include_in_layout = XL_LEGEND_POSITION.BOTTOM, False
            plot = chart.plots[0]
            plot.has_data_labels = True
            if ctype != XL_CHART_TYPE.PIE and all(v >= 0 for ser in ch["series"] for v in ser["values"]):
                chart.value_axis.minimum_scale = 0  # axis from zero so differences are not exaggerated
            if ch.get("title"):
                chart.has_title = True
                chart.chart_title.text_frame.text = ch["title"]
            else:
                chart.has_title = False
            if ch.get("number_format"):
                plot.data_labels.number_format = ch["number_format"]
                plot.data_labels.number_format_is_linked = False
            if ctype == XL_CHART_TYPE.PIE:
                plot.data_labels.show_category_name = True
                plot.data_labels.font.size = Pt(14)
        elif kind == "diagram":
            # left column = independent variables, right column = dependent; arrows left to right
            l, tp, w, h = content_box(prs, slide)
            boxes = s["boxes"]
            cols = {0: [b for b in boxes if b.get("col", 0) == 0], 1: [b for b in boxes if b.get("col", 0) == 1]}
            bw, bh = Inches(3.6), Inches(1.0)
            pos = {}
            for c, items in cols.items():
                x = l + (Inches(0.4) if c == 0 else w - bw - Inches(0.4))
                gap = (h - bh * len(items)) / (len(items) + 1) if items else 0
                for k, b in enumerate(items):
                    y = tp + gap * (k + 1) + bh * k
                    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, int(y), bw, bh)
                    shp.text_frame.text = b["text"]
                    shp.fill.solid()
                    shp.fill.fore_color.theme_color = MSO_THEME_COLOR.ACCENT_1
                    shp.shadow.inherit = False
                    for para in shp.text_frame.paragraphs:
                        for r in para.runs:
                            r.font.size = Pt(18)
                    pos[b["id"]] = shp
            for a in s.get("arrows", []):
                src, dst = pos[a[0]], pos[a[1]]
                con = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, 0, 0, 0, 0)
                con.begin_connect(src, 3)
                con.end_connect(dst, 1)
                con.line.width = Pt(2)
                ln = con.line._get_or_add_ln()
                tail = ln.makeelement("{http://schemas.openxmlformats.org/drawingml/2006/main}tailEnd", {"type": "triangle"})
                ln.append(tail)
                if len(a) > 2 and a[2]:
                    mx, my = (src.left + src.width + dst.left) // 2, (src.top + dst.top + bh) // 2
                    tb = slide.shapes.add_textbox(mx - Inches(0.4), my - Inches(0.45), Inches(0.8), Inches(0.4))
                    tb.text_frame.text = a[2]
        else:
            sys.exit(f"slide {i}: unknown layout: {kind}")
        add_caption(slide, prs, s.get("caption"))
        remove_empty_placeholders(slide, keep)
        if s.get("notes"):
            slide.notes_slide.notes_text_frame.text = s["notes"]
        theme_name = spec.get("theme", "academic")
        if not template and theme_name in THEMES:
            apply_theme(slide, s, kind, THEMES[theme_name], i, len(spec["slides"]))
    prs.save(out)
    return prs

def write_script(spec, path, wpm):
    lines = ["# Defense presentation script", "", f"Pace: {wpm} words per minute.", ""]
    total = 0
    for i, s in enumerate(spec["slides"], 1):
        n = len(s.get("notes", "").split())
        total += n
        lines += [f"## Slide {i}: {s['title']}", "", f"Estimate: {n / wpm * 60:.0f} s ({n} words)", "", s.get("notes", "(no script yet)"), ""]
    m, d = divmod(round(total / wpm * 60), 60)
    lines.insert(3, f"Estimated total: {m} min {d} s ({total} words).")
    lines.insert(4, "")
    open(path, "w", encoding="utf-8").write("\n".join(lines))
    return total / wpm


# Older Indonesian specs keep working.
ALIASES = {"layout": {"judul": "title", "poin": "bullets", "tabel": "table", "grafik": "chart"},
           "chart": {"kolom": "column", "garis": "line"}, "theme": {"akademik": "academic", "polos": "plain"}}


def normalize(spec):
    if "tema" in spec:
        spec["theme"] = spec.pop("tema")
    spec["theme"] = ALIASES["theme"].get(spec.get("theme", "academic"), spec.get("theme", "academic"))
    for s in spec["slides"]:
        s["layout"] = ALIASES["layout"].get(s.get("layout", "bullets"), s.get("layout", "bullets"))
        if s.get("gaya") == "gelap":
            s["style"] = "dark"
        if "chart" in s:
            s["chart"]["type"] = ALIASES["chart"].get(s["chart"].get("type", "column"), s["chart"].get("type", "column"))
    return spec


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("spec"); ap.add_argument("out")
    ap.add_argument("--template"); ap.add_argument("--script", "--naskah", dest="script")
    a = ap.parse_args()
    spec = normalize(json.load(open(a.spec, encoding="utf-8")))
    build(spec, a.out, a.template)
    msg = f"OK {a.out}: {len(spec['slides'])} slides"
    if a.script:
        msg += f", script {a.script} (~{write_script(spec, a.script, spec.get('wpm', 120)):.1f} min)"
    print(msg)
