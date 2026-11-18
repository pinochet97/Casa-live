"""Zhibo brand constants + python-pptx helpers shared by every generated document."""
import os, subprocess, shutil
from pptx import Presentation
from pptx.util import Emu, Pt, Inches
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

B = os.path.dirname(os.path.abspath(__file__))
DIST = f'{B}/dist/Zhibo_Marca_e_Comercial'
LOGO = f'{DIST}/01_Identidade_Visual/Logos'
AVATAR = f'{DIST}/01_Identidade_Visual/Avatares/Finais_Digitais'

# ---------------- colours ----------------
def cmyk(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5))
    k = 1 - max(r, g, b)
    if k >= 1: return (0, 0, 0, 100)
    c, m, y = ((1 - x - k) / (1 - k) for x in (r, g, b))
    return tuple(round(v * 100) for v in (c, m, y, k))

def rgb(hexc): return tuple(int(hexc[i:i + 2], 16) for i in (1, 3, 5))

PALETTE = [  # name, hex, role, group
    ('Vermelho Live', '#E5262A', 'Cor principal. Símbolo, destaques, chamadas. Cor da frente Zhibo Shop.', 'Principal'),
    ('Tinta', '#141010', 'Textos e fundos escuros. Cor da frente Zhibo institucional.', 'Principal'),
    ('Papel', '#FFF7EC', 'Fundo claro padrão.', 'Principal'),
    ('Ouro Oferta', '#FFC42E', 'Preço, oferta, selo. Cor da frente Zhibo Agência.', 'Apoio'),
    ('Vermelho Fundo', '#9E1418', 'Profundidade, fundos e sombras sobre o vermelho.', 'Apoio'),
    ('Cinza Quente', '#5C504A', 'Textos secundários, legendas.', 'Apoio'),
    ('Areia', '#EDE2D3', 'Caixas, áreas de foto, divisórias em fundo claro.', 'Apoio'),
    ('Branco', '#FFFFFF', 'Fundos de documentos e versão branca do logo.', 'Apoio'),
]
RED, INK, PAPER, GOLD, DEEP, GREY, SAND, WHITE = '#E5262A', '#141010', '#FFF7EC', '#FFC42E', '#9E1418', '#5C504A', '#EDE2D3', '#FFFFFF'

FRONTS = {
    'Institucional': dict(name='Zhibo', file='Zhibo_Institucional', accent=INK, on_accent=PAPER, avatar_bg=INK),
    'Agencia': dict(name='Zhibo Agência', file='Zhibo_Agencia', accent=GOLD, on_accent=INK, avatar_bg=GOLD),
    'Shop': dict(name='Zhibo Shop', file='Zhibo_Shop', accent=RED, on_accent=PAPER, avatar_bg=RED),
}
HEAD, BODY = 'Unbounded', 'Inter'
TBD = '[A PREENCHER]'

def logo(front, layout='Horizontal', colorway='Colorida', fmt='png'):
    f = FRONTS[front]['file']
    sub = 'Finais_Digitais' if fmt == 'png' else 'Editaveis'
    return f'{LOGO}/{f}/{sub}/{f}_Logo_{layout}_{colorway}_v01.{fmt}'

def symbol_png(color='Vermelho'):
    return f'{LOGO}/Zhibo_Simbolo/Finais_Digitais/Zhibo_Simbolo_{color}_v01.png'

def is_dark(hexc):
    r, g, b = rgb(hexc); return (0.299 * r + 0.587 * g + 0.114 * b) < 140

# ---------------- pptx helpers ----------------
SIZES = {  # inches
    '16:9': (13.333, 7.5), 'A4': (8.268, 11.693), 'feed': (11.25, 14.0625), 'story': (11.25, 20.0), 'square': (11.25, 11.25),
}

def new_deck(size='16:9'):
    p = Presentation(); w, h = SIZES[size]
    p.slide_width, p.slide_height = Inches(w), Inches(h)
    return p

def slide(p, bg=PAPER):
    s = p.slides.add_slide(p.slide_layouts[6])
    fill = s.background.fill; fill.solid(); fill.fore_color.rgb = RGBColor.from_string(bg[1:])
    return s

def _col(hexc): return RGBColor.from_string(hexc[1:])

def box(s, x, y, w, h, fill=None, line=None, lw=1.0, shape=MSO_SHAPE.RECTANGLE, radius=None, dash=False):
    sh = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if fill: sh.fill.solid(); sh.fill.fore_color.rgb = _col(fill)
    else: sh.fill.background()
    if line: sh.line.color.rgb = _col(line); sh.line.width = Pt(lw)
    else: sh.line.fill.background()
    if dash and line:
        ln = sh.line._get_or_add_ln(); d = etree.SubElement(ln, qn('a:prstDash')); d.set('val', 'dash')
    if radius is not None and shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = radius
    sh.shadow.inherit = False
    tf = sh.text_frame; tf.text = ''
    return sh

