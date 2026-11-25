"""Check a deck: words per slide, speaker notes, decoration, images, title length.

Usage: uv run --with python-pptx python check_pptx.py deck.pptx [--max-words 30]
Exits 1 when there are findings that must be fixed.
"""
import argparse, re, sys
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

ap = argparse.ArgumentParser(); ap.add_argument("pptx"); ap.add_argument("--max-words", "--maks-kata", dest="max_words", type=int, default=30)
a = ap.parse_args()
prs = Presentation(a.pptx)
problems = 0
for i, s in enumerate(prs.slides, 1):
    words, notes, found = 0, "", []
    for sh in s.shapes:
        if sh.has_text_frame:
            if re.fullmatch(r"\d+/\d+", sh.text_frame.text.strip()):
                continue  # slide number added by the builder
            words += len(sh.text_frame.text.split())
            for p in sh.text_frame.paragraphs:
                if any(ord(ch) > 0x2600 for ch in p.text):
                    found.append("emoji/decorative symbol")
        if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
            found.append("image (make sure it explains content)")
        if sh.shape_type == MSO_SHAPE_TYPE.LINE and not sh._element.xpath(".//a:stCxn"):
            found.append("loose line (decoration?)")
    if s.has_notes_slide:
        notes = s.notes_slide.notes_text_frame.text
    title = s.shapes.title.text if s.shapes.title is not None else ""
    if words > a.max_words and i > 1:
        found.append(f"{words} words > {a.max_words}")
    if not notes.strip():
        found.append("empty speaker notes")
    if not title.strip():
        found.append("no title")
    elif len(title) > (120 if i == 1 else 70):
        found.append(f"title {len(title)} chars > {120 if i == 1 else 70} (may collide with content)")
    must = [f for f in found if not f.startswith("image")]
    problems += len(must)
    print(f"slide {i:2d}: {words:3d} words, notes {len(notes.split()):3d} words" + (f"  ! {', '.join(found)}" if found else ""))
print("OK" if not problems else f"{problems} findings must be fixed")
sys.exit(1 if problems else 0)
