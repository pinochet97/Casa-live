"""Slide templates shared by the manual, media kits, proposals, reports and portfolio (16:9)."""
from brand import *

W, H = 13.333, 7.5
M = 0.7  # outer margin (in)

def bg_image(front, tone, fmt='Apresentacao_16x9'):
    return f'{DIST}/01_Identidade_Visual/Elementos_Graficos/Fundos/Finais_Digitais/{FRONTS[front]["file"]}_Fundo_{fmt}_{tone}_v01.png'

def cover(p, front, title, subtitle='', kicker='', tone='Escuro'):
    bgc = {'Institucional': INK, 'Agencia': INK, 'Shop': RED}[front] if tone == 'Escuro' else PAPER
    s = slide(p, bgc)
    image(s, bg_image(front, tone), 0, 0, W, H)
    dark = is_dark(bgc) or bgc == RED
    image_fit(s, logo(front, 'Horizontal', 'Branca' if bgc == RED else ('Negativa' if dark else 'Colorida')), M, M, 4.2, 0.75)
    fg = PAPER if dark else INK
    if kicker: text(s, M, 3.0, 7.5, 0.4, kicker.upper(), size=12, color=GOLD if bgc == INK else fg, bold=True, font=BODY)
    text(s, M, 3.4, 7.6, 2.0, title, size=36, color=fg, bold=True, font=HEAD, line=1.0)
    if subtitle: text(s, M, 5.55, 7.2, 1.0, subtitle, size=15, color=fg, font=BODY)
    return s

def section(p, front, number, title, tone='Escuro'):
    bgc = {'Institucional': INK, 'Agencia': INK, 'Shop': RED}[front]
    s = slide(p, bgc)
    image(s, bg_image(front, 'Escuro'), 0, 0, W, H)
    text(s, M, 2.6, 6, 0.6, number, size=16, color=GOLD if bgc == INK else PAPER, bold=True)
    text(s, M, 3.1, 8, 1.6, title, size=40, color=PAPER, bold=True, font=HEAD, line=1.0)
    return s

def page(p, front, kicker, title, num=None, bg=PAPER, footer=True):
    s = slide(p, bg)
    dark = is_dark(bg)
    fg = PAPER if dark else INK
    acc = FRONTS[front]['accent'] if FRONTS[front]['accent'] != INK else RED
    if front == 'Agencia' and not dark: acc = '#B07D00'   # darker gold for text on light bg (contrast)
    text(s, M, 0.55, 9, 0.3, kicker.upper(), size=11, color=acc if not dark else GOLD, bold=True)
    text(s, M, 0.85, 11.9, 0.9, title, size=26, color=fg, bold=True, font=HEAD, line=1.0)
    if footer:
        image_fit(s, logo(front, 'Horizontal', 'Negativa' if dark else 'Colorida'), M, H - 0.55, 1.6, 0.26, valign='middle')
        if num is not None: text(s, W - M - 1, H - 0.55, 1, 0.26, f'{num:02d}', size=10, color=GREY if not dark else '#B9ADA4', align='right', anchor='middle')
    return s

def bullets(s, x, y, w, h, items, size=14, color=INK, gap=8, mark=RED):
    paras = [[('■  ', dict(color=mark, size=size * .7)), (it, {})] if isinstance(it, str) else it for it in items]
    return text(s, x, y, w, h, paras, size=size, color=color, spacing=gap)

def card(s, x, y, w, h, title, body, fill=WHITE, title_color=INK, body_color=INK, icon=None, line=None, num=None):
    box(s, x, y, w, h, fill=fill, line=line, lw=1.25, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
    ty = y + 0.3
    if icon:
        image(s, icon, x + 0.3, y + 0.3, 0.45, 0.45); ty = y + 0.95
    if num:
        text(s, x + 0.3, y + 0.25, 1, 0.5, num, size=22, color=RED, bold=True, font=HEAD); ty = y + 0.85
    text(s, x + 0.3, ty, w - 0.6, 0.5, title, size=14 if w > 2.4 else 11.5, color=title_color, bold=True, font=BODY)
    text(s, x + 0.3, ty + 0.45, w - 0.6, h - (ty - y) - 0.55, body, size=11.5, color=body_color, line=1.2)

def icon(name, color='Vermelho'):
    return f'{DIST}/01_Identidade_Visual/Elementos_Graficos/Icones/Finais_Digitais/Zhibo_Icone_{name}_{color}_v01.png'

def contact_block(s, x, y, w, front, dark=False):
    fg = PAPER if dark else INK
    rows = [('Comercial', 'Felipe Percebão'), ('WhatsApp', f'{TBD} (número comercial)'), ('E-mail', f'{TBD}'),
            ('Instagram / TikTok', f'@{TBD}'), ('Site', f'{TBD} (zhibo.com.br, a registrar)')]
    for i, (k, v) in enumerate(rows):
        text(s, x, y + i * 0.52, 2.3, 0.4, k, size=12, color=GOLD if dark else GREY, bold=True)
        text(s, x + 2.4, y + i * 0.52, w - 2.4, 0.4, v, size=14, color=fg)
