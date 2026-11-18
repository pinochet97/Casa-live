"""03_Aplicacoes: 05 destaques, 06 Cartões e assinaturas, 07 Folhetos e banners, 08 Espaço físico, 09 coassinatura.
Print pieces are SVG (editable, live text in Unbounded/Inter) -> vector PDF at final size + bleed."""
from deck import *
import json, re, shutil
from docx import Document
from docx.shared import Pt as DPt, Cm, RGBColor as DRGB
AP = f'{DIST}/03_Aplicacoes_da_Marca'
F = lambda fr: FRONTS[fr]['file']
SPECS = []   # (piece, front, final size, bleed, safe, notes) -> Leia-me
svg_jobs, html_jobs = [], []

def logo_svg(front, layout='Horizontal', cw='Colorida', x=0, y=0, w=None, h=None):
    src = open(logo(front, layout, cw, 'svg')).read()
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', src); lw, lh = float(vb[1]), float(vb[2])
    if w and not h: h = w * lh / lw
    if h and not w: w = h * lw / lh
    inner = re.sub(r'<\?xml[^>]*>\s*', '', src)
    inner = re.sub(r'<svg [^>]*>', f'<svg x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" viewBox="0 0 {lw} {lh}">', inner, count=1)
    return inner, w, h
def sym_svg(color, x, y, w):
    name = {RED: 'Vermelho', INK: 'Preto', WHITE: 'Branco', PAPER: 'Creme'}[color]
    src = open(f'{LOGO}/Zhibo_Simbolo/Editaveis/Zhibo_Simbolo_{name}_v01.svg').read()
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', src); lw, lh = float(vb[1]), float(vb[2]); h = w * lh / lw
    inner = re.sub(r'<\?xml[^>]*>\s*', '', src)
    return re.sub(r'<svg [^>]*>', f'<svg x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" viewBox="0 0 {lw} {lh}">', inner, count=1)
def T(x, y, s, size, color=INK, font='Inter', weight=400, anchor='start', ls=0):
    return f'<text x="{x:.2f}" y="{y:.2f}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" letter-spacing="{ls}">{s}</text>'
def R(x, y, w, h, fill='none', stroke=None, sw=0.3, rx=0, dash=None):
    st = f' stroke="{stroke}" stroke-width="{sw}"' + (f' stroke-dasharray="{dash}"' if dash else '') if stroke else ''
    return f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{fill}"{st}/>'
def waves_svg(cx, cy, n, r0, step, sw, color, op, a0=-58, a1=58):
    import math; o = ''
    for i in range(n):
        r = r0 + i * step; x1, y1 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)); x2, y2 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        o += f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" opacity="{op}"/>'
    return o
def deco(cx, cy, u, playcol, wavecol, op):
    x1 = cx - u * .16 / 3; sz = u * .16
    pl = f'<polygon points="{x1:.1f},{cy - sz * .6:.1f} {x1:.1f},{cy + sz * .6:.1f} {x1 + sz:.1f},{cy:.1f}" fill="{playcol}" stroke="{playcol}" stroke-width="{sz * .2:.1f}" stroke-linejoin="round"/>'
    return pl + waves_svg(cx - u * .02, cy, 5, u * .2, u * .14, u * .045, wavecol, op)
