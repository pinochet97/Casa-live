"""03_Aplicacoes: 01 Propostas, 02 Relatórios, 03 Briefing e Plano, 04 Cases e Portfólio."""
from deck import *
import content as K
AP = f'{DIST}/03_Aplicacoes_da_Marca'
F = lambda fr: FRONTS[fr]['file']

def field(s, x, y, w, h, label, value, size=12):
    text(s, x, y, w, 0.3, label.upper(), size=9.5, color=GREY, bold=True)
    box(s, x, y + 0.3, w, h - 0.3, fill=WHITE, line=SAND)
    text(s, x + 0.12, y + 0.38, w - 0.24, h - 0.45, value, size=size)

# ------------------------------------------------------------------ 01 Propostas
def proposta(front, exemplo=False):
    p = new_deck(); n = [0]
    def nx(): n[0] += 1; return n[0]
    v = (lambda real, ph: real) if exemplo else (lambda real, ph: ph)
    cli = v('Marca Exemplo (fictícia)', '[NOME DO CLIENTE]')
    tag = 'EXEMPLO DE PREENCHIMENTO · DADOS FICTÍCIOS' if exemplo else 'MODELO EDITÁVEL'
    label = {'Agencia': 'Proposta Zhibo Agência', 'Shop': 'Proposta Zhibo Shop', 'Institucional': 'Proposta conjunta Zhibo (Agência + Shop)'}[front]
    s = cover(p, front, f'Proposta para {cli}', v('Lives de venda no TikTok Shop · válida até 30/12/2026', '[Objetivo em uma linha] · válida até [DATA]'), label)
    box(s, W - M - 3.3, M, 3.3, 1.2, fill=WHITE, line=GREY, dash=True)
    text(s, W - M - 3.3, M, 3.3, 1.2, ['LOGO DO CLIENTE', '(substituir esta caixa)'], size=9.5, color=GREY, align='center', anchor='middle')
    pill(s, M, 6.55, tag, fill=GOLD, color=INK, size=9.5)
    s = page(p, front, 'Objetivo', 'O que vamos alcançar juntos', nx())
    field(s, M, 1.9, 11.9, 1.6, 'Objetivo do projeto', v('Testar lives semanais para os 3 produtos mais vendidos da loja e medir vendas por hora.', '[Descreva o objetivo do cliente em 2 a 3 linhas]'), 14)
    field(s, M, 3.7, 5.8, 1.4, 'Canal e conta da transmissão', v('TikTok Shop, conta @marcaexemplo (acesso como membro da equipe)', '[Canal] · [@ da conta] · [forma de acesso]'))
    field(s, 6.8, 3.7, 5.8, 1.4, 'Audiência da conta (quando fizer parte)', v('Seguidores: 12.000 (dado fictício)', '[Seguidores / audiência média, se houver dados]'))
    field(s, M, 5.3, 11.9, 1.3, 'Produtos foco', v('Produto A, Produto B, Produto C', '[3 a 5 produtos com SKU]'))
    s = page(p, front, 'Escopo', 'Escopo contratado', nx())
    scope = {'Agencia': ['Planejamento do mês e calendário', 'Fichas de produto', 'Roteiro e plano de ofertas', 'Vídeos de aquecimento', 'Relatórios e revisão mensal'],
             'Shop': ['Lives no estúdio Zhibo Shop', 'Host e moderador em cada live', 'Cenário com a marca', 'Operação do carrinho e relâmpago', 'Relatório da live em D+1'],
             'Institucional': ['Agência: planejamento, fichas, roteiro, ofertas, relatórios', 'Shop: estúdio, host, moderador, operação da live', 'Revisão mensal conjunta']}[front]
    bullets(s, M, 1.95, 5.8, 4.5, [x + v('', '  [manter / remover]') for x in scope], size=14, gap=8)
    table(s, 6.9, 1.95, 5.7, [['Horas e sessões', ''], ['Horas ao vivo por mês', v('16 h', '[__ h]')], ['Sessões', v('8 lives de 2 h', '[__ lives de __ h]')],
                              ['Dias e horários', v('Terças e quintas, 19 h', '[dias] · [horário]')], ['Período', v('01/12 a 31/12/2026', '[início] a [fim]')]],
          col_w=[2.9, 2.8], size=12, row_h=0.55)
    s = page(p, front, 'Equipe, estrutura e entregas', 'Quem faz e o que você recebe', nx())
    text(s, M, 1.9, 5.8, 0.4, 'Equipe e estrutura', size=13, bold=True)
    bullets(s, M, 2.35, 5.8, 3, ['Host: ' + v('Duda', '[nome]'), 'Moderador: ' + v('Kaio', '[nome]'), 'Coordenação: ' + v('Duda', '[nome]'), 'Cenário: ' + v('cenário 1 com painel da marca', '[cenário]')], size=13, gap=5)
    text(s, 7.0, 1.9, 5.6, 0.4, 'Entregas', size=13, bold=True)
    bullets(s, 7.0, 2.35, 5.6, 4.3, K.ANTES[:3] + K.DEPOIS[:3], size=12, gap=4)
    s = page(p, front, 'Cronograma', 'Cronograma', nx())
    table(s, M, 1.95, 11.9, [['Etapa', 'Prazo', 'Responsável'], ['Assinatura do acordo', v('25/11', '[data]'), 'Marca + Zhibo'], ['Onboarding: formulário, acessos, amostras', v('26/11 a 30/11', '[D-7 a D-1]'), 'Marca'],
                             ['Fichas e ofertas aprovadas', v('29/11', '[D-3]'), 'Marca aprova, Zhibo prepara'], ['Primeira live', v('02/12', '[data]'), 'Zhibo'],
                             ['Relatório da live', 'D+1 até 12 h', 'Zhibo'], ['Revisão do mês', v('29/12', '[data]'), 'Marca + Zhibo']], col_w=[6.0, 3.0, 2.9], size=12, row_h=0.52)
    s = page(p, front, 'Investimento', 'Investimento e condições', nx())
    table(s, M, 1.95, 7.2, [['Item', 'Valor'], ['Fixo mensal', v('R$ 0 (mês de teste)', 'R$ [valor]')], ['Comissão sobre vendas líquidas', v('10%', '[__ %]')],
                            ['Adicionais', v('Não contratados', '[item] · R$ [valor]')], ['Total do mês (sem comissão)', v('R$ 0', 'R$ [valor]')]], col_w=[4.2, 3.0], size=12.5, row_h=0.58)
    text(s, 8.3, 1.95, 4.3, 4.7, [[('Condições de pagamento', dict(bold=True))], v('Comissão apurada no dia 1, vencimento no dia 5, Pix ou boleto, com nota fiscal.', '[forma, prazo, vencimento]'), '',
                                  [('Validade da proposta', dict(bold=True))], v('15 dias', '[__ dias] a partir de [data]'), '',
                                  [('Comissão', dict(bold=True))], 'Calculada sobre o GMV líquido: vendas das lives menos cancelamentos e devoluções.'], size=12.5, spacing=3)
    s = page(p, front, 'Responsabilidades', 'Quem cuida de quê', nx())
    text(s, M, 1.9, 5.8, 0.4, 'Marca', size=13, bold=True); bullets(s, M, 2.35, 5.8, 4.4, K.RESP_MARCA + ['Fornecer: acessos, amostras, fichas aprovadas, pessoa no WhatsApp durante a live'], size=12.5, gap=5)
    text(s, 7.0, 1.9, 5.6, 0.4, 'Zhibo', size=13, bold=True); bullets(s, 7.0, 2.35, 5.6, 4.4, K.RESP_ZHIBO, size=12.5, gap=5)
    s = page(p, front, 'Próximo passo', 'Contato do responsável comercial', nx())
    contact_block(s, M, 2.0, 11, front)
    text(s, M, 5.0, 11.9, 1.2, 'Para aprovar: responda esta proposta ou assine o acordo enviado por assinatura digital.', size=13)
    return p

