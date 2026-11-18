from deck import *
import content as K
K.LOCAL = f'Cidade, bairro e endereço: {TBD}'
MK = f'{DIST}/02_Midia_Kit'

def two_col_list(s, y, left_title, left, right_title, right, size=12.5):
    text(s, M, y, 5.8, 0.4, left_title, size=13, bold=True); bullets(s, M, y + 0.45, 5.8, 4, left, size=size, gap=5)
    text(s, 7.0, y, 5.6, 0.4, right_title, size=13, bold=True); bullets(s, 7.0, y + 0.45, 5.6, 4, right, size=size, gap=5)

def cards_row(s, y, items, h=2.4, fill=WHITE, icons=None, cols=None):
    n = len(items); cols = cols or n; w = (W - 2 * M - (cols - 1) * 0.25) / cols
    for i, (t, b) in enumerate(items):
        x = M + (i % cols) * (w + 0.25); yy = y + (i // cols) * (h + 0.25)
        card(s, x, yy, w, h, t, b, fill=fill, line=SAND, icon=icons[i] if icons else None)

def pages_entregas(p, front, nx):
    s = page(p, front, 'Entregas', 'O que a marca recebe antes, durante e depois', nx())
    for i, (t, items) in enumerate([('Antes', K.ANTES), ('Durante', K.DURANTE), ('Depois', K.DEPOIS)]):
        x = M + i * 4.05
        box(s, x, 1.9, 3.8, 4.75, fill=WHITE, line=SAND, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
        text(s, x + 0.3, 2.1, 3.2, 0.5, t, size=17, bold=True, font=HEAD, color=RED)
        bullets(s, x + 0.3, 2.75, 3.2, 3.8, items, size=12, gap=6)

def pages_regras(p, front, nx):
    s = page(p, front, 'Como funciona a contratação', 'Conta, horas, equipe e responsabilidades', nx())
    rows = [['Item', 'Como é'], ['Conta da transmissão', K.CONTA], ['Audiência da conta', K.AUDIENCIA], ['Horas ao vivo', K.HORAS],
            ['Preparação e montagem', K.PREPARO], ['Profissionais incluídos', 'Host e moderador em cada live, mais coordenação.'], ['Adicionais e despesas', K.ADICIONAIS]]
    table(s, M, 1.85, 11.9, rows, col_w=[2.8, 9.1], size=10.5, row_h=0.66)
    s = page(p, front, 'Como funciona a contratação', 'O que a marca fornece e quem cuida de quê', nx())
    text(s, M, 1.85, 5.8, 0.4, 'A marca fornece', size=13, bold=True); bullets(s, M, 2.3, 5.8, 4.6, K.CLIENTE_FORNECE, size=11.5, gap=4)
    text(s, 7.0, 1.85, 2.7, 0.4, 'Responsabilidade da marca', size=12, bold=True); bullets(s, 7.0, 2.3, 2.75, 4.3, K.RESP_MARCA, size=11.5, gap=4)
    text(s, 9.95, 1.85, 2.7, 0.4, 'Responsabilidade Zhibo', size=12, bold=True); bullets(s, 9.95, 2.3, 2.7, 4.3, K.RESP_ZHIBO, size=11.5, gap=4)

def page_indicadores(p, front, nx):
    s = page(p, front, 'Acompanhamento de resultados', 'Indicadores e relatórios entregues', nx())
    bullets(s, M, 1.95, 6.0, 4.6, K.INDICADORES, size=13, gap=8)
    table(s, 7.1, 1.95, 5.5, [['Relatório', 'Quando'], ['Da live', 'Dia seguinte, até 12 h'], ['Semanal', 'Toda segunda'], ['Mensal', 'Dia 1, com comissão apurada']],
          col_w=[2.5, 3.0], size=12, row_h=0.5)
    text(s, 7.1, 4.25, 5.5, 1.6, 'GMV é venda bruta atribuída à live, não é lucro. A comissão é calculada sobre o GMV líquido: menos cancelamentos e devoluções.', size=11.5, color=GREY)

def page_cases(p, front, nx, label='Cases e resultados'):
    s = page(p, front, label, 'Resultados comprovados entram aqui', nx())
    box(s, M, 1.9, 11.9, 4.7, fill=WHITE, line=GREY, dash=True)
    text(s, M + 0.4, 2.2, 6.2, 4, [[('Modelo de case', dict(bold=True, size=15))], 'Cliente: ' + TBD, 'Período: ' + TBD, 'Horas transmitidas: ' + TBD,
                                     'Resultados (painel do TikTok Shop): ' + TBD, 'Investimento em anúncios, quando houver: ' + TBD, 'Depoimento autorizado: ' + TBD], size=13, spacing=7)
    text(s, 7.2, 2.2, 5.0, 4, ['A operação começou em novembro de 2026. Os primeiros cases entram depois das lives de teste.',
                               'Regra: só números do painel da plataforma, com autorização da marca.'], size=13, spacing=10, color=GREY)

def page_modalidades(p, front, nx):
    s = page(p, front, 'Modalidades de contratação', 'Comece pelo teste, continue no plano', nx())
    cards_row(s, 1.95, K.MODALIDADES, h=3.3)
    text(s, M, 5.6, 11.9, 0.5, K.NOTA_VALORES, size=13, color=GREY)

def page_contato(p, front, nx, title='Vamos colocar sua marca ao vivo'):
    bgc = {'Institucional': INK, 'Agencia': INK, 'Shop': RED}[front]
    s = slide(p, bgc); image(s, bg_image(front, 'Escuro'), 0, 0, W, H)
    image_fit(s, logo(front, 'Horizontal', 'Branca' if bgc == RED else 'Negativa'), M, M, 4.2, 0.75)
    text(s, M, 1.9, 8, 1.4, title, size=32, bold=True, font=HEAD, color=PAPER, line=1.0)
    contact_block(s, M, 3.6, 8, front, dark=True)

# ------------------------------------------------------------------ Institucional
def institucional():
    p = new_deck(); n = [0]
    def nx(): n[0] += 1; return n[0]
    cover(p, 'Institucional', 'Lives que vendem pela sua marca', 'Planejamento, estúdio, apresentadores e relatório. Do primeiro roteiro ao pedido no carrinho.', 'Apresentação institucional')
    s = page(p, 'Institucional', 'A Zhibo', 'Uma casa de lives que vende pelas marcas', nx())
    text(s, M, 1.95, 6.2, 4.6, ['A marca envia o produto. A Zhibo planeja, transmite e vende ao vivo no TikTok Shop, e entrega o resultado no dia seguinte.',
                               'Zhibo é a palavra em mandarim para “transmissão ao vivo”. Na China, a venda em live virou hábito; no Brasil, o TikTok Shop está crescendo rápido e a maioria das marcas ainda não sabe fazer live.',
                               'Canais: ' + K.CANAIS], size=14, spacing=12)
    photo(s, 7.3, 1.95, 5.3, 4.6, 'Equipe ou estúdio Zhibo em uma live real')
    s = page(p, 'Institucional', 'Duas frentes', 'Zhibo Agência planeja. Zhibo Shop transmite.', nx())
    for i, (f, t, items) in enumerate([('Agencia', 'Zhibo Agência', ['Planejamento das ações e calendário', 'Estudo dos produtos e fichas', 'Roteiros e ofertas', 'Acompanhamento de resultados']),
                                       ('Shop', 'Zhibo Shop', ['Estúdio com cenários personalizáveis', 'Hosts e moderação', 'Transmissão e operação do carrinho', 'Registro de cada live'])]):
        x = M + i * 6.05
        box(s, x, 1.9, 5.85, 4.7, fill=WHITE, line=SAND, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.04)
        box(s, x, 1.9, 5.85, 0.16, fill=FRONTS[f]['accent'])
        image_fit(s, logo(f), x + 0.4, 2.35, 3.6, 0.7)
        bullets(s, x + 0.4, 3.35, 5.0, 3, items, size=14, gap=8)
    s = page(p, 'Institucional', 'Soluções', 'O que fazemos pela marca', nx())
    cards_row(s, 1.9, [('Lives de venda', '2 h por sessão, em grade fixa, na conta da marca.'), ('Vídeos curtos', 'Aquecimento antes da live e cortes depois.'),
                       ('Planejamento', 'Calendário, ofertas, roteiro e fichas de produto.'), ('Relatórios', 'Da live no dia seguinte, semanal e mensal.')],
              h=3.2, icons=[icon('live'), icon('estudio'), icon('roteiro'), icon('relatorio')])
    s = page(p, 'Institucional', 'Estrutura e equipe', 'Quem está na sua live', nx())
    cards_row(s, 1.9, K.EQUIPE, h=2.3)
    bullets(s, M, 4.55, 11.9, 2, ['Estrutura: ' + ', '.join(t.lower() for t, _ in K.ESTRUTURA) + '. Detalhes na apresentação Zhibo Shop.', K.CAPACIDADE, 'Local: ' + K.LOCAL], size=13, gap=8)
    s = page(p, 'Institucional', 'Funcionamento', 'Da primeira conversa à renovação', nx())
    steps = [('1', 'Conversa', 'Entendemos a loja e escolhemos 3 a 5 produtos.'), ('2', 'Onboarding', 'Formulário, acesso à conta, amostras e fichas aprovadas.'),
             ('3', 'Planejamento', 'Agenda, roteiro e ofertas aprovadas.'), ('4', 'Live', 'Transmissão com host e moderador.'),
             ('5', 'Relatório', 'Números no dia seguinte, semanal e mensal.'), ('6', 'Revisão', 'Ajustes e próximo mês.')]
    w = (W - 2 * M - 5 * 0.2) / 6
    for i, (nm, t, b) in enumerate(steps):
        card(s, M + i * (w + 0.2), 2.0, w, 3.6, t, b, fill=WHITE, line=SAND, num=nm)
    s = page(p, 'Institucional', 'Exemplos de projetos', 'Projetos realizados entram aqui', nx())
    for i in range(3): photo(s, M + i * 4.05, 1.9, 3.8, 3.0, f'Projeto {i + 1}: marca, formato da live e período {TBD}')
    text(s, M, 5.15, 11.9, 1, 'Mostre só projetos feitos e autorizados pela marca. Use o modelo de página de portfólio (03_Aplicacoes_da_Marca/04_Cases_e_Portfolio).', size=12, color=GREY)
    page_cases(p, 'Institucional', nx)
    page_modalidades(p, 'Institucional', nx)
    pages_regras(p, 'Institucional', nx)
    page_contato(p, 'Institucional', nx)
    return p

# ------------------------------------------------------------------ Agência
def agencia():
    p = new_deck(); n = [0]
    def nx(): n[0] += 1; return n[0]
    cover(p, 'Agencia', 'Sua marca vendendo ao vivo, com planejamento', 'Estudo de produto, roteiro, ofertas e acompanhamento de resultados para lives de venda no TikTok Shop.', 'Mídia kit · Zhibo Agência')
    s = page(p, 'Agencia', 'O papel da agência', 'Planejamos para a live vender', nx())
    text(s, M, 1.95, 6.2, 4.6, ['A Zhibo Agência cuida de tudo o que vem antes e depois da transmissão: escolha dos produtos, fichas, roteiro, ofertas, calendário e leitura dos resultados.',
                               'A transmissão acontece na Zhibo Shop, com a mesma equipe e o mesmo processo.'], size=14, spacing=12)
    cards_row_s = [('Planejamento das ações', 'Calendário do mês em grade fixa, datas sazonais e produtos foco.'), ('Estudo dos produtos', 'Ficha de cada SKU: benefícios, demonstração, objeções e o que não pode ser dito.')]
    for i, (t, b) in enumerate(cards_row_s): card(s, 7.2, 1.95 + i * 2.35, 5.4, 2.15, t, b, fill=WHITE, line=SAND)
    s = page(p, 'Agencia', 'Serviços', 'O que a agência entrega', nx())
    cards_row(s, 1.9, [('Roteiros', 'Roteiro-base de 2 h com abertura, ciclos por produto, oferta e fechamento.'), ('Campanhas e lives', 'Agenda, plano de ofertas (âncora, relâmpago, kit) e vídeos de aquecimento.'),
                       ('Equipe', 'Host, moderador e coordenação dedicados a cada live.'), ('Resultados', 'Relatórios da live, semanal e mensal, com recomendações.')],
              h=3.3, icons=[icon('roteiro'), icon('agenda'), icon('equipe'), icon('resultado')])
    s = page(p, 'Agencia', 'Processo de execução', 'Como o trabalho anda, semana a semana', nx())
    steps = [('E3', 'Onboarding', 'Formulário, acessos, amostras e fichas aprovadas (D-7 a D-1).'), ('E4', 'Planejamento', 'Agenda, roteiro e ofertas aprovadas até D-3.'),
             ('E5', 'Live', 'Checklist T-20, transmissão e registro.'), ('E6', 'Relatório', 'D+1 até 12 h, semanal na segunda, mensal no dia 1.'), ('E9', 'Revisão mensal', 'Resultado, testes, novos produtos e campanhas.')]
    w = (W - 2 * M - 4 * 0.2) / 5
    for i, (nm, t, b) in enumerate(steps): card(s, M + i * (w + 0.2), 2.0, w, 3.6, t, b, fill=WHITE, line=SAND, num=nm)
    pages_entregas(p, 'Agencia', nx)
    page_indicadores(p, 'Agencia', nx)
    page_cases(p, 'Agencia', nx, 'Cases da agência')
    s = page(p, 'Agencia', 'Pacotes e entregas', 'Pacotes por horas de live por mês', nx())
    table(s, M, 1.95, 11.9, [['Modalidade', 'Horas', 'Inclui', 'Cobrança'],
                             ['Teste (30 dias)', 'Combinado na proposta', 'Planejamento, live, relatórios', 'Só comissão'],
                             ['Plano mensal', '40 h ou 80 h por mês', 'Tudo do teste + revisão mensal', 'Fixo + comissão'],
                             ['Adicionais', 'Sob demanda', 'Vídeos extras, cortes, cenário personalizado', 'Sob orçamento']],
          col_w=[2.6, 2.7, 4.3, 2.3], size=12, row_h=0.6)
    text(s, M, 4.6, 11.9, 0.6, K.NOTA_VALORES, size=13, color=GREY)
    pages_regras(p, 'Agencia', nx)
    page_contato(p, 'Agencia', nx)
    return p

# ------------------------------------------------------------------ Shop
def shop():
    p = new_deck(); n = [0]
    def nx(): n[0] += 1; return n[0]
    cover(p, 'Shop', 'A casa onde sua marca entra ao vivo', 'Estúdio, hosts e operação de lives de venda no TikTok Shop.', 'Mídia kit · Zhibo Shop')
    s = page(p, 'Shop', 'A casa', 'Espaço e localização', nx())
    photo(s, M, 1.9, 7.4, 4.75, 'Foto real do espaço: visão geral do estúdio')
    photo(s, 8.35, 1.9, 4.25, 2.25, 'Foto real: cenário montado')
    text(s, 8.35, 4.4, 4.25, 2.2, [[('Localização', dict(bold=True))], K.LOCAL, '', K.CAPACIDADE], size=12.5, spacing=4)
    s = page(p, 'Shop', 'Cenários', 'Cenários com a cara da sua marca', nx())
    for i in range(3): photo(s, M + i * 4.05, 1.9, 3.8, 2.8, f'Foto real: cenário {i + 1}')
    text(s, M, 4.95, 11.9, 1.6, ['2 a 3 cenários móveis. Personalização com painel, banner da marca ou arco de balões.', 'Cenário personalizado sob orçamento.'], size=13, spacing=6)
    s = page(p, 'Shop', 'Estrutura técnica', 'Equipamentos de cada cenário', nx())
    cards_row(s, 1.9, K.ESTRUTURA, h=2.15, cols=3, icons=[icon(i) for i in ('estudio', 'host', 'iluminacao', 'live', 'produto', 'resultado')])
    s = page(p, 'Shop', 'Equipe', 'Apresentadores e operação', nx())
    cards_row(s, 1.9, K.EQUIPE, h=2.4)
    for i in range(3): photo(s, M + i * 4.05, 4.55, 3.8, 2.05, f'Foto real: host {i + 1}')
    s = page(p, 'Shop', 'Formatos', 'Formatos de live', nx())
    cards_row(s, 1.9, K.FORMATOS, h=3.0)
    s = page(p, 'Shop', 'Etapas', 'Preparação e transmissão', nx())
    w = (W - 2 * M - 3 * 0.2) / 4
    for i, (t, b) in enumerate(K.ETAPAS_LIVE): card(s, M + i * (w + 0.2), 1.95, w, 4.6, t, b, fill=WHITE, line=SAND, num=str(i + 1))
    s = page(p, 'Shop', 'Contratação', 'Horas e sessões', nx())
    table(s, M, 1.95, 11.9, [['Como contratar', 'Formato'], ['Sessão', 'Live de 2 h na conta da marca'], ['Pacote mensal', '40 h ou 80 h por mês, em grade fixa'],
                             ['Teste de 30 dias', 'Sessões semanais, cobrança só por comissão'], ['Adicionais', 'Cenário personalizado, vídeos curtos e cortes']],
          col_w=[3.6, 8.3], size=12.5, row_h=0.6)
    text(s, M, 5.2, 11.9, 0.6, K.NOTA_VALORES, size=13, color=GREY)
    pages_regras(p, 'Shop', nx)
    s = page(p, 'Shop', 'Lives realizadas', 'Exemplos de lives', nx())
    for i in range(3): photo(s, M + i * 4.05, 1.9, 3.8, 3.4, f'Print ou foto de live realizada {i + 1}: marca, data, horas {TBD}')
    text(s, M, 5.55, 11.9, 0.8, 'Só lives realizadas, com autorização da marca. Números do painel da plataforma.', size=12, color=GREY)
    page_contato(p, 'Shop', nx, 'Agende uma live na Zhibo Shop')
    return p

# ------------------------------------------------------------------ one-pagers (A4)
def one_pager(front):
    p = new_deck('A4'); w, h = SIZES['A4']
    s = slide(p, PAPER)
    bgc = INK if front == 'Agencia' else RED
    box(s, 0, 0, w, 3.6, fill=bgc)
    image(s, bg_image(front, 'Escuro', 'Apresentacao_16x9'), 0, 0, w, 3.6) if False else None
    image_fit(s, logo(front, 'Horizontal', 'Negativa' if bgc == INK else 'Branca'), 0.6, 0.55, 3.6, 0.6)
    title = {'Agencia': 'Planejamento e resultado para suas lives de venda', 'Shop': 'Estúdio, hosts e operação para sua marca vender ao vivo'}[front]
    text(s, 0.6, 1.45, 7.0, 1.6, title, size=22, bold=True, font=HEAD, color=PAPER, line=1.0)
    text(s, 0.6, 3.0, 7.0, 0.5, 'TikTok Shop · teste de 30 dias só por comissão', size=11.5, color=GOLD if bgc == INK else PAPER, bold=True)
    photo(s, 0.6, 3.9, 7.07, 2.3, 'Imagem representativa: foto real da casa ou de uma live')
    text(s, 0.6, 6.45, 3.4, 0.4, 'Principais serviços', size=12.5, bold=True)
    svc = {'Agencia': ['Planejamento e calendário', 'Estudo de produto e fichas', 'Roteiros e ofertas', 'Relatórios D+1, semanal e mensal'],
           'Shop': ['Lives de 2 h na conta da marca', 'Host e moderador em cada live', '2 a 3 cenários personalizáveis', 'Relatório no dia seguinte']}[front]
    bullets(s, 0.6, 6.85, 3.4, 2.2, svc, size=10.5, gap=3)
    text(s, 4.25, 6.45, 3.45, 0.4, 'Como trabalhamos', size=12.5, bold=True)
    bullets(s, 4.25, 6.85, 3.45, 2.2, ['Processo com checklist em cada etapa', 'Ficha de produto aprovada pela marca', 'Números do painel da plataforma', 'Diferenciais comprovados: ' + TBD + ' (após os primeiros cases)'], size=10.5, gap=3)
    box(s, 0, 9.55, w, 2.15, fill=INK)
    text(s, 0.6, 9.8, 7, 0.4, 'Fale com o comercial', size=12, bold=True, color=GOLD)
    text(s, 0.6, 10.2, 7, 1.3, ['Felipe Percebão · WhatsApp ' + TBD, 'E-mail ' + TBD + ' · @' + TBD], size=11, color=PAPER, spacing=3)
    return p

out = {}
for name, fn, fr in (('01_Zhibo_Institucional', institucional, 'Institucional'), ('02_Zhibo_Agencia', agencia, 'Agencia'), ('03_Zhibo_Shop', shop, 'Shop')):
    fname = {'Institucional': 'Zhibo_Institucional', 'Agencia': 'Zhibo_Agencia', 'Shop': 'Zhibo_Shop'}[fr] + '_Midia_Kit_v01'
    out[name] = export(fn(), f'{MK}/{name}/Editaveis/{fname}.pptx', f'{MK}/{name}/Finais_Digitais', f'{B}/prev/{name}', 700)
for fr in ('Agencia', 'Shop'):
    fname = FRONTS[fr]['file'] + '_Resumo_Comercial_v01'
    out[fr] = export(one_pager(fr), f'{MK}/04_Resumos_Comerciais/Editaveis/{fname}.pptx', f'{MK}/04_Resumos_Comerciais/Finais_Digitais', f'{MK}/04_Resumos_Comerciais/Finais_Digitais', 1240)
print('ok')