def doc(w, h, body, title):  # mm units
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}mm" height="{h}mm"><title>{title}</title>{body}</svg>\n'
def print_piece(folder, name, pages, w, h, bleed, safe, front, notes, preview_w=1400):
    """pages: list of (suffix, svg_body) drawn on a (w+2b) x (h+2b) mm canvas, origin at bleed corner."""
    W2, H2 = w + 2 * bleed, h + 2 * bleed
    os.makedirs(f'{folder}/Editaveis', exist_ok=True); os.makedirs(f'{folder}/Impressao', exist_ok=True); os.makedirs(f'{folder}/Finais_Digitais', exist_ok=True)
    files = []
    for suf, body in pages:
        fn = f'{name}_{suf}_v01' if suf else f'{name}_v01'
        guide = (f'<g id="GUIAS_apagar_antes_de_imprimir" display="none">{R(bleed, bleed, w, h, stroke="#00AEEF", sw=0.3)}'
                 f'{R(bleed + safe, bleed + safe, w - 2 * safe, h - 2 * safe, stroke="#FF00FF", sw=0.3, dash="2 2")}</g>')
        open(f'{folder}/Editaveis/{fn}.svg', 'w').write(doc(W2, H2, body + guide, fn))
        svg_jobs.append(dict(svg=f'{folder}/Editaveis/{fn}.svg', pdf=f'{folder}/Impressao/{fn}.pdf', pdfWidthMm=W2,
                             png=f'{folder}/Finais_Digitais/{fn}_preview.png', pngWidth=preview_w))
        files.append(fn)
    SPECS.append(dict(piece=name, front=FRONTS[front]['name'] if front else 'Zhibo', size=f'{w} × {h} mm', bleed=f'{bleed} mm', safe=f'{safe} mm', notes=notes, files=files))

# ------------------------------------------------------------------ 06 cartões impressos 90x50
for fr in ('Institucional', 'Agencia', 'Shop'):
    b, w, h, sf = 3, 90, 50, 5
    acc = {'Institucional': INK, 'Agencia': GOLD, 'Shop': RED}[fr]
    lg_cw = {'Institucional': 'Negativa', 'Agencia': 'Preta', 'Shop': 'Branca'}[fr]
    lg, lw_, lh_ = logo_svg(fr, 'Vertical', lg_cw, 0, 0, None, 22)
    lg, lw_, lh_ = logo_svg(fr, 'Vertical', lg_cw, b + w / 2 - (22 * 0 + 0), 0, None, 22)
    lw_ = float(re.search(r'width="([\d.]+)"', lg)[1]); lg, _, _ = logo_svg(fr, 'Vertical', lg_cw, b + (w - lw_) / 2, b + (h - 22) / 2, None, 22)
    frente = R(0, 0, w + 2 * b, h + 2 * b, acc) + lg
    lg2, _, _ = logo_svg(fr, 'Horizontal', 'Colorida', b + sf, b + sf, None, 6)
    verso = (R(0, 0, w + 2 * b, h + 2 * b, PAPER) + lg2 + T(b + sf, b + 22, '[Nome Sobrenome]', 4.2, INK, 'Unbounded', 700)
             + T(b + sf, b + 27, '[Cargo]', 3, GREY, 'Inter', 600)
             + T(b + sf, b + 35, 'WhatsApp [+55 00 00000-0000]', 2.8) + T(b + sf, b + 39.2, '[nome]@[dominio]', 2.8) + T(b + sf, b + 43.4, '@[perfil] · [site]', 2.8)
             + R(b + w - sf - 14, b + h - sf - 14, 14, 14, 'none', GREY, .3, 0, '1 1') + T(b + w - sf - 7, b + h - sf - 6.2, 'QR', 2.4, GREY, 'Inter', 600, 'middle'))
    print_piece(f'{AP}/06_Cartoes_e_Assinaturas/{F(fr)}/Cartao_Impresso', f'{F(fr)}_Cartao_Impresso_90x50', [('Frente', frente), ('Verso', verso)], w, h, b, sf, fr,
                'Papel couché 300 g, 4x4 cores, laminação fosca (sugestão). QR só com destino verificado.', 1000)

