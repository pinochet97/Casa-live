"""03_Aplicacoes: 03 Briefing/Plano (docx, xlsx), 05 Redes sociais, 09 Materiais para lives (pptx)."""
from deck import *
import content as K
from docx import Document
from docx.shared import Pt as DPt, Cm, RGBColor as DRGB
from docx.enum.text import WD_ALIGN_PARAGRAPH
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.drawing.image import Image as XImage
AP = f'{DIST}/03_Aplicacoes_da_Marca'
F = lambda fr: FRONTS[fr]['file']

# ------------------------------------------------------------------ docx helpers
def doc_base(front, title, subtitle):
    d = Document()
    sec = d.sections[0]; sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2); sec.top_margin = Cm(2.2); sec.bottom_margin = Cm(2)
    st = d.styles['Normal']; st.font.name = 'Inter'; st.font.size = DPt(10.5)
    hp = sec.header.paragraphs[0]; hp.add_run().add_picture(logo(front, 'Horizontal', 'Colorida'), height=Cm(0.9))
    fp = sec.footer.paragraphs[0]; r = fp.add_run(f'{FRONTS[front]["name"]} · Comercial: Felipe Percebão · WhatsApp {TBD} · {TBD}@[dominio]')
    r.font.size = DPt(8); r.font.color.rgb = DRGB(0x5C, 0x50, 0x4A)
    h = d.add_paragraph(); r = h.add_run(title); r.font.name = 'Unbounded'; r.font.bold = True; r.font.size = DPt(20)
    if subtitle:
        p = d.add_paragraph(); r = p.add_run(subtitle); r.font.color.rgb = DRGB(0x5C, 0x50, 0x4A)
    return d

def doc_section(d, title):
    p = d.add_paragraph(); p.paragraph_format.space_before = DPt(12)
    r = p.add_run(title.upper()); r.font.bold = True; r.font.size = DPt(10); r.font.color.rgb = DRGB(0xE5, 0x26, 0x2A)

def doc_fields(d, rows, widths=(6, 11)):
    t = d.add_table(rows=len(rows), cols=2); t.style = 'Table Grid'
    for i, (k, v) in enumerate(rows):
        c0, c1 = t.rows[i].cells; c0.width, c1.width = Cm(widths[0]), Cm(widths[1])
        c0.text = ''; rr = c0.paragraphs[0].add_run(k); rr.font.bold = True; rr.font.size = DPt(10)
        c1.text = v
    return t

def doc_grid(d, header, n_rows):
    t = d.add_table(rows=n_rows + 1, cols=len(header)); t.style = 'Table Grid'
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]; c.text = ''; rr = c.paragraphs[0].add_run(h); rr.font.bold = True; rr.font.size = DPt(9.5)
    return t

def briefing(front):
    d = doc_base(front, 'Ficha de briefing do cliente', 'Preencha e devolva antes do onboarding. Campos com [ ] são obrigatórios.')
    doc_section(d, 'Marca e responsáveis')
    doc_fields(d, [('Marca', '[ ]'), ('Razão social e CNPJ', '[ ]'), ('Decisor (nome, cargo, WhatsApp)', '[ ]'),
                   ('Responsável pela operação na live (nome, WhatsApp)', '[ ]'), ('Contato financeiro', '[ ]'), ('Link da loja e @ da conta TikTok', '[ ]')])
    doc_section(d, 'Objetivo da ação')
    doc_fields(d, [('Objetivo principal', '[ ] ex.: vender estoque, lançar produto, data sazonal'), ('Meta (se houver)', '[ ]'), ('Período', '[ ]')])
    doc_section(d, 'Produtos (3 a 5)')
    t = doc_grid(d, ['Produto', 'SKU / ID', 'Preço normal', 'Preço mínimo de live', 'Estoque', 'Prazo de envio'], 5)
    doc_section(d, 'Público')
    doc_fields(d, [('Quem compra', '[ ]'), ('Tom da marca', '[ ]'), ('Concorrentes', '[ ]')])
    doc_section(d, 'Informações e diferenciais dos produtos')
    doc_fields(d, [('3 benefícios principais (por produto)', '[ ]'), ('Como demonstrar', '[ ]'), ('Perguntas frequentes e respostas', '[ ]'), ('Objeções comuns e respostas', '[ ]')])
    doc_section(d, 'Ofertas e condições comerciais')
    doc_fields(d, [('Produto âncora', '[ ]'), ('Promoção relâmpago', '[ ]'), ('Kits, brindes, cupons', '[ ]'), ('Limites de desconto', '[ ]')])
    doc_section(d, 'Datas e disponibilidade')
    doc_fields(d, [('Datas importantes (lançamentos, promoções)', '[ ]'), ('Dias e horários preferidos para live', '[ ]'), ('Datas indisponíveis', '[ ]')])
    doc_section(d, 'Materiais e acessos necessários')
    doc_fields(d, [('Acesso à conta como membro da equipe', '[ ] concedido em __/__ por ____'), ('Amostras enviadas (1 por SKU, 2 se consumível)', '[ ]'),
                   ('Logo e materiais de marca', '[ ] link'), ('Autorização de uso de imagem e dos cortes', '[ ] sim / não')])
    doc_section(d, 'Observações e restrições informadas pelo cliente')
    doc_fields(d, [('O que NÃO pode ser dito (promessas, comparações, termos proibidos)', '[ ]'), ('Outras restrições', '[ ]')])
    p = d.add_paragraph(); p.paragraph_format.space_before = DPt(14)
    p.add_run('Aprovado por: ____________________   Data: __/__/____').font.size = DPt(10)
    return d

