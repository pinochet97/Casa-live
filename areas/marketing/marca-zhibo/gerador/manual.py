from deck import *
FIG = f'{B}/figs'
p = new_deck('16:9'); n = 0
def nx():
    global n; n += 1; return n

cover(p, 'Institucional', 'Manual da marca', 'Zhibo, Zhibo Agência e Zhibo Shop. Versão 01, novembro de 2026.', 'Identidade visual')

s = page(p, 'Institucional', 'Sumário', 'O que está neste manual', nx())
items = ['01  A marca e o símbolo', '02  Arquitetura: Zhibo, Agência e Shop', '03  Construção e versões das assinaturas',
         '04  Área de proteção e tamanho mínimo', '05  Cores', '06  Tipografia', '07  Símbolo, avatares e marca-d’água',
         '08  Elementos gráficos e fundos', '09  Fotografia', '10  Aplicação em fundos, documentos e impressos',
         '11  Usos incorretos', '12  Coassinatura com clientes e parceiros', '13  Agência e Shop juntas', '14  Arquivos e contato']
text(s, M, 2.0, 5.8, 5, items[:7], size=15, spacing=10)
text(s, 7.0, 2.0, 5.8, 5, items[7:], size=15, spacing=10)

# 01
section(p, 'Institucional', '01', 'A marca e o símbolo')
s = page(p, 'Institucional', '01 · A marca', 'Zhibo quer dizer “transmissão ao vivo”', nx())
text(s, M, 2.0, 5.6, 4.5, [
    [('zhí bō', dict(bold=True, font=HEAD, size=22))],
    'Em mandarim, zhibo é o nome da transmissão ao vivo. A China é onde a venda em live nasceu e virou hábito.',
    'Usamos só a palavra, escrita no nosso alfabeto. Caracteres chineses não fazem parte da marca.',
    [('Grafia correta: ', dict(bold=True)), ('Zhibo, com Z maiúsculo no texto corrido. No logo, sempre minúsculo: “zhibo”.', {})],
], size=15, spacing=14)
image_fit(s, f'{LOGO}/Zhibo_Simbolo/Finais_Digitais/Zhibo_Simbolo_Vermelho_v01.png', 7.4, 1.9, 4.6, 3.2, align='center')
text(s, 7.0, 5.3, 5.5, 1.2, [[('O símbolo: ', dict(bold=True)), ('o play com duas ondas de sinal. Quer dizer “estamos no ar”: a live começou e a venda está acontecendo.', {})]], size=13, align='center')

# 02
section(p, 'Institucional', '02', 'Arquitetura da marca')
s = page(p, 'Institucional', '02 · Arquitetura', 'Uma marca, três assinaturas', nx())
cols = [('Institucional', 'Zhibo', 'A operação como um todo. Apresentações gerais, contratos, papelaria, eventos, quando as duas frentes aparecem juntas.', INK),
        ('Agencia', 'Zhibo Agência', 'Planejamento, estudo de produto, roteiros, campanhas e acompanhamento de resultados. Propostas e comunicação da agência.', GOLD),
        ('Shop', 'Zhibo Shop', 'A casa de lives: estúdio, hosts, moderação e transmissão. Peças de live, agenda, sinalização da casa.', RED)]