# ------------------------------------------------------------------ 07 folhetos A5 e banners 80x200
def folheto(fr):
    b, w, h, sf = 3, 148, 210, 6
    dark = INK if fr == 'Agencia' else RED
    lg, _, _ = logo_svg(fr, 'Horizontal', 'Negativa' if dark == INK else 'Branca', b + sf + 4, b + sf + 6, None, 11)
    head = {'Agencia': ['Planejamento e resultado', 'para suas lives de venda'], 'Shop': ['Sua marca vendendo', 'ao vivo no TikTok Shop']}[fr]
    svc = {'Agencia': ['Planejamento e calendário', 'Estudo de produto e fichas', 'Roteiros e plano de ofertas', 'Relatórios D+1, semanal e mensal'],
           'Shop': ['Lives de 2 h na conta da marca', 'Host e moderador em cada live', '2 a 3 cenários personalizáveis', 'Relatório no dia seguinte']}[fr]
    frente = (R(0, 0, w + 2 * b, h + 2 * b, dark) + deco(b + 118, b + 172, 70, GOLD if dark == INK else PAPER, GOLD if dark == INK else DEEP, .7 if dark == INK else .9) + lg
              + T(b + sf + 4, b + 50, head[0], 8, PAPER, 'Unbounded', 700) + T(b + sf + 4, b + 61, head[1], 8, PAPER, 'Unbounded', 700)
              + T(b + sf + 4, b + 76, 'Teste de 30 dias só por comissão.', 5, GOLD if dark == INK else PAPER, 'Inter', 600)
              + R(b + sf + 4, b + 88, 88, 62, '#2A2220' if dark == INK else DEEP, '#B9ADA4', .4, 2, '2 2') + T(b + sf + 48, b + 120, 'FOTO REAL DA CASA OU DE UMA LIVE', 3.2, '#E9DED3', 'Inter', 600, 'middle')
              + T(b + sf + 4, b + h - sf - 12, '[site ou @perfil]', 4.5, PAPER, 'Inter', 600))
    verso = R(0, 0, w + 2 * b, h + 2 * b, PAPER) + T(b + sf + 4, b + sf + 16, 'Serviços', 9, INK, 'Unbounded', 700)
    for i, s_ in enumerate(svc): verso += R(b + sf + 4, b + 34 + i * 11, 3, 3, RED) + T(b + sf + 10, b + 37 + i * 11, s_, 4.6)
    verso += T(b + sf + 4, b + 96, 'Como funciona', 9, INK, 'Unbounded', 700)
    for i, s_ in enumerate(['1. Conversa e escolha dos produtos', '2. Onboarding: acessos, amostras, fichas', '3. Planejamento: agenda, roteiro, ofertas', '4. Live com host e moderador', '5. Relatório no dia seguinte']):
        verso += T(b + sf + 4, b + 110 + i * 8.5, s_, 4.4)
    verso += (R(0, b + 160, w + 2 * b, h + 2 * b - (b + 160), INK) + T(b + sf + 4, b + 174, 'Fale com o comercial', 5, GOLD, 'Inter', 700)
              + T(b + sf + 4, b + 182, 'Felipe Percebão · WhatsApp [A PREENCHER]', 4.4, PAPER) + T(b + sf + 4, b + 189, '[e-mail] · @[perfil]', 4.4, PAPER)
              + R(b + w - sf - 30, b + 166, 28, 28, PAPER, GREY, .4, 1, '1.5 1.5') + T(b + w - sf - 16, b + 181, 'QR CODE', 3.2, GREY, 'Inter', 700, 'middle')
              + T(b + w - sf - 16, b + 186, '[destino verificado]', 2.4, GREY, 'Inter', 400, 'middle'))
    print_piece(f'{AP}/07_Folhetos_e_Banners/{F(fr)}/Folheto_A5', f'{F(fr)}_Folheto_A5', [('Frente', frente), ('Verso', verso)], w, h, b, sf, fr,
                'Couché 150 g, 4x4 cores (sugestão). Gerar o QR só depois de confirmar o destino.')
for fr in ('Agencia', 'Shop'): folheto(fr)