def plano_xlsx(front, path):
    wb = Workbook(); ws = wb.active; ws.title = 'Plano de execução'
    ws['A1'] = f'{FRONTS[front]["name"]} — Plano de execução das lives'; ws['A1'].font = Font(name='Unbounded', bold=True, size=14)
    ws['A2'] = 'Cliente: [ ]   Campanha: [ ]   Período: [ ]   Conta de transmissão: [ ]'; ws['A2'].font = Font(name='Inter', size=10, color='5C504A')
    hdr = ['ID da live', 'Data', 'Horário', 'Duração', 'Conta de transmissão', 'Host', 'Moderador', 'Produtos (sequência)', 'Ofertas e chamadas principais',
           'Preparação necessária', 'Responsável', 'Prazo', 'Status']
    widths = [12, 11, 9, 9, 20, 14, 14, 34, 34, 30, 14, 11, 14]
    thin = Side(style='thin', color='EDE2D3')
    for i, (h, w) in enumerate(zip(hdr, widths), start=1):
        c = ws.cell(row=4, column=i, value=h); c.font = Font(name='Inter', bold=True, color='FFF7EC'); c.fill = PatternFill('solid', fgColor='141010')
        c.alignment = Alignment(wrap_text=True, vertical='center'); ws.column_dimensions[c.column_letter].width = w
    for r in range(5, 25):
        for i in range(1, len(hdr) + 1):
            c = ws.cell(row=r, column=i); c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
            c.alignment = Alignment(wrap_text=True, vertical='top'); c.font = Font(name='Inter', size=10)
            if r % 2 == 0: c.fill = PatternFill('solid', fgColor='FFF7EC')
        ws.cell(row=r, column=4, value='2 h')
    ws.cell(row=5, column=1, value='CL-2026-001'); ws.cell(row=5, column=8, value='1) [Produto A]  2) [Produto B]  3) [Produto C]')
    dv = DataValidation(type='list', formula1='"Planejada,Preparação,Pronta (D-1 ok),Realizada,Remarcada,Cancelada"', allow_blank=True)
    ws.add_data_validation(dv); dv.add('M5:M24')
    ws.row_dimensions[4].height = 30; ws.freeze_panes = 'A5'
    ws2 = wb.create_sheet('Como usar')
    for i, line in enumerate(['O ID da live (CL-AAAA-NNN) nasce na planilha Agenda e nunca é reaproveitado.', 'Status: Planejada → Preparação → Pronta (D-1 ok) → Realizada.',
                              'Live remarcada: a linha antiga fica “Remarcada” e a nova data ganha outro ID.', 'Ofertas precisam estar aprovadas pela marca até D-3.'], start=1):
        ws2.cell(row=i, column=1, value=line).font = Font(name='Inter', size=11)
    ws2.column_dimensions['A'].width = 100
    os.makedirs(os.path.dirname(path), exist_ok=True); wb.save(path)

