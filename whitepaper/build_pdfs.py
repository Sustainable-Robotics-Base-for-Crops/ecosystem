#!/usr/bin/env python3
"""Build WHITEPAPER-SHORT.<lang>.pdf from WHITEPAPER-SHORT.<lang>.md with the manifesto layout."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

HERE = Path(__file__).resolve().parent
MANIFESTO_DIR = HERE.parent / "manifesto"

_spec = importlib.util.spec_from_file_location("manifesto_layout", MANIFESTO_DIR / "build_pdfs.py")
mf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mf)

LANGS = mf.LANGS

HEADER_RIGHT = {
    "fr": "Livre blanc",
    "en": "White paper",
    "de": "Weißbuch",
    "it": "Libro bianco",
    "es": "Libro blanco",
}

REFERENCE_TITLES = {"Références", "References", "Literatur", "Riferimenti", "Referencias"}
JOIN_PREFIXES = ("Rejoindre", "Join the ecosystem", "Dem Ökosystem", "Unirsi", "Unirse")


def extra_styles(styles, font, font_b):
    styles.add(
        ParagraphStyle(
            name="Reference", parent=styles["BodyJust"], fontSize=8.3, leading=10.8,
            alignment=TA_LEFT, spaceAfter=3,
        )
    )
    styles.add(ParagraphStyle(name="Cell", fontName=font, fontSize=8.6, leading=11, textColor=mf.GRAY))
    styles.add(ParagraphStyle(name="CellHead", parent=styles["Cell"], fontName=font_b, textColor=mf.BROWN))
    return styles


def make_table(rows, styles, width):
    data = [
        [Paragraph(mf.inline(c), styles["CellHead" if r == 0 else "Cell"]) for c in row]
        for r, row in enumerate(rows)
    ]
    ratios = [0.30, 0.19, 0.22, 0.29]
    table = Table(data, colWidths=[width * x for x in ratios], repeatRows=1, hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), mf.CALLOUT_BG),
                ("LINEABOVE", (0, 0), (-1, 0), 1.2, mf.ORANGE),
                ("LINEBELOW", (0, 0), (-1, -1), 0.5, mf.RULE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def build_pdf(lang: str, font, font_b, font_i):
    md_path = HERE / f"WHITEPAPER-SHORT.{lang}.md"
    pdf_path = HERE / f"WHITEPAPER-SHORT.{lang}.pdf"
    styles = extra_styles(mf.build_styles(font, font_b, font_i), font, font_b)
    lines = md_path.read_text(encoding="utf-8").splitlines()
    width = A4[0] - 4 * cm

    story = []
    in_refs = False
    title = ""
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            story.append(Spacer(1, 4))
            story.append(HRFlowable(width="100%", thickness=0.5, color=mf.RULE, spaceBefore=2, spaceAfter=10))
            i += 1
            continue

        if stripped.startswith("# "):
            title = stripped[2:]
            story.append(Paragraph(mf.inline(title), styles["MainTitle"]))
            i += 1
            continue

        if stripped.startswith("### "):
            story.append(Paragraph(mf.inline(stripped[4:]), styles["SubTitle"]))
            i += 1
            continue

        if stripped.startswith("## "):
            heading = re.sub(r"\s*\{#[^}]+\}", "", stripped[3:]).strip()
            in_refs = heading in REFERENCE_TITLES
            story.append(Paragraph(mf.inline(heading), styles["H2"]))
            i += 1
            if heading == mf.TOC_TITLES[lang]:
                while i < len(lines) and not lines[i].strip():
                    i += 1
                n = 1
                while i < len(lines) and lines[i].strip() and lines[i].strip() != "---":
                    item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                    item = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", item)
                    story.append(Paragraph(mf.inline(f"{n}. {item}"), styles["TOCItem"]))
                    n += 1
                    i += 1
                story.append(Spacer(1, 4))
            continue

        if re.match(r"^(Auteur|Author|Autor|Autore)\s*:", stripped, flags=re.IGNORECASE) or (
            stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**")
        ):
            story.append(Paragraph(mf.inline(stripped), styles["AuthorLine"]))
            i += 1
            continue

        if stripped.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip("> ").strip())
                i += 1
            story += [Spacer(1, 6), mf.make_callout(quote, styles), Spacer(1, 8)]
            continue

        if stripped.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            story += [Spacer(1, 2), make_table(rows, styles, width), Spacer(1, 8)]
            continue

        if stripped.startswith("**") and re.sub(r"\*\*", "", stripped) in mf.CONTACT_LABELS.values():
            block = [Paragraph(mf.inline(stripped), styles["SectionLabel"])]
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            while i < len(lines):
                item = re.sub(r"^[-*]\s+", "", lines[i].strip())
                m = re.match(r"^(GitHub|LinkedIn)\s*:\s*\[([^\]]+)\]\(([^)]+)\)", item)
                if not m:
                    break
                icon = mf.ASSETS / ("github.png" if m.group(1) == "GitHub" else "linkedin.png")
                block.append(mf.contact_row(m.group(1), icon, m.group(2), m.group(3), styles))
                i += 1
            story.append(KeepTogether(block))
            continue

        if re.match(r"^[-*]\s+", stripped):
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i].strip()):
                item = re.sub(r"^[-*]\s+", "", lines[i].strip())
                story.append(Paragraph(f"• {mf.inline(item)}", styles["BulletItem"]))
                i += 1
            story.append(Spacer(1, 4))
            continue

        if stripped.startswith("**") and stripped.startswith(tuple(f"**{p}" for p in JOIN_PREFIXES)):
            block = [Paragraph(mf.inline(stripped), styles["Join"])]
            i += 1
            if i < len(lines) and lines[i].strip():
                block.append(Paragraph(mf.inline(lines[i].strip()), styles["BodyJust"]))
                i += 1
            story.append(KeepTogether(block))
            continue

        if stripped.startswith("**Alexandre"):
            story.append(Paragraph(mf.inline(stripped), styles["AuthorName"]))
            i += 1
            continue

        if stripped in mf.ROLE_LINES.values():
            story.append(Paragraph(mf.inline(stripped), styles["AuthorRole"]))
            i += 1
            continue

        paragraph = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith(("#", ">", "|", "---")) or re.match(r"^[-*]\s+", nxt):
                break
            paragraph.append(nxt)
            i += 1
        text = " ".join(paragraph)
        if in_refs:
            style = styles["Reference"]
        elif "**" in text and len(text) < 180:
            style = styles["BodyStrong"]
        else:
            style = styles["BodyJust"]
        story.append(Paragraph(mf.inline(text), style))

    def header_footer(canvas, doc):
        canvas.saveState()
        w, h = A4
        canvas.setStrokeColor(mf.RULE)
        canvas.setLineWidth(0.7)
        canvas.line(2 * cm, h - 1.4 * cm, w - 2 * cm, h - 1.4 * cm)
        canvas.setFillColor(mf.MUTED)
        canvas.setFont(font, 8)
        canvas.drawString(2 * cm, h - 1.2 * cm, "Sustainable Robotics Base for Crops")
        canvas.drawRightString(w - 2 * cm, h - 1.2 * cm, HEADER_RIGHT[lang])
        canvas.line(2 * cm, 1.35 * cm, w - 2 * cm, 1.35 * cm)
        canvas.drawCentredString(w / 2, 1.0 * cm, str(doc.page))
        canvas.restoreState()

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2.1 * cm,
        bottomMargin=1.8 * cm,
        title=title,
        author="Alexandre Prévault-Osmani",
    )
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return pdf_path, doc.page


def main(argv: list[str]) -> int:
    mf.ensure_icons()
    font, font_b, font_i = mf.register_fonts()
    pdfmetrics.registerFontFamily(font, normal=font, bold=font_b, italic=font_i, boldItalic=font_b)
    for lang in argv[1:] or list(LANGS):
        if lang not in LANGS:
            print(f"skip unknown lang: {lang}", file=sys.stderr)
            continue
        path, pages = build_pdf(lang, font, font_b, font_i)
        print(f"built {path.name} ({pages} pages, {path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