def text(s, x, y, w, h, content, size=14, color=INK, font=BODY, bold=False, align='left', anchor='top',
         spacing=None, line=1.15, fill=None, italic=False, link=None):
    """content: str or list of runs/paragraphs. A paragraph = str or list of (text, overrides) tuples."""
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    if fill: tb.fill.solid(); tb.fill.fore_color.rgb = _col(fill)
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = {'top': MSO_ANCHOR.TOP, 'middle': MSO_ANCHOR.MIDDLE, 'bottom': MSO_ANCHOR.BOTTOM}[anchor]
    paras = content if isinstance(content, list) else [content]
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {'left': PP_ALIGN.LEFT, 'center': PP_ALIGN.CENTER, 'right': PP_ALIGN.RIGHT}[align]
        p.line_spacing = line
        if spacing is not None: p.space_after = Pt(spacing)
        runs = para if isinstance(para, list) else [(para, {})]
        for rt, ov in runs:
            r = p.add_run(); r.text = rt
            f = r.font; f.name = ov.get('font', font); f.size = Pt(ov.get('size', size)); f.bold = ov.get('bold', bold)
            f.italic = ov.get('italic', italic); f.color.rgb = _col(ov.get('color', color))
            if ov.get('link', link): r.hyperlink.address = ov.get('link', link)
    return tb

def image(s, path, x, y, w=None, h=None):
    kw = {}
    if w: kw['width'] = Inches(w)
    if h: kw['height'] = Inches(h)
    return s.shapes.add_picture(path, Inches(x), Inches(y), **kw)

def image_fit(s, path, x, y, w, h, align='left', valign='middle'):
    """Place an image inside a box keeping its ratio."""
    from PIL import Image
    iw, ih = Image.open(path).size; k = min(w / iw, h / ih); W, H = iw * k, ih * k
    X = x + {'left': 0, 'center': (w - W) / 2, 'right': w - W}[align]
    Y = y + {'top': 0, 'middle': (h - H) / 2, 'bottom': h - H}[valign]
    return s.shapes.add_picture(path, Inches(X), Inches(Y), Inches(W), Inches(H))

def photo(s, x, y, w, h, label, dark=False):
    """Honest placeholder for a real photo that still has to be supplied."""
    b = box(s, x, y, w, h, fill='#2A2220' if dark else SAND, line=GREY, lw=1.25, dash=True)
    text(s, x + 0.15, y, w - 0.3, h, [[('FOTO REAL', dict(bold=True, size=11))], label], size=11,
         color='#B9ADA4' if dark else GREY, align='center', anchor='middle')
    return b

def pill(s, x, y, label, fill=INK, color=PAPER, size=11, h=0.36, pad=0.18, font=BODY, bold=True):
    w = pad * 2 + len(label) * size * 0.0105
    box(s, x, y, w, h, fill=fill, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
    text(s, x, y, w, h, label, size=size, color=color, bold=bold, align='center', anchor='middle', font=font)
    return w

def table(s, x, y, w, rows, col_w=None, header_fill=INK, header_color=PAPER, size=10, row_h=0.36, zebra=SAND, body_fill=WHITE):
    nr, nc = len(rows), len(rows[0])
    gt = s.shapes.add_table(nr, nc, Inches(x), Inches(y), Inches(w), Inches(row_h * nr)).table
    if col_w:
        for i, cw in enumerate(col_w): gt.columns[i].width = Inches(cw)
    for ri, row in enumerate(rows):
        gt.rows[ri].height = Inches(row_h)
        for ci, val in enumerate(row):
            c = gt.cell(ri, ci); c.text = ''
            c.margin_left = c.margin_right = Inches(0.08); c.margin_top = c.margin_bottom = Inches(0.04)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.fill.solid(); c.fill.fore_color.rgb = _col(header_fill if ri == 0 else (zebra if ri % 2 == 0 else body_fill))
            p = c.text_frame.paragraphs[0]; r = p.add_run(); r.text = str(val)
            r.font.name = BODY; r.font.size = Pt(size); r.font.bold = ri == 0
            r.font.color.rgb = _col(header_color if ri == 0 else INK)
    return gt

def notes(s, txt): s.notes_slide.notes_text_frame.text = txt

# ---------------- export ----------------
def export(p, out_pptx, pdf_dir=None, png_dir=None, png_width=1600):
    os.makedirs(os.path.dirname(out_pptx), exist_ok=True); p.save(out_pptx)
    res = {'pptx': out_pptx}
    if pdf_dir:
        os.makedirs(pdf_dir, exist_ok=True)
        subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', pdf_dir, out_pptx], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        res['pdf'] = os.path.join(pdf_dir, os.path.basename(out_pptx)[:-5] + '.pdf')
        if png_dir:
            os.makedirs(png_dir, exist_ok=True)
            stem = os.path.join(png_dir, os.path.basename(out_pptx)[:-5])
            subprocess.run(['pdftoppm', '-png', '-scale-to-x', str(png_width), '-scale-to-y', '-1', res['pdf'], stem], check=True)
    return res