for fr in ('Agencia', 'Shop'):
    d = f'{AP}/03_Briefing_e_Plano_de_Lives/{F(fr)}/Editaveis'; os.makedirs(d, exist_ok=True)
    briefing(fr).save(f'{d}/{F(fr)}_Ficha_de_Briefing_v01.docx')
    plano_xlsx(fr, f'{d}/{F(fr)}_Plano_de_Execucao_Lives_v01.xlsx')

# ------------------------------------------------------------------ social templates (pptx in px-like inches: 1080 px = 11.25 in)
PX = 11.25 / 1080
def px(v): return v * PX
def social(p, front, tone, fmt, kicker, title, body, photo_label=None, client=False, contact=False, num=None):
    w, h = SIZES[fmt]
    dark_bg = {'Institucional': INK, 'Agencia': INK, 'Shop': RED}[front]
    bg = dark_bg if tone == 'Escuro' else PAPER
    s = slide(p, bg); dk = tone == 'Escuro'
    image(s, bg_image(front, tone, 'Feed_4x5' if fmt == 'feed' else 'Stories_9x16'), 0, 0, w, h)
    top = px(170) if fmt == 'story' else px(80)              # stories: keep clear of the top UI
    image_fit(s, logo(front, 'Horizontal', ('Branca' if bg == RED else 'Negativa') if dk else 'Colorida'), px(80), top, px(420), px(70))
    y = top + px(150)
    kc = (GOLD if bg == INK else PAPER) if dk else ('#B07D00' if front == 'Agencia' else RED)
    text(s, px(80), y, w - px(160), px(50), kicker.upper(), size=20, bold=True, color=kc)
    text(s, px(80), y + px(60), w - px(160), px(260), title, size=46, bold=True, font=HEAD, color=PAPER if dk else INK, line=1.0)
    y2 = y + px(340)
    if body: text(s, px(80), y2, w - px(160), px(200), body, size=22, color=PAPER if dk else INK, line=1.2); y2 += px(210)
    if photo_label:
        ph = (h - y2 - px(320 if fmt == 'story' else 200))
        photo(s, px(80), y2, w - px(160), ph, photo_label, dark=dk)
        y2 += ph + px(30)
    if client:
        box(s, w - px(80) - px(300), top - px(10), px(300), px(90), fill=None, line=PAPER if dk else GREY, dash=True)
        text(s, w - px(80) - px(300), top - px(10), px(300), px(90), 'LOGO DO CLIENTE', size=12, color=PAPER if dk else GREY, align='center', anchor='middle')
    if contact:
        text(s, px(80), h - px(300 if fmt == 'story' else 170), w - px(160), px(120), [f'WhatsApp {TBD}', f'@{TBD}'], size=20, color=PAPER if dk else INK, bold=True)
    return s

SOCIAL = {
    'Agencia': {'feed': [('Apresentação', 'Somos a Zhibo Agência', 'Planejamos lives de venda que vendem no TikTok Shop.', 'Foto real da equipe', False, False),
                         ('Serviços', 'Planejamento, roteiro e resultado', 'Fichas de produto, ofertas, calendário e relatórios.', None, False, True),
                         ('Processo de trabalho', 'Do briefing ao relatório', 'Onboarding · planejamento · live · relatório D+1 · revisão mensal', 'Foto real de bastidor', False, False),
                         ('Resultados', '[Resultado comprovado]', '[Cliente] · [período] · números do painel', 'Foto real do case', True, False)],
                'story': [('Serviços', 'O que a agência faz', 'Planejamento · fichas · roteiro · ofertas · relatórios', 'Foto real', False, False),
                          ('Bastidores', '[Título do bastidor]', None, 'Foto ou vídeo real de bastidor', False, False),
                          ('Cases', '[Cliente]: [resultado]', '[período] · números do painel', 'Foto real do case', True, False),
                          ('Contato', 'Bora colocar sua marca ao vivo?', 'Chama no direct ou no WhatsApp', None, False, True)]},
    'Shop': {'feed': [('Estrutura', 'A casa onde sua marca entra ao vivo', '2 a 3 cenários, luz, áudio e internet de reserva.', 'Foto real do estúdio', False, False),
                      ('Equipe', 'Host, moderador e coordenação', 'Em cada live, uma equipe completa.', 'Foto real da equipe', False, False),
                      ('Formatos de live', 'Venda, lançamento e datas sazonais', 'Lives de 2 h com relâmpago nos picos.', None, False, True),
                      ('Projetos realizados', '[Marca] ao vivo na Zhibo Shop', '[data] · [horas] · números do painel', 'Foto real da live', True, False)],
             'story': [('Agenda', 'Ao vivo hoje às [HH:MM]', '[Marca] · [oferta principal]', 'Foto real do produto', True, False),
                       ('Bastidores', '[Título do bastidor]', None, 'Foto ou vídeo real de bastidor', False, False),
                       ('O espaço', 'Conheça a Zhibo Shop', 'Cenários, luz e equipe pronta para vender.', 'Foto real do espaço', False, False),
                       ('Contato', 'Agende uma live', 'Chama no direct ou no WhatsApp', None, False, True)]},
}
for fr, sets in SOCIAL.items():
    d = f'{AP}/05_Redes_Sociais/{F(fr)}'
    for fmt, items in sets.items():
        p = new_deck(fmt)
        for tone in ('Claro', 'Escuro'):
            for (k, t, b, ph, cl, ct) in items: social(p, fr, tone, fmt, k, t, b, ph, cl, ct)
        nm = f'{F(fr)}_{"Feed_1080x1350" if fmt == "feed" else "Stories_1080x1920"}_Templates_v01'
        export(p, f'{d}/Editaveis/{nm}.pptx', f'{d}/Finais_Digitais', f'{d}/Finais_Digitais/{"Feed" if fmt == "feed" else "Stories"}_PNG', 1080)

