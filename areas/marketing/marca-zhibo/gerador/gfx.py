"""Graphic elements: icons, patterns, backgrounds, palette sheet and manual figures (SVG/HTML -> PNG/PDF)."""
import os, json, subprocess, shutil
from brand import *

GFX = f'{DIST}/01_Identidade_Visual/Elementos_Graficos'
CF = f'{DIST}/01_Identidade_Visual/Cores_e_Fontes'
FIG = f'{B}/figs'
os.makedirs(FIG, exist_ok=True)
html_jobs = []   # {html, w, h, out}

def svgdoc(w, h, body, bg=None):
    r = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{r}{body}</svg>\n'

def save(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(content); return path

# ---------------- icons ----------------
ICONS = {
    'live': '<circle cx="12" cy="12" r="9"/><path d="M10 8.5v7l5.5-3.5z" fill="currentColor"/>',
    'carrinho': '<path d="M3 4h2l2.4 10.2a1 1 0 0 0 1 .8h8.9a1 1 0 0 0 1-.8L20 8H6.2"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
    'roteiro': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8.5 8h7M8.5 12h7M8.5 16h4"/>',
    'relatorio': '<path d="M4 20h16"/><rect x="6" y="12" width="3" height="8"/><rect x="11" y="8" width="3" height="12"/><rect x="16" y="4" width="3" height="16"/>',
    'host': '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0M12 17.5V21M8.5 21h7"/>',
    'estudio': '<rect x="3" y="7" width="13" height="10" rx="2"/><path d="M16 10.5l5-3v9l-5-3z"/>',
    'produto': '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M4 7.5l8 4.5 8-4.5M12 12v9"/>',
    'chat': '<path d="M4 5h16v11H9l-5 4z"/>',
    'agenda': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    'resultado': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1" fill="currentColor"/>',
    'iluminacao': '<circle cx="12" cy="10" r="7"/><circle cx="12" cy="10" r="3.5"/><path d="M12 17v4M9 21h6"/>',
    'equipe': '<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 20a5 5 0 0 1 5.5-4.8"/>',
}
def icon_svg(body, color, size=24):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" '
            f'stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" color="{color}">{body}</svg>\n')
for name, body in ICONS.items():
    for cn, col in (('Vermelho', RED), ('Tinta', INK), ('Branco', WHITE)):
        save(f'{GFX}/Icones/Editaveis/Zhibo_Icone_{name}_{cn}_v01.svg', icon_svg(body, col))