for fr, nm in (('Agencia', 'Zhibo_Agencia'), ('Shop', 'Zhibo_Shop'), ('Institucional', 'Zhibo_Conjunta')):
    d = f'{AP}/01_Propostas_Comerciais/{F(fr)}'
    export(proposta(fr), f'{d}/Editaveis/{nm}_Proposta_Comercial_v01.pptx')
    export(proposta(fr, True), f'{B}/tmp/{nm}_Proposta_Comercial_Exemplo_v01.pptx', f'{d}/Finais_Digitais', f'{B}/prev/prop_{fr}', 500)
    os.rename(f'{d}/Finais_Digitais/{nm}_Proposta_Comercial_Exemplo_v01.pdf', f'{d}/Finais_Digitais/{nm}_Proposta_Comercial_Exemplo_v01.pdf')

# ------------------------------------------------------------------ 02 Relatórios
def relatorio(front):
    p = new_deck(); n = [0]
    def nx(): n[0] += 1; return n[0]
    s = cover(p, front, 'Relatório de resultados', '[Cliente] · [Campanha] · [Período]', {'Agencia': 'Zhibo Agência', 'Shop': 'Zhibo Shop', 'Institucional': 'Zhibo'}[front])
    pill(s, M, 6.55, 'NÚMEROS DESTE MODELO SÃO EXEMPLO DE LAYOUT', fill=GOLD, color=INK, size=9.5)
    s = page(p, front, 'Resumo', 'Resumo das entregas', nx())
    kpis = [('Lives realizadas', '8'), ('Horas ao vivo', '16 h'), ('Espectadores', '12.400'), ('Pedidos', '310'), ('Itens vendidos', '420'), ('Vendas brutas (GMV)', 'R$ 18.600')]
    w = (W - 2 * M - 5 * 0.2) / 6
    for i, (k, val) in enumerate(kpis):
        x = M + i * (w + 0.2)
        box(s, x, 1.95, w, 1.6, fill=WHITE, line=SAND, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
        text(s, x + 0.2, 2.1, w - 0.4, 0.4, k, size=10, color=GREY, bold=True)
        text(s, x + 0.2, 2.6, w - 0.4, 0.7, val, size=16, bold=True, font=HEAD)
    text(s, M, 3.7, 11.9, 0.3, 'Valores ilustrativos (exemplo de layout). Substituir pelos números do painel do TikTok Shop.', size=10, color=RED, bold=True)
    field(s, M, 4.15, 5.8, 2.45, 'Entregas do período', '[Lives, vídeos de aquecimento, cortes, fichas, relatórios]')
    field(s, 6.8, 4.15, 5.8, 2.45, 'Investimento em anúncios (quando houver)', '[Valor e canal, ou “Não houve”]')
    s = page(p, front, 'Sessões', 'Comparação entre sessões', nx())
    rows = [['Live', 'Data', 'Horas', 'Espectadores', 'Pico', 'Pedidos', 'Itens', 'GMV (R$)', 'Conversão']]
    ex = [('CL-001', '02/12', '2', '1.200', '180', '28', '36', '1.650', '2,3%'), ('CL-002', '04/12', '2', '1.450', '210', '35', '47', '2.080', '2,4%'),
          ('CL-003', '09/12', '2', '1.600', '260', '41', '55', '2.430', '2,6%'), ('CL-004', '11/12', '2', '1.520', '230', '38', '52', '2.270', '2,5%')]
    table(s, M, 1.95, 7.3, rows + [list(e) for e in ex], col_w=[0.8, 0.7, 0.6, 1.05, 0.6, 0.75, 0.6, 0.95, 1.25], size=10, row_h=0.42)
    vals = [1650, 2080, 2430, 2270]; mx = max(vals)
    text(s, 8.4, 1.95, 4.2, 0.3, 'GMV por live (R$)', size=11, bold=True)
    for i, vv in enumerate(vals):
        bh = 3.2 * vv / mx; x = 8.5 + i * 1.0
        box(s, x, 5.5 - bh, 0.6, bh, fill=RED); text(s, x - 0.2, 5.55, 1.0, 0.3, ex[i][0], size=9, align='center', color=GREY)
    text(s, M, 4.3, 7.3, 0.3, 'Exemplo de layout: valores ilustrativos.', size=10, color=RED, bold=True)
    field(s, M, 4.75, 7.3, 1.85, 'Comentário', '[O que explica a variação entre as sessões]')
    s = page(p, front, 'Produtos', 'Produtos com melhor desempenho', nx())
    table(s, M, 1.95, 11.9, [['Produto', 'Pedidos', 'Itens', 'GMV (R$)', 'Observação'], ['[Produto A]', '120', '160', '7.200', '[ex.: melhor no relâmpago]'],
                             ['[Produto B]', '95', '130', '5.400', ''], ['[Produto C]', '60', '80', '3.100', '']], col_w=[3.2, 1.5, 1.5, 1.8, 3.9], size=11.5, row_h=0.5)
    text(s, M, 4.1, 11.9, 0.3, 'Exemplo de layout: valores ilustrativos.', size=10, color=RED, bold=True)
    s = page(p, front, 'Aprendizados', 'Aprendizados, recomendações e próximos passos', nx())
    field(s, M, 1.9, 3.85, 4.7, 'Aprendizados', '[O que funcionou e o que não funcionou]')
    field(s, M + 4.05, 1.9, 3.85, 4.7, 'Recomendações', '[O que mudar nas próximas lives]')
    field(s, M + 8.1, 1.9, 3.8, 4.7, 'Próximos passos', '[Ação · responsável · prazo]')
    text(s, M, 6.65, 11.9, 0.3, 'GMV é venda bruta atribuída à live, não é lucro. Comissão sobre GMV líquido (menos cancelamentos e devoluções).', size=9.5, color=GREY)
    return p
for fr in ('Agencia', 'Shop', 'Institucional'):
    d = f'{AP}/02_Relatorios_de_Resultados/{F(fr)}'
    export(relatorio(fr), f'{d}/Editaveis/{F(fr)}_Relatorio_de_Resultados_v01.pptx', f'{d}/Finais_Digitais', f'{B}/prev/rel_{fr}' if fr == 'Shop' else None, 500)

# ------------------------------------------------------------------ 04 Cases e portfólio
def case_one(front):
    p = new_deck('A4'); w, h = SIZES['A4']
    s = slide(p, PAPER); box(s, 0, 0, w, 2.3, fill=INK if front == 'Agencia' else RED)
    image_fit(s, logo(front, 'Horizontal', 'Negativa' if front == 'Agencia' else 'Branca'), 0.6, 0.45, 3.0, 0.5)
    text(s, 0.6, 1.15, 7, 0.9, 'Case: [Cliente]', size=24, bold=True, font=HEAD, color=PAPER)
    photo(s, 0.6, 2.6, 3.4, 2.6, '[Foto do cliente / live]')
    for i, (k, vv) in enumerate([('Período', '[início a fim]'), ('Horas ao vivo', '[__ h]'), ('Lives', '[__]')]):
        field(s, 4.25, 2.6 + i * 0.87, 3.4, 0.8, k, vv, 11)
    field(s, 0.6, 5.45, 7.07, 1.2, 'Desafio', '[O problema da marca antes da Zhibo]', 11)
    field(s, 0.6, 6.85, 7.07, 1.2, 'Trabalho realizado', '[O que fizemos: planejamento, lives, ofertas]', 11)
    field(s, 0.6, 8.25, 7.07, 1.3, 'Resultados (painel da plataforma)', '[GMV, pedidos, conversão] · [investimento em anúncios, se houver]', 11)
    field(s, 0.6, 9.75, 7.07, 1.3, 'Depoimento autorizado', '“[Depoimento]” — [Nome, cargo]', 11)
    return p
def carrossel(front):
    p = new_deck('feed'); w, h = SIZES['feed']
    acc = FRONTS[front]['accent']; dark_bg = INK if front == 'Agencia' else RED
    titles = [('Case', '[Cliente]'), ('O desafio', '[Desafio em 2 linhas]'), ('O que fizemos', '[Trabalho realizado]'), ('Resultado', '[Número principal do painel]'), ('Quer o mesmo?', 'Chama no direct')]
    for i, (k, t) in enumerate(titles):
        bg = dark_bg if i in (0, 4) else PAPER; s = slide(p, bg); dk = bg != PAPER
        if dk: image(s, bg_image(front, 'Escuro', 'Feed_4x5'), 0, 0, w, h)
        image_fit(s, logo(front, 'Horizontal', ('Branca' if bg == RED else 'Negativa') if dk else 'Colorida'), 0.9, 0.9, 4.2, 0.7)
        text(s, 0.9, 3.2, 9.4, 0.6, k.upper(), size=22, bold=True, color=GOLD if bg == INK else (PAPER if dk else RED))
        text(s, 0.9, 4.0, 9.4, 3.2, t, size=54, bold=True, font=HEAD, color=PAPER if dk else INK, line=1.0)
        if i in (1, 2, 3): photo(s, 0.9, 7.6, 9.45, 5.2, '[Foto real do case]')
        text(s, w - 2.2, h - 1.2, 1.4, 0.5, f'{i + 1}/5', size=18, color=PAPER if dk else GREY, align='right')
    return p
def portfolio(front):
    p = new_deck()
    s = page(p, front, 'Portfólio', '[Cliente] · [Formato do projeto]', 1)
    photo(s, M, 1.9, 6.0, 4.7, '[Foto real do projeto]')
    for i, (k, vv) in enumerate([('Período', '[início a fim]'), ('Horas ao vivo', '[__ h]'), ('Resultado', '[número do painel]'), ('Depoimento', '“[frase autorizada]”')]):
        field(s, 7.0, 1.9 + i * 1.2, 5.6, 1.1, k, vv)
    return p
for fr in ('Agencia', 'Shop'):
    d = f'{AP}/04_Cases_e_Portfolio/{F(fr)}'
    export(case_one(fr), f'{d}/Editaveis/{F(fr)}_Case_1_Pagina_v01.pptx', f'{d}/Finais_Digitais', f'{B}/prev/case1_{fr}', 500)
    export(carrossel(fr), f'{d}/Editaveis/{F(fr)}_Case_Carrossel_5_Telas_v01.pptx', f'{d}/Finais_Digitais', f'{d}/Finais_Digitais/Carrossel_PNG', 1080)
    export(portfolio(fr), f'{d}/Editaveis/{F(fr)}_Pagina_Portfolio_v01.pptx', f'{d}/Finais_Digitais')
print('ok')