def banner(fr):
    b, w, h, sf = 10, 800, 2000, 40
    bgc = {'Institucional': INK, 'Agencia': INK, 'Shop': RED}[fr]
    lg, _, _ = logo_svg(fr, 'Vertical', 'Negativa' if bgc == INK else 'Branca', b + 150, b + 120, 500, None)
    head = {'Agencia': ['Planejamento', 'que vende', 'ao vivo'], 'Shop': ['Sua marca', 'vendendo', 'ao vivo'], 'Institucional': ['Agência e', 'casa de lives', 'de venda']}[fr]
    body = R(0, 0, w + 2 * b, h + 2 * b, bgc) + deco(b + 560, b + (1500 if fr == 'Institucional' else 1350), 440, RED if bgc == INK else PAPER, GOLD if bgc == INK else DEEP, .7 if bgc == INK else .9) + lg
    for i, l in enumerate(head): body += T(b + sf + 40, b + 760 + i * 95, l, 80, PAPER, 'Unbounded', 700)
    sub = {'Agencia': 'Planejamento · fichas · roteiro · ofertas · relatórios', 'Shop': 'Estúdio · hosts · moderação · relatório no dia seguinte',
           'Institucional': 'Zhibo Agência planeja. Zhibo Shop transmite.'}[fr]
    body += T(b + sf + 40, b + 1080, sub, 26, GOLD if bgc == INK else PAPER, 'Inter', 600)
    if fr == 'Institucional':
        a, _, _ = logo_svg('Agencia', 'Horizontal', 'Negativa', b + sf + 40, b + 1150, 560, None); s_, _, _ = logo_svg('Shop', 'Horizontal', 'Negativa', b + sf + 40, b + 1270, 560, None)
        body += a + s_
    body += (R(b + sf + 40, b + h - sf - 300, 720, 260, PAPER, None, 0, 12) + T(b + sf + 80, b + h - sf - 220, 'Fale com a gente', 34, INK, 'Unbounded', 700)
             + T(b + sf + 80, b + h - sf - 160, 'WhatsApp [A PREENCHER]', 26, INK, 'Inter', 600) + T(b + sf + 80, b + h - sf - 115, '@[perfil] · [site]', 26, INK)
             + R(b + sf + 520, b + h - sf - 270, 200, 200, WHITE, GREY, 2, 6, '10 8') + T(b + sf + 620, b + h - sf - 165, 'QR', 30, GREY, 'Inter', 700, 'middle'))
    print_piece(f'{AP}/07_Folhetos_e_Banners/{F(fr)}/Banner_80x200', f'{F(fr)}_Banner_Vertical_80x200', [('', body)], w, h, b, sf, fr,
                'Lona ou banner roll-up 80 × 200 cm. Confirmar com a gráfica a sangria e a área extra na base do roll-up.', 700)
for fr in ('Agencia', 'Shop', 'Institucional'): banner(fr)

# ------------------------------------------------------------------ 08 espaço físico (finais + simulações)
EF = f'{AP}/08_Espaco_Fisico'
lg, _, _ = logo_svg('Shop', 'Horizontal', 'Branca', 0, 0, 480, None)
lgh = float(re.search(r'height="([\d.]+)"', lg)[1]); lg, _, _ = logo_svg('Shop', 'Horizontal', 'Branca', 60, (400 - lgh) / 2, 480, None)
print_piece(f'{EF}/Placa_Identificacao', 'Zhibo_Shop_Placa_Identificacao_60x40cm', [('', R(0, 0, 600, 400, RED) + lg)], 600, 400, 0, 30, 'Shop',
            '[A MEDIR] Medida proposta 60 × 40 cm em ACM ou PVC 3 mm. Confirmar local, medida e fixação antes de produzir.', 1000)
lg, lw2, lh2 = logo_svg('Shop', 'Horizontal', 'Colorida', 0, 0, 1600, None)
print_piece(f'{EF}/Logo_Parede_Painel', 'Zhibo_Shop_Logo_Parede_Recorte', [('', lg)], 1600, round(lh2), 0, 0, 'Shop',
            '[A MEDIR] Largura de referência 160 cm (adesivo recortado ou letra caixa). Ajustar à parede real mantendo a proporção.', 1400)