# ---------------- patterns ----------------
def waves(cx, cy, n, r0, step, sw, color, opacity=1.0, a0=-60, a1=60):
    import math
    out = []
    for i in range(n):
        r = r0 + i * step
        x1, y1 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x2, y2 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        out.append(f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" opacity="{opacity}"/>')
    return ''.join(out)
def play(x, y, s, color, opacity=1.0):  # centroid at x,y
    x1 = x - s / 3
    return f'<polygon points="{x1:.1f},{y - s * .6:.1f} {x1:.1f},{y + s * .6:.1f} {x1 + s:.1f},{y:.1f}" fill="{color}" stroke="{color}" stroke-width="{s * .2:.1f}" stroke-linejoin="round" opacity="{opacity}"/>'

pat_ondas = svgdoc(400, 400, ''.join(waves(0, 200, 6, 40, 60, 14, RED, 1, -80, 80)))
pat_play = svgdoc(200, 200, play(50, 50, 30, RED) + play(150, 150, 30, RED))
for nm, s in (('Ondas', pat_ondas), ('Play', pat_play)):
    save(f'{GFX}/Padroes/Editaveis/Zhibo_Padrao_{nm}_v01.svg', s)

# ---------------- backgrounds ----------------
BG_FORMATS = {'Apresentacao_16x9': (1920, 1080), 'Feed_4x5': (1080, 1350), 'Stories_9x16': (1080, 1920), 'Documento_A4': (2480, 3508)}
BG_TONES = {  # front -> tone -> (bg, wave colour, wave opacity, play colour)
    'Institucional': {'Claro': (PAPER, RED, .14, RED), 'Escuro': (INK, RED, .55, RED)},
    'Agencia': {'Claro': (PAPER, GOLD, .55, INK), 'Escuro': (INK, GOLD, .65, GOLD)},
    'Shop': {'Claro': (PAPER, RED, .18, RED), 'Escuro': (RED, DEEP, .9, PAPER)},
}
BG_POS = {'Apresentacao_16x9': (.70, .50, 1.0), 'Feed_4x5': (.42, .74, .9), 'Stories_9x16': (.40, .78, .9), 'Documento_A4': (.80, .07, .32)}
def background(w, h, bg, wave, op, pl, fmt):
    fx, fy, sc = BG_POS[fmt]; u = min(w, h) * sc
    px, py = w * fx, h * fy                       # play centroid; waves open to the right, like the symbol
    body = play(px, py, u * .16, pl, 1)
    body += waves(px - u * .02, py, 6, u * .2, u * .14, u * .045, wave, op, -58, 58)
    return svgdoc(w, h, body, bg)
bg_files = []
for front, tones in BG_TONES.items():
    for tone, spec in tones.items():
        for fmt, (w, h) in BG_FORMATS.items():
            svg = background(w, h, *spec, fmt)
            p = save(f'{GFX}/Fundos/Editaveis/{FRONTS[front]["file"]}_Fundo_{fmt}_{tone}_v01.svg', svg)
            bg_files.append(p)

# ---------------- figures for the manual (HTML -> PNG) ----------------
def fig(name, w, h, inner, bg=WHITE):
    html = (f'<html><head><style>@font-face{{font-family:Inter;src:url(file://{B}/fonts/Inter-600.ttf)}}'
            f'body{{margin:0;width:{w}px;height:{h}px;background:{bg};font-family:Inter;overflow:hidden;position:relative}}</style></head><body>{inner}</body></html>')
    html_jobs.append(dict(html=html, w=w, h=h, out=f'{FIG}/{name}.png'))

L = lambda front, lay='Horizontal', cw='Colorida': 'file://' + logo(front, lay, cw, 'svg')
# protection area: x = height of the "z"
import re as _re
_m = json.load(open(f'{B}/out/manifest.json')); _X = _m['unitX']
_it = [i for i in _m['items'] if i['front']=='Agencia' and i['layout']=='Horizontal' and i['colorway']=='Colorida'][0]
_LH = min(200, 1400/(_it['w']/_it['h'] + 2*_X/_it['h'])); _LW = _LH*_it['w']/_it['h']; _x = _LH*_X/_it['h']; _ox = (1600-_LW-2*_x)/2; _oy = 110
_xb = lambda l,t: f'<div style="position:absolute;left:{l:.1f}px;top:{t:.1f}px;width:{_x:.1f}px;height:{_x:.1f}px;background:{GOLD};display:flex;align-items:center;justify-content:center;font:700 30px Inter">x</div>'
fig('protecao', 1600, 700, f'''
<div style="position:absolute;left:{_ox:.1f}px;top:{_oy}px;width:{_LW+2*_x:.1f}px;height:{_LH+2*_x:.1f}px;border:3px dashed {RED};box-sizing:border-box"></div>
<img src="{L('Agencia')}" style="position:absolute;left:{_ox+_x:.1f}px;top:{_oy+_x:.1f}px;width:{_LW:.1f}px;height:{_LH}px">
{_xb(_ox, _oy+_x)}{_xb(_ox+_x+_LW, _oy+_x+_LH-_x)}{_xb(_ox+_x+_LW/2-_x/2, _oy)}{_xb(_ox+_x+_LW/2-_x/2, _oy+_x+_LH)}
<div style="position:absolute;left:{_ox:.1f}px;top:{_oy+_LH+2*_x+40:.1f}px;font:600 26px Inter;color:{GREY}">x = altura do “z” de zhibo. Nenhum texto, borda ou imagem entra na área tracejada.</div>''')
# minimum sizes
fig('tamanho_minimo', 1600, 520, f'''
<div style="position:absolute;left:80px;top:80px;display:flex;gap:120px;align-items:flex-end">
 <div><img src="{L('Shop')}" style="height:56px"><div style="font:600 24px Inter;margin-top:24px;color:{GREY}">Horizontal: 30 mm / 160 px de largura</div></div>
 <div><img src="{L('Shop','Vertical')}" style="height:110px"><div style="font:600 24px Inter;margin-top:24px;color:{GREY}">Vertical: 18 mm / 90 px</div></div>
 <div><img src="file://{LOGO}/Zhibo_Simbolo/Editaveis/Zhibo_Simbolo_Vermelho_v01.svg" style="height:40px"><div style="font:600 24px Inter;margin-top:24px;color:{GREY}">Símbolo: 6 mm / 24 px</div></div>
</div>''')
# wrong uses
wrong = [
    ('Não distorcer', f'<img src="{L("Institucional")}" style="width:300px;height:60px;transform:scaleY(1.6)">'),
    ('Não trocar as cores', f'<img src="{L("Institucional")}" style="width:300px;filter:hue-rotate(140deg)">'),
    ('Não girar', f'<img src="{L("Institucional")}" style="width:300px;transform:rotate(-14deg)">'),
    ('Não aplicar sombra ou efeito', f'<img src="{L("Institucional")}" style="width:300px;filter:drop-shadow(8px 8px 4px rgba(0,0,0,.6))">'),
    ('Não usar em fundo sem contraste', f'<div style="background:{RED};padding:30px"><img src="{L("Institucional")}" style="width:300px"></div>'),
    ('Não mudar a fonte do nome', f'<div style="font:800 64px Georgia;color:{INK}">zhibo <span style="font-size:30px">agência</span></div>'),
]
cells = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:22px"><div style="height:210px;width:440px;display:flex;align-items:center;justify-content:center;background:#F6F1EA;position:relative">{c}<svg style="position:absolute;right:12px;top:12px" width="44" height="44" viewBox="0 0 24 24" fill="none" stroke="{RED}" stroke-width="3"><circle cx="12" cy="12" r="10"/><path d="M5 5l14 14"/></svg></div><div style="font:600 26px Inter">{t}</div></div>' for t, c in wrong)
fig('usos_incorretos', 1600, 760, f'<div style="position:absolute;inset:40px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px 30px">{cells}</div>')
# co-branding
def cobrand(name, front, partner_label):
    fig(name, 1600, 520, f'''
<div style="position:absolute;left:160px;top:150px;height:200px;display:flex;align-items:center;gap:0">
 <img src="{L(front)}" style="height:110px">
 <div style="width:3px;height:170px;background:{INK};margin:0 80px"></div>
 <div style="width:420px;height:150px;border:3px dashed {GREY};display:flex;align-items:center;justify-content:center;font:600 30px Inter;color:{GREY}">{partner_label}</div>
</div>
<div style="position:absolute;left:160px;top:420px;font:600 24px Inter;color:{GREY}">Mesma altura visual · separador de 1 x · espaço de 2 x de cada lado · Zhibo sempre à esquerda (ou em cima).</div>''')
cobrand('coassinatura_agencia', 'Agencia', 'LOGO DA MARCA CLIENTE')
cobrand('coassinatura_shop', 'Shop', 'LOGO DA MARCA CLIENTE')
cobrand('coassinatura_institucional', 'Institucional', 'LOGO DO PARCEIRO')
# fronts together
fig('frentes_juntas', 1600, 520, f'''
<div style="position:absolute;left:0;right:0;top:110px;display:flex;justify-content:center;align-items:center;gap:90px">
 <img src="{L('Agencia')}" style="height:92px"><div style="width:3px;height:140px;background:{INK}"></div><img src="{L('Shop')}" style="height:92px">
</div>
<div style="position:absolute;left:0;right:0;top:330px;text-align:center;font:600 26px Inter;color:{GREY}">Lado a lado, mesma altura, separadas por um traço. Em material institucional, use a assinatura Zhibo<br>e cite as frentes no texto.</div>''')
# palette sheet (also delivered in Cores_e_Fontes)
sw = ''.join(f'''<div style="display:flex;flex-direction:column;gap:12px"><div style="height:260px;background:{h};border:{'2px solid #141010' if h in (WHITE, PAPER) else 'none'};border-radius:18px"></div>
<div style="font:700 24px Inter">{n}</div><div style="font:600 18px Inter;color:{GREY};line-height:1.5">HEX {h}<br>RGB {', '.join(map(str, rgb(h)))}<br>CMYK {' '.join(map(str, cmyk(h)))}</div></div>''' for n, h, _, _ in PALETTE)
fig('paleta', 1920, 760, f'<div style="position:absolute;inset:60px;display:grid;grid-template-columns:repeat(8,1fr);gap:24px">{sw}</div><div style="position:absolute;left:60px;bottom:40px;font:600 20px Inter;color:{GREY}">CMYK de referência, convertido do RGB. Antes de imprimir, peça prova de cor à gráfica.</div>', PAPER)
# icon sheet
ic = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:14px"><img src="file://{GFX}/Icones/Editaveis/Zhibo_Icone_{n}_Tinta_v01.svg" style="width:90px"><div style="font:600 20px Inter">{n}</div></div>' for n in ICONS)
fig('icones', 1920, 520, f'<div style="position:absolute;inset:70px;display:grid;grid-template-columns:repeat(6,1fr);gap:50px 20px">{ic}</div>', PAPER)

json.dump(html_jobs, open(f'{B}/jobs_html.json', 'w'))
# svg->png/pdf jobs for icons/patterns/backgrounds
jobs = []
for root, _, files in os.walk(GFX):
    for f in files:
        if f.endswith('.svg') and '/Editaveis' in root:
            src = os.path.join(root, f); outd = root.replace('/Editaveis', '/Finais_Digitais')
            w = 512 if '/Icones/' in root else (1200 if '/Padroes/' in root else None)
            j = dict(svg=src, png=os.path.join(outd, f[:-4] + '.png'))
            if w: j['pngWidth'] = w
            else:
                import re; j['pngWidth'] = int(re.search(r'viewBox="0 0 (\d+)', open(src).read()).group(1))
            jobs.append(j)
json.dump(jobs, open(f'{B}/jobs_gfx.json', 'w'))
print('icons', len(ICONS), 'backgrounds', len(bg_files), 'figs', len(html_jobs), 'svgjobs', len(jobs))