# ------------------------------------------------------------------ 09 materiais para lives (stories 1080x1920, safe zones)
SAFE_NOTE = 'Área segura: conteúdo entre 15% e 55% da altura. A parte de baixo fica livre para comentários e o cartão do produto.'
def live_set(front):
    p = new_deck('story'); w, h = SIZES['story']
    items = [('Divulgação de live', 'Live hoje às [HH:MM]', '[Marca participante] · [data] · [oferta principal]', 'Foto real do produto ou do host', 'pre'),
             ('Programação semanal', 'Agenda da semana', None, None, 'agenda'),
             ('Apresentação de produto', '[Nome do produto]', '[Benefício 1] · [Benefício 2] · [Benefício 3]', 'Foto real do produto', 'live'),
             ('Oferta ou cupom', 'Cupom [CÓDIGO]', '[__]% OFF até [HH:MM] · enquanto durar o estoque', None, 'live'),
             ('Apresentação do host', 'Com [Nome do host]', '[Uma linha sobre o host]', 'Foto real do host', 'live'),
             ('Resultado / destaque', 'Obrigado por ter vindo!', '[Destaque da live: produto campeão, próxima data]', 'Foto real da live', 'pos')]
    for k, t, b, ph, kind in items:
        s = social(p, front, 'Escuro', 'story', k, t, b, None, client=True)
        if kind == 'agenda':
            for i, dia in enumerate(['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SÁB']):
                yy = px(780) + i * px(150)
                box(s, px(80), yy, w - px(160), px(130), fill=PAPER, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.15)
                text(s, px(110), yy, px(160), px(130), dia, size=24, bold=True, font=HEAD, color=RED, anchor='middle')
                text(s, px(300), yy, w - px(420), px(130), '[HH:MM] · [Marca] · [oferta]', size=22, color=INK, anchor='middle')
        elif kind == 'live':
            if ph: photo(s, px(80), px(800), w - px(160), px(250), ph, dark=True)
            box(s, 0, h * .6, w, h * .4, fill=None, line=GOLD, lw=2, dash=True)
            text(s, px(80), h * .6 + px(30), w - px(160), px(200), ['ÁREA RESERVADA À INTERFACE DA LIVE', 'Comentários, cartão do produto e botões. Não colocar texto aqui. (Apague esta caixa antes de usar.)'], size=16, color=GOLD, bold=True)
        elif ph:
            photo(s, px(80), px(860), w - px(160), px(700), ph, dark=True)
    return p
for fr in ('Shop', 'Agencia'):
    d = f'{AP}/09_Materiais_para_Lives/{F(fr)}'
    export(live_set(fr), f'{d}/Editaveis/{F(fr)}_Materiais_para_Lives_Templates_v01.pptx', f'{d}/Finais_Digitais', f'{d}/Finais_Digitais/PNG', 1080)
print('ok')