bd = R(0, 0, 2000, 2000, INK)
for i in range(4):
    for j in range(4):
        sx, sy = 120 + j * 470, 160 + i * 470
        bd += sym_svg(RED, sx, sy, 230)
        lgs, _, _ = logo_svg('Institucional', 'Compacta', 'Negativa', sx + 15, sy + 210, 200, None) if False else ('', 0, 0)
print_piece(f'{EF}/Painel_Fotos_Gravacoes', 'Zhibo_Painel_Backdrop_200x200cm', [('', bd)], 2000, 2000, 0, 50, 'Institucional',
            '[A MEDIR] Backdrop 2 × 2 m em lona, padrão de símbolos. Confirmar a medida do espaço e a altura do enquadramento das câmeras.', 1000)
cam_f, _, _ = logo_svg('Shop', 'Horizontal', 'Colorida', 0, 0, 100, None)
cam_v = sym_svg(RED, 25, 0, 200) + logo_svg('Shop', 'Vertical', 'Preta', 0, 0, 0.1, None)[0][:0]
cam_vh = float(re.search(r'height="([\d.]+)"', sym_svg(RED, 25, 0, 200))[1])
lgv, _, _ = logo_svg('Shop', 'Horizontal', 'Preta', 0, cam_vh + 30, 250, None)
print_piece(f'{EF}/Camiseta_Equipe', 'Zhibo_Shop_Camiseta', [('Frente_Peito', cam_f), ('Costas', sym_svg(RED, 25, 0, 200) + lgv)], 100, 25, 0, 0, 'Shop',
            'Frente: logo de 10 cm no peito esquerdo. Costas: símbolo + nome, 25 cm de largura. Camiseta preta ou branca (versões de cor conforme o manual). Confirmar a técnica (silk ou DTF) com o fornecedor.', 800)
# fix camiseta costas artboard size
p_ = f'{EF}/Camiseta_Equipe/Editaveis/Zhibo_Shop_Camiseta_Costas_v01.svg'
s_ = open(p_).read(); hh = cam_vh + 30 + float(re.search(r'height="([\d.]+)"', lgv)[1])
s_ = re.sub(r'viewBox="0 0 [\d.]+ [\d.]+" width="[\d.]+mm" height="[\d.]+mm"', f'viewBox="0 0 250 {hh:.1f}" width="250mm" height="{hh:.1f}mm"', s_, count=1)
open(p_, 'w').write(s_.replace('<svg x="25.00"', '<svg x="25.00"', 1))
for j in svg_jobs:
    if j['svg'] == p_: j['pdfWidthMm'] = 250
SPECS[-1]['size'] = 'Frente 10 cm de largura · Costas 25 cm de largura'

# simulations (HTML scenes)
def sim(name, folder, inner, w=1600, h=1000):
    os.makedirs(f'{folder}/Simulacoes', exist_ok=True)
    html_jobs.append(dict(html=f'<html><body style="margin:0;width:{w}px;height:{h}px;overflow:hidden;font-family:Inter;position:relative">{inner}<div style="position:absolute;left:20px;bottom:16px;font:600 18px Inter;color:#5C504A;background:rgba(255,255,255,.8);padding:6px 10px">SIMULAÇÃO · medidas a confirmar no local</div></body></html>',
                          w=w, h=h, out=f'{folder}/Simulacoes/{name}.png'))