for i, (f, nm, desc_, col) in enumerate(cols):
    x = M + i * 4.05
    box(s, x, 2.0, 3.8, 4.6, fill=WHITE, line=INK, lw=1.25, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
    box(s, x, 2.0, 3.8, 0.18, fill=col)
    image_fit(s, logo(f, 'Vertical', 'Colorida'), x + 0.3, 2.45, 3.2, 1.5, align='center')
    text(s, x + 0.3, 4.15, 3.2, 0.4, f'Quando usar {nm}', size=13, bold=True)
    text(s, x + 0.3, 4.6, 3.2, 1.9, desc_, size=12, line=1.25)
s = page(p, 'Institucional', '02 · Arquitetura', 'Qual assinatura usar', nx())
table(s, M, 1.95, 11.9, [
    ['Material', 'Assinatura', 'Por quê'],
    ['Apresentação geral, site, contrato, cartão institucional', 'Zhibo', 'Fala da operação inteira'],
    ['Proposta de planejamento, campanha, roteiro, relatório de campanha', 'Zhibo Agência', 'Serviço intelectual e de gestão'],
    ['Agenda de lives, divulgação de live, placa da casa, camiseta da equipe da casa', 'Zhibo Shop', 'Execução das lives na casa'],
    ['Projeto que envolve as duas frentes', 'Zhibo (e cita Agência + Shop no texto)', 'Evita duas assinaturas competindo'],
    ['Peça com marca cliente', 'A frente responsável + marca cliente', 'Ver coassinatura (seção 12)'],
], col_w=[5.2, 3.2, 3.5], size=12, row_h=0.62)
text(s, M, 6.0, 11.9, 0.6, 'Na dúvida, use Zhibo (institucional). Nunca misture duas assinaturas na mesma peça, exceto no formato “Agência e Shop juntas”.', size=12, color=GREY)

# 03
section(p, 'Institucional', '03', 'Construção e versões')
s = page(p, 'Institucional', '03 · Construção', 'As regras que valem para as três assinaturas', nx())
bullets(s, M, 2.0, 6.0, 4.6, [
    'Nome “zhibo”: Unbounded ExtraBold, entreletra -4,2%, convertido em curvas. Nunca redigitar.',
    'Descritor (“agência”, “shop”): Unbounded Medium, sempre com 50% do tamanho do nome.',
    'Horizontal: símbolo com 1,1 vez a altura do nome, centralizado na altura do nome. Descritor na mesma linha de base.',
    'Vertical: símbolo com 1,3 vez a altura do nome, centralizado acima. Descritor centralizado abaixo.',
    'Compacta: símbolo com a altura do bloco “nome + descritor”. Na institucional, a compacta é só o nome.',
    'O símbolo é centralizado pela caixa visual real, contando a espessura do traço.',
], size=13, gap=9)
image_fit(s, logo('Agencia', 'Horizontal'), 7.2, 2.1, 5.3, 1.0, align='center')
image_fit(s, logo('Agencia', 'Vertical'), 7.2, 3.4, 2.5, 1.9, align='center')
image_fit(s, logo('Agencia', 'Compacta'), 10.0, 3.6, 2.5, 1.5, align='center')
text(s, 7.2, 5.55, 5.3, 0.4, 'Horizontal · Vertical · Compacta', size=11, color=GREY, align='center')
for f in ('Institucional', 'Agencia', 'Shop'):
    s = page(p, f, '03 · Versões', f'Versões de {FRONTS[f]["name"]}', nx())
    for ci, cw in enumerate(['Colorida', 'Negativa', 'Preta', 'Branca']):
        x = M + ci * 3.0; bgc = INK if cw in ('Negativa', 'Branca') else WHITE
        for li, lay in enumerate(['Horizontal', 'Vertical', 'Compacta']):
            y = 1.9 + li * 1.6
            box(s, x, y, 2.85, 1.45, fill=bgc, line=SAND if bgc == WHITE else None)
            image_fit(s, logo(f, lay, cw), x + 0.25, y + 0.22, 2.35, 1.0, align='center')
        text(s, x, 6.72, 2.85, 0.3, cw + (' (fundo escuro)' if cw == 'Negativa' else ''), size=10.5, color=GREY, align='center')

# 04
section(p, 'Institucional', '04', 'Área de proteção e tamanho mínimo')
s = page(p, 'Institucional', '04 · Proteção', 'Área de proteção', nx())
image_fit(s, f'{FIG}/protecao.png', M, 1.8, 11.9, 4.9, align='center')
s = page(p, 'Institucional', '04 · Tamanho mínimo', 'Abaixo destes tamanhos, use o símbolo sozinho', nx())
image_fit(s, f'{FIG}/tamanho_minimo.png', M, 2.0, 11.9, 3.9, align='center')

# 05
section(p, 'Institucional', '05', 'Cores')
s = page(p, 'Institucional', '05 · Cores', 'Paleta principal e de apoio', nx())
image_fit(s, f'{FIG}/paleta.png', M, 1.8, 11.9, 4.8, align='center')
s = page(p, 'Institucional', '05 · Cores', 'Cada frente tem uma cor de apoio', nx())
for i, (f, col, txt) in enumerate([('Institucional', INK, 'Tinta. Peças sóbrias, fundo escuro com símbolo vermelho.'),
                                   ('Agencia', GOLD, 'Ouro Oferta. Destaques, selos, fundos de capa, avatar.'),
                                   ('Shop', RED, 'Vermelho Live. Energia da transmissão, fundos de capa, avatar.')]):
    x = M + i * 4.05
    box(s, x, 2.0, 3.8, 2.2, fill=col, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
    image_fit(s, f'{AVATAR}/{FRONTS[f]["file"]}_Avatar_v01.png', x + 1.2, 2.2, 1.4, 1.8, align='center')
    text(s, x, 4.4, 3.8, 0.4, FRONTS[f]['name'], size=15, bold=True, font=HEAD)
    text(s, x, 4.85, 3.8, 1.2, txt, size=12.5)
text(s, M, 6.2, 11.9, 0.6, 'O vermelho do símbolo e a Tinta dos textos são iguais nas três frentes. A cor de apoio só muda fundos, selos e destaques.', size=12, color=GREY)

# 06
section(p, 'Institucional', '06', 'Tipografia')
s = page(p, 'Institucional', '06 · Tipografia', 'Duas famílias gratuitas do Google Fonts', nx())
text(s, M, 2.0, 6, 0.4, 'TÍTULOS E SUBTÍTULOS', size=11, color=GREY, bold=True)
text(s, M, 2.35, 6, 1.0, 'Unbounded', size=40, bold=True, font=HEAD)
text(s, M, 3.35, 5.8, 1.6, ['Bold para títulos, Medium para subtítulos.', 'fonts.google.com/specimen/Unbounded'], size=13, spacing=6)
text(s, 7.0, 2.0, 6, 0.4, 'TEXTOS', size=11, color=GREY, bold=True)
text(s, 7.0, 2.35, 6, 1.0, 'Inter', size=40, bold=True, font=BODY)
text(s, 7.0, 3.35, 5.6, 1.6, ['Regular para textos, SemiBold para destaques.', 'fonts.google.com/specimen/Inter'], size=13, spacing=6)
table(s, M, 4.9, 11.9, [['Uso', 'Fonte', 'Peso', 'Tamanho em slides 16:9'],
                        ['Título', 'Unbounded', 'Bold', '26 a 40 pt'], ['Subtítulo / chamada', 'Unbounded', 'Medium', '16 a 20 pt'],
                        ['Texto', 'Inter', 'Regular', '12 a 15 pt'], ['Legenda / rótulo', 'Inter', 'SemiBold, maiúsculas', '10 a 11 pt']],
      col_w=[3.2, 2.6, 3.0, 3.1], size=11.5, row_h=0.36)

# 07
section(p, 'Institucional', '07', 'Símbolo, avatares e marca-d’água')
s = page(p, 'Institucional', '07 · Avatares', 'Um avatar por perfil, reconhecível em tamanho pequeno', nx())
for i, f in enumerate(['Institucional', 'Agencia', 'Shop']):
    x = M + 0.4 + i * 4.0
    image_fit(s, f'{AVATAR}/{FRONTS[f]["file"]}_Avatar_v01.png', x, 1.9, 2.6, 2.6, align='center')
    text(s, x - 0.4, 4.7, 3.4, 0.4, FRONTS[f]['name'], size=14, bold=True, align='center')
bullets(s, M, 5.3, 11.9, 1.6, ['Avatar = símbolo centralizado sobre a cor de apoio da frente. O nome do perfil identifica a frente; não coloque texto no avatar.',
                               'Arquivo 1080 × 1080 px. As redes cortam em círculo: o símbolo já está dentro da área segura.',
                               'Marca-d’água: logo horizontal branco ou preto com 60% de opacidade, no canto inferior, fora da área de comentários da live.'], size=12, gap=6)

# 08
section(p, 'Institucional', '08', 'Elementos gráficos e fundos')
s = page(p, 'Institucional', '08 · Elementos', 'Ondas, play e ícones', nx())
image_fit(s, bg_image('Shop', 'Escuro'), M, 1.9, 5.6, 3.15)
text(s, M, 5.2, 5.6, 1.2, 'Ondas de sinal: saem do play para a direita, como no símbolo. Sempre cortadas pela borda da peça, nunca soltas no meio do texto.', size=12)
image_fit(s, f'{FIG}/icones.png', 6.7, 1.9, 5.9, 1.6)
text(s, 6.7, 3.7, 5.9, 2.5, ['Ícones de traço, 2 px em grade de 24 px, cantos arredondados. Cores: Vermelho, Tinta ou Branco.',
                             'Padrões (ondas e play) e fundos prontos ficam em Elementos_Graficos, em 16:9, feed 4:5, stories 9:16 e A4, nas versões clara e escura de cada frente.'], size=12, spacing=8)

# 09
section(p, 'Institucional', '09', 'Fotografia')
s = page(p, 'Institucional', '09 · Fotografia', 'Fotos reais, com luz de estúdio e gente vendendo', nx())
for i, lab in enumerate(['Host demonstrando o produto, olhando para a câmera', 'Bastidor: moderador no painel, luz, celular no tripé', 'Produto em close, fundo limpo, luz suave']):
    photo(s, M + i * 4.05, 1.9, 3.8, 2.6, lab)
bullets(s, M, 4.75, 11.9, 2.0, [
    'Use só fotos reais da casa, da equipe e de lives feitas. Nada de banco de imagens com pessoas genéricas.',
    'Luz clara e frontal, cores naturais. Tratamento: contraste leve, pele natural, sem filtros coloridos.',
    'Sobre fotos, aplique o logo branco ou a versão negativa num canto, respeitando a área de proteção.',
    'Para usar imagem de host, cliente ou produto, guarde a autorização de uso (ver 04_Referencias_e_Insumos).'], size=12.5, gap=6)

# 10
section(p, 'Institucional', '10', 'Fundos, documentos e impressos')
s = page(p, 'Institucional', '10 · Aplicação', 'Contraste primeiro', nx())
combos = [(WHITE, 'Colorida', 'Branco / Papel: logo colorido'), (INK, 'Negativa', 'Tinta: logo negativo'),
          (RED, 'Branca', 'Vermelho: logo branco'), (GOLD, 'Preta', 'Ouro: logo preto')]
for i, (bgc, cw, lab) in enumerate(combos):
    x = M + i * 3.0
    box(s, x, 1.95, 2.85, 1.7, fill=bgc, line=SAND if bgc == WHITE else None)
    image_fit(s, logo('Institucional', 'Horizontal', cw), x + 0.3, 2.35, 2.25, 0.9, align='center')
    text(s, x, 3.75, 2.85, 0.4, lab, size=11, color=GREY, align='center')
bullets(s, M, 4.45, 11.9, 2.3, [
    'Documentos (propostas, relatórios, papel timbrado): fundo branco, logo colorido no topo, rodapé com contato. Textos em Tinta.',
    'Impressos: CMYK de referência deste manual. Peça prova de cor; sangria de 3 mm e margem de segurança de 5 mm (banners: 20 mm).',
    'Fotos: logo branco sobre área escura da foto, ou dentro de uma faixa Tinta.'], size=12.5, gap=6)

# 11
section(p, 'Institucional', '11', 'Usos incorretos')
s = page(p, 'Institucional', '11 · Usos incorretos', 'O que não fazer', nx())
image_fit(s, f'{FIG}/usos_incorretos.png', M, 1.75, 11.9, 5.0, align='center')

# 12
section(p, 'Institucional', '12', 'Coassinatura')
s = page(p, 'Institucional', '12 · Coassinatura', 'Zhibo + marca cliente ou parceiro', nx())
image_fit(s, f'{FIG}/coassinatura_shop.png', M, 1.75, 6.2, 2.0)
image_fit(s, f'{FIG}/coassinatura_agencia.png', M, 3.85, 6.2, 2.0)
bullets(s, 7.2, 1.9, 5.4, 4.8, [
    'Os dois logos com a mesma altura visual.',
    'Separador vertical: traço de 1 px (digital) ou 0,5 pt (impresso), com altura de 1,5 vez o logo.',
    'Distância entre cada logo e o separador: 2 x (x = altura do “z”).',
    'Zhibo à esquerda ou em cima. A marca cliente à direita ou embaixo.',
    'Use a frente responsável: Zhibo Shop em peças de live, Zhibo Agência em campanhas. Zhibo institucional com parceiros.',
    'Peças usadas durante a live: logos no topo, longe da área de produtos e comentários (ver 09_Materiais_para_Lives).'], size=12.5, gap=7)

# 13
section(p, 'Institucional', '13', 'Agência e Shop juntas')
s = page(p, 'Institucional', '13 · Juntas', 'Quando as duas frentes aparecem na mesma peça', nx())
image_fit(s, f'{FIG}/frentes_juntas.png', M, 1.8, 11.9, 3.9, align='center')
text(s, M, 5.9, 11.9, 0.8, 'Ordem fixa: Agência primeiro, Shop depois. É a ordem do trabalho: planejar e depois transmitir.', size=13)

# 14
s = page(p, 'Institucional', '14 · Arquivos', 'Onde estão os arquivos', nx())
table(s, M, 1.9, 11.9, [['O quê', 'Pasta no Drive', 'Formatos'],
                        ['Logos das três assinaturas', '01_Identidade_Visual / Logos / <frente>', 'SVG (editável), PDF vetorial, PNG transparente'],
                        ['Símbolo e marca-d’água', 'Logos / Zhibo_Simbolo e Logos / Marca_dAgua', 'SVG, PDF, PNG'],
                        ['Avatares', '01_Identidade_Visual / Avatares', 'PNG 1080 px, SVG'],
                        ['Cores e fontes', '01_Identidade_Visual / Cores_e_Fontes', 'PNG, PDF, guia com links'],
                        ['Ícones, padrões e fundos', '01_Identidade_Visual / Elementos_Graficos', 'SVG e PNG'],
                        ['Este manual', '01_Identidade_Visual / Manual_da_Marca', 'Google Slides e PDF']],
      col_w=[3.4, 4.9, 3.6], size=11.5, row_h=0.5)
text(s, M, 5.75, 11.9, 0.8, 'Dúvidas sobre a marca: Kaio (estratégia). Pedidos de peças: Duda (operação).', size=13, color=GREY)

out = f'{DIST}/01_Identidade_Visual/Manual_da_Marca'
r = export(p, f'{out}/Editaveis/Zhibo_Manual_da_Marca_v01.pptx', f'{out}/Finais_Digitais', f'{B}/prev/manual', 800)
print(r, len(p.slides._sldIdLst))
