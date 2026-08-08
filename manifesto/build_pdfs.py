#!/usr/bin/env python3
"""Build MANIFESTO.<lang>.pdf from MANIFESTO.<lang>.md with the official layout."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Flowable,
    HRFlowable,
    Image as RLImage,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

HERE = Path(__file__).resolve().parent
ASSETS = HERE / ".pdf_assets"
LANGS = ("fr", "en", "de", "it", "es")

BROWN = HexColor("#302828")
ORANGE = HexColor("#C85830")
INK = HexColor("#1A1A1A")
GRAY = HexColor("#3A3A3A")
MUTED = HexColor("#6B6560")
RULE = HexColor("#E2D8D0")
CALLOUT_BG = HexColor("#F8F1EB")
CALLOUT_BORDER = HexColor("#C85830")

HEADER_RIGHT = {
    "fr": "Manifeste",
    "en": "Manifesto",
    "de": "Manifest",
    "it": "Manifesto",
    "es": "Manifiesto",
}

TOC_TITLES = {
    "fr": "Sommaire",
    "en": "Contents",
    "de": "Inhalt",
    "it": "Sommario",
    "es": "Sumario",
}

CONTACT_LABELS = {
    "fr": "Contact",
    "en": "Contact",
    "de": "Kontakt",
    "it": "Contatto",
    "es": "Contacto",
}

ROLE_LINES = {
    "fr": "CTO et cofondateur de SABI AGRI",
    "en": "CTO and co-founder of SABI AGRI",
    "de": "CTO und Mitgründer von SABI AGRI",
    "it": "CTO e cofondatore di SABI AGRI",
    "es": "CTO y cofundador de SABI AGRI",
}


class CalloutBox(Flowable):
    def __init__(self, paragraphs, width):
        Flowable.__init__(self)
        self.paragraphs = paragraphs
        self.box_width = width

    def wrap(self, availWidth, availHeight):
        w = min(self.box_width, availWidth)
        inner_w = w - 14 * mm
        h = 8 * mm
        for p in self.paragraphs:
            _, ph = p.wrap(inner_w, availHeight)
            h += ph + 2
        h += 4 * mm
        self.width = w
        self.height = h
        self._inner_w = inner_w
        return w, h

    def draw(self):
        self.canv.saveState()
        self.canv.setFillColor(CALLOUT_BG)
        self.canv.roundRect(0, 0, self.width, self.height, 3, fill=1, stroke=0)
        self.canv.setFillColor(CALLOUT_BORDER)
        self.canv.rect(0, 0, 2.2 * mm, self.height, fill=1, stroke=0)
        y = self.height - 5 * mm
        for p in self.paragraphs:
            _, ph = p.wrap(self._inner_w, self.height)
            y -= ph
            p.drawOn(self.canv, 5 * mm, y)
            y -= 2
        self.canv.restoreState()


def register_fonts():
    fonts = Path("/System/Library/Fonts/Supplemental")
    pdfmetrics.registerFont(TTFont("Body", str(fonts / "Arial.ttf")))
    pdfmetrics.registerFont(TTFont("Body-Bold", str(fonts / "Arial Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Body-Italic", str(fonts / "Arial Italic.ttf")))
    return "Body", "Body-Bold", "Body-Italic"


def ensure_icons():
    ASSETS.mkdir(exist_ok=True)
    # Prefer prepared PNGs already present under .pdf_assets
    for name in ("github.png", "linkedin.png"):
        if not (ASSETS / name).exists():
            raise SystemExit(f"Missing icon: {ASSETS / name}")


def inline(s: str) -> str:
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\[([^\]]+)\]\(#([^)]+)\)", r"\1", s)
    s = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<link href="\2" color="#C85830"><u>\1</u></link>',
        s,
    )
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"<i>\1</i>", s)
    return s


def build_styles(font, font_b, font_i):
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="MainTitle",
            fontName=font_b,
            fontSize=24,
            leading=28,
            textColor=BROWN,
            alignment=TA_CENTER,
            spaceAfter=8,
            spaceBefore=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubTitle",
            fontName=font,
            fontSize=11,
            leading=14,
            textColor=ORANGE,
            alignment=TA_CENTER,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="AuthorLine",
            fontName=font_i,
            fontSize=9,
            leading=12,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceAfter=8,
            spaceBefore=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="H2",
            fontName=font_b,
            fontSize=13,
            leading=16,
            textColor=BROWN,
            spaceBefore=26,
            spaceAfter=9,
            keepWithNext=True,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyJust",
            fontName=font,
            fontSize=10,
            leading=14,
            textColor=GRAY,
            alignment=TA_JUSTIFY,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyStrong",
            fontName=font,
            fontSize=10,
            leading=14,
            textColor=INK,
            alignment=TA_JUSTIFY,
            spaceAfter=7,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CalloutText",
            fontName=font,
            fontSize=10,
            leading=13.5,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=0,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CalloutLabel",
            fontName=font_b,
            fontSize=8.5,
            leading=11,
            textColor=ORANGE,
            alignment=TA_LEFT,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BulletItem",
            fontName=font,
            fontSize=10,
            leading=13.5,
            textColor=GRAY,
            leftIndent=4,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Join",
            fontName=font_b,
            fontSize=10.5,
            leading=14,
            textColor=BROWN,
            spaceBefore=8,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="AuthorName",
            fontName=font_b,
            fontSize=11.5,
            leading=14,
            textColor=BROWN,
            spaceAfter=1,
        )
    )
    styles.add(
        ParagraphStyle(
            name="AuthorRole",
            fontName=font,
            fontSize=9.5,
            leading=12,
            textColor=MUTED,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TOCItem",
            fontName=font,
            fontSize=9.5,
            leading=13,
            textColor=GRAY,
            leftIndent=2,
            spaceAfter=1,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionLabel",
            fontName=font_b,
            fontSize=9,
            leading=11,
            textColor=ORANGE,
            spaceBefore=10,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ContactLabel",
            fontName=font,
            fontSize=10,
            leading=13,
            textColor=GRAY,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ContactLink",
            fontName=font,
            fontSize=10,
            leading=13,
            textColor=ORANGE,
        )
    )
    return styles


def make_callout(lines, styles):
    paras = []
    for i, line in enumerate(lines):
        text = line.strip()
        if not text:
            continue
        # First line of affirmation-style callouts often bold label
        if i == 0 and text.startswith("**") and text.endswith("**") and len(text) < 80:
            paras.append(Paragraph(inline(re.sub(r"\*\*", "", text)), styles["CalloutLabel"]))
        elif i == 0 and any(
            k in text
            for k in (
                "Affirmation",
                "Central affirmation",
                "Zentrale Aussage",
                "Affermazione",
                "Afirmación",
            )
        ):
            paras.append(Paragraph(inline(re.sub(r"\*\*", "", text)), styles["CalloutLabel"]))
        else:
            paras.append(Paragraph(inline(text), styles["CalloutText"]))
    return CalloutBox(paras, width=17 * cm)


def contact_row(label, icon_path, link_text, url, styles):
    icon = RLImage(str(icon_path), width=12, height=12)
    label_p = Paragraph(inline(f"{label} :"), styles["ContactLabel"])
    link_p = Paragraph(
        f'<link href="{url}" color="#C85830"><u>{link_text}</u></link>',
        styles["ContactLink"],
    )
    t = Table(
        [[Paragraph("•", styles["ContactLabel"]), label_p, icon, link_p]],
        colWidths=[10, 52, 18, 300],
    )
    t.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return t


def build_pdf(lang: str, font, font_b, font_i):
    md_path = HERE / f"MANIFESTO.{lang}.md"
    pdf_path = HERE / f"MANIFESTO.{lang}.pdf"
    styles = build_styles(font, font_b, font_i)
    raw_lines = md_path.read_text(encoding="utf-8").splitlines()

    story = []
    i = 0
    in_quote = False
    quote_buf: list[str] = []
    in_list = False
    list_items: list[str] = []
    in_contact = False

    def flush_quote():
        nonlocal quote_buf
        if quote_buf:
            story.append(Spacer(1, 6))
            story.append(make_callout(quote_buf, styles))
            story.append(Spacer(1, 8))
            quote_buf = []

    def flush_list():
        nonlocal list_items, in_contact
        if not list_items:
            return
        if in_contact:
            for item in list_items:
                m = re.match(r"^(GitHub|LinkedIn)\s*:\s*\[([^\]]+)\]\(([^)]+)\)", item)
                if m:
                    label, text, url = m.group(1), m.group(2), m.group(3)
                    icon = ASSETS / ("github.png" if label == "GitHub" else "linkedin.png")
                    story.append(contact_row(label, icon, text, url, styles))
                else:
                    story.append(Paragraph(f"• {inline(item)}", styles["BulletItem"]))
            story.append(Spacer(1, 4))
            in_contact = False
        else:
            for item in list_items:
                story.append(Paragraph(f"• {inline(item)}", styles["BulletItem"]))
            story.append(Spacer(1, 4))
        list_items = []

    while i < len(raw_lines):
        stripped = raw_lines[i].strip()

        if in_quote:
            if stripped.startswith(">"):
                quote_buf.append(stripped.lstrip("> ").strip())
                i += 1
                continue
            flush_quote()
            in_quote = False

        if in_list:
            if re.match(r"^[-*]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
                list_items.append(re.sub(r"^([-*]|\d+\.)\s+", "", stripped))
                i += 1
                continue
            flush_list()
            in_list = False

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            story.append(Spacer(1, 4))
            story.append(
                HRFlowable(width="100%", thickness=0.5, color=RULE, spaceBefore=2, spaceAfter=10)
            )
            i += 1
            continue

        if stripped.startswith("# ") and not stripped.startswith("## "):
            story.append(Paragraph(inline(stripped[2:]), styles["MainTitle"]))
            i += 1
            continue

        if stripped.startswith("### "):
            story.append(Paragraph(inline(stripped[4:]), styles["SubTitle"]))
            i += 1
            continue

        if stripped.startswith("## "):
            title = re.sub(r"\s*\{#[^}]+\}", "", stripped[3:]).strip()
            if title == TOC_TITLES[lang]:
                story.append(Paragraph(inline(title), styles["H2"]))
                i += 1
                n = 1
                while (
                    i < len(raw_lines)
                    and raw_lines[i].strip()
                    and not raw_lines[i].startswith("#")
                    and raw_lines[i].strip() != "---"
                ):
                    item = raw_lines[i].strip()
                    item = re.sub(r"^\d+\.\s+", "", item)
                    item = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", item)
                    story.append(Paragraph(inline(f"{n}. {item}"), styles["TOCItem"]))
                    n += 1
                    i += 1
                story.append(Spacer(1, 4))
                continue
            story.append(Paragraph(inline(title), styles["H2"]))
            i += 1
            continue

        # Author line under title (localized prefixes)
        if re.match(
            r"^(Auteur|Author|Autor|Autore)\s*:",
            stripped,
            flags=re.IGNORECASE,
        ):
            story.append(Paragraph(inline(stripped), styles["AuthorLine"]))
            i += 1
            continue

        if stripped.startswith(">"):
            in_quote = True
            quote_buf = [stripped.lstrip("> ").strip()]
            i += 1
            continue

        if stripped.startswith("**") and re.sub(r"\*\*", "", stripped) in CONTACT_LABELS.values():
            story.append(Paragraph(inline(stripped), styles["SectionLabel"]))
            in_contact = True
            i += 1
            continue

        if re.match(r"^[-*]\s+", stripped):
            in_list = True
            list_items = [re.sub(r"^[-*]\s+", "", stripped)]
            i += 1
            continue

        # Join CTA lines
        if stripped.startswith("**") and any(
            k in stripped
            for k in (
                "Rejoindre",
                "Join the ecosystem",
                "Dem Ökosystem",
                "Unirsi",
                "Unirse",
            )
        ):
            story.append(Paragraph(inline(stripped), styles["Join"]))
            i += 1
            continue

        if stripped.startswith("**Alexandre"):
            story.append(Paragraph(inline(stripped), styles["AuthorName"]))
            i += 1
            continue

        if stripped in ROLE_LINES.values():
            story.append(Paragraph(inline(stripped), styles["AuthorRole"]))
            i += 1
            continue

        style = (
            styles["BodyStrong"]
            if "**" in stripped and len(stripped) < 180
            else styles["BodyJust"]
        )
        story.append(Paragraph(inline(stripped), style))
        i += 1

    flush_quote()
    flush_list()

    def header_footer(canvas, doc):
        canvas.saveState()
        w, h = A4
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.7)
        canvas.line(2 * cm, h - 1.4 * cm, w - 2 * cm, h - 1.4 * cm)
        canvas.setFillColor(MUTED)
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
        title=f"SRBC {HEADER_RIGHT[lang]}",
        author="Alexandre Prévault-Osmani",
    )
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return pdf_path


def main(argv: list[str]) -> int:
    ensure_icons()
    font, font_b, font_i = register_fonts()
    langs = argv[1:] or list(LANGS)
    for lang in langs:
        if lang not in LANGS:
            print(f"skip unknown lang: {lang}", file=sys.stderr)
            continue
        path = build_pdf(lang, font, font_b, font_i)
        print(f"built {path.name} ({path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