fu = lambda p: 'file://' + p
sim('Zhibo_Shop_Placa_Simulacao_v01', f'{EF}/Placa_Identificacao', f'<div style="position:absolute;inset:0;background:linear-gradient(#D9D2C9,#C9C0B5)"></div><div style="position:absolute;left:0;right:0;bottom:0;height:220px;background:#8E8379"></div><img src="{fu(EF + "/Placa_Identificacao/Finais_Digitais/Zhibo_Shop_Placa_Identificacao_60x40cm_v01_preview.png")}" style="position:absolute;left:590px;top:260px;width:420px;box-shadow:0 18px 30px rgba(0,0,0,.35)"><div style="position:absolute;left:520px;top:520px;width:560px;height:260px;border:14px solid #6B5F55;border-bottom:none;background:#3A322D"></div>')
sim('Zhibo_Shop_Parede_Simulacao_v01', f'{EF}/Logo_Parede_Painel', f'<div style="position:absolute;inset:0;background:#F2ECE4"></div><div style="position:absolute;left:0;right:0;bottom:0;height:260px;background:#B9A994"></div><img src="{fu(logo("Shop","Horizontal","Colorida","svg"))}" style="position:absolute;left:400px;top:250px;width:800px"><div style="position:absolute;left:560px;top:600px;width:480px;height:160px;background:#141010;border-radius:8px"></div>')
sim('Zhibo_Painel_Backdrop_Simulacao_v01', f'{EF}/Painel_Fotos_Gravacoes', f'<div style="position:absolute;inset:0;background:#DCD5CC"></div><img src="{fu(EF + "/Painel_Fotos_Gravacoes/Finais_Digitais/Zhibo_Painel_Backdrop_200x200cm_v01_preview.png")}" style="position:absolute;left:500px;top:90px;width:600px;height:600px"><div style="position:absolute;left:740px;top:430px;width:120px;height:360px;background:#5C504A;border-radius:60px 60px 0 0"></div><div style="position:absolute;left:760px;top:350px;width:80px;height:80px;background:#5C504A;border-radius:50%"></div>')
tee = lambda col, inner: f'<svg width="560" height="620" viewBox="0 0 560 620" style="position:absolute;top:150px"><path d="M140 20 L210 0 Q280 50 350 0 L420 20 L540 120 L470 210 L420 170 L420 600 L140 600 L140 170 L90 210 L20 120 Z" fill="{col}" stroke="#bbb"/>{inner}</svg>'
_lf = fu(logo('Shop', 'Horizontal', 'Colorida', 'svg')); _ls = fu(f'{LOGO}/Zhibo_Simbolo/Editaveis/Zhibo_Simbolo_Vermelho_v01.svg'); _lb = fu(logo('Shop', 'Horizontal', 'Branca', 'svg'))
_front = f'<image href="{_lf}" x="300" y="120" width="100"/>'
_back = f'<image href="{_ls}" x="200" y="140" width="160"/><image href="{_lb}" x="170" y="300" width="220"/>'
sim('Zhibo_Shop_Camiseta_Simulacao_v01', f'{EF}/Camiseta_Equipe', '<div style="position:absolute;inset:0;background:#EFE9E1"></div>'
    + f'<div style="position:absolute;left:180px">{tee(WHITE, _front)}</div><div style="position:absolute;left:860px">{tee(INK, _back)}</div>'
    + '<div style="position:absolute;left:400px;top:100px;font:700 24px Inter">Frente</div><div style="position:absolute;left:1080px;top:100px;font:700 24px Inter">Costas</div>')

# ------------------------------------------------------------------ 05 capas de destaques (1080x1920)
ICO = f'{DIST}/01_Identidade_Visual/Elementos_Graficos/Icones/Editaveis'
HL = {'Agencia': [('Sobre', 'chat'), ('Servicos', 'roteiro'), ('Cases', 'resultado'), ('Bastidores', 'estudio'), ('Contato', 'chat')],
      'Shop': [('A_Casa', 'live'), ('Estrutura', 'iluminacao'), ('Lives', 'live'), ('Equipe', 'equipe'), ('Contato', 'chat')]}
HL['Agencia'][0] = ('Sobre', 'equipe')
for fr, items in HL.items():
    bgc, fg = (GOLD, 'Tinta') if fr == 'Agencia' else (RED, 'Branco')
    for nm, ic in items:
        icon_src = open(f'{ICO}/Zhibo_Icone_{ic}_{fg}_v01.svg').read()
        inner = re.sub(r'<svg [^>]*?>', '', re.sub(r'<\?xml[^>]*>', '', icon_src)).replace('</svg>', '')
        col = INK if fg == 'Tinta' else WHITE
        body = (f'<rect width="1080" height="1920" fill="{bgc}"/><g transform="translate(300 720) scale(20)" fill="none" stroke="{col}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" color="{col}">{inner}</g>')
        d = f'{AP}/05_Redes_Sociais/{F(fr)}/Capas_Destaques'
        os.makedirs(f'{d}/Editaveis', exist_ok=True)
        fn = f'{F(fr)}_Destaque_{nm}_v01'
        open(f'{d}/Editaveis/{fn}.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1920" width="1080" height="1920">{body}</svg>\n')
        svg_jobs.append(dict(svg=f'{d}/Editaveis/{fn}.svg', png=f'{d}/Finais_Digitais/{fn}.png', pngWidth=1080))
    shutil.copy(f'{AVATAR}/{F(fr)}_Avatar_v01.png', f'{AP}/05_Redes_Sociais/{F(fr)}/Finais_Digitais/{F(fr)}_Avatar_v01.png')

# ------------------------------------------------------------------ 09 coassinatura (SVG)
CO = f'{AP}/09_Materiais_para_Lives/Coassinatura'
os.makedirs(f'{CO}/Editaveis', exist_ok=True)
_m = json.load(open(f'{B}/out/manifest.json')); X = _m['unitX']
for fr, lab in (('Agencia', 'MARCA CLIENTE'), ('Shop', 'MARCA CLIENTE'), ('Institucional', 'PARCEIRO')):
    for cw, txt, bgc in (('Colorida', INK, None), ('Negativa', PAPER, INK)):
        it = [i for i in _m['items'] if i['front'] == fr and i['layout'] == 'Horizontal' and i['colorway'] == cw][0]
        H0 = 100; k = H0 / it['h']; x = X * k; lw_ = it['w'] * k
        lg, _, _ = logo_svg(fr, 'Horizontal', cw, 0, 0, lw_, H0)
        sep_x = lw_ + 2 * x; part_x = sep_x + 2 * x; pw = 2.6 * H0
        body = ('' if not bgc else R(-40, -40, part_x + pw + 80, H0 + 80, bgc)) + lg + f'<line x1="{sep_x:.1f}" y1="{-H0 * .25:.1f}" x2="{sep_x:.1f}" y2="{H0 * 1.25:.1f}" stroke="{txt}" stroke-width="2"/>'
        body += R(part_x, 0, pw, H0, 'none', txt, 2, 0, '8 6') + T(part_x + pw / 2, H0 / 2 + 7, f'LOGO {lab}', 20, txt, 'Inter', 600, 'middle')
        vb = f'{-40} {-40} {part_x + pw + 80:.1f} {H0 + 80}'
        fn = f'{F(fr)}_Coassinatura_{"Cliente" if fr != "Institucional" else "Parceiro"}_{cw}_v01'
        open(f'{CO}/Editaveis/{fn}.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{(part_x + pw + 80) * 4:.0f}" height="{(H0 + 80) * 4}">{body}</svg>\n')
        svg_jobs.append(dict(svg=f'{CO}/Editaveis/{fn}.svg', png=f'{CO}/Finais_Digitais/{fn}.png', pngWidth=2400, pdf=f'{CO}/Impressao/{fn}.pdf', pdfWidthMm=200))

json.dump(svg_jobs, open(f'{B}/jobs_apps3.json', 'w')); json.dump(html_jobs, open(f'{B}/jobs_apps3_html.json', 'w')); json.dump(SPECS, open(f'{B}/specs.json', 'w'), ensure_ascii=False, indent=1)
print('svg', len(svg_jobs), 'sims', len(html_jobs))
