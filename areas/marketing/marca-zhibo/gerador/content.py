"""Factual commercial content, taken from docs/ (plano mestre, playbook, operação, relatórios).
Anything not decided is marked [A PREENCHER] or [A CONFIRMAR]."""
TBD = '[A PREENCHER]'
CONF = '[A CONFIRMAR]'

CANAIS = 'TikTok Shop (foco atual). Shopee e Mercado Livre na sequência.'
CONTA = ('Na conta da marca no TikTok Shop: a Zhibo entra como membro da equipe, com acesso de operação. Nunca pedimos senha. '
         'Quando combinado, também na conta Zhibo, como afiliada.')
AUDIENCIA = f'Audiência da conta usada: informada na proposta quando fizer parte da contratação e houver dados. {TBD}'
HORAS = 'Lives de 2 h, em grade fixa (mesmo dia e horário toda semana). Contamos as horas efetivamente ao vivo.'
PREPARO = f'Preparação incluída no serviço: fichas de produto, roteiro, plano de ofertas e checklist técnico antes de cada live. {CONF} se a montagem conta ou não nas horas contratadas.'
EQUIPE = [('Host', 'Apresenta, demonstra, conversa com o público e puxa a oferta.'),
          ('Moderador e operador', 'Fixa o produto no carrinho, lança a promoção relâmpago, responde o chat, cuida de som e imagem e fala com a marca no WhatsApp.'),
          ('Coordenação', 'Agenda, briefing, fichas e relatórios.')]
ANTES = ['Onboarding: formulário, acessos testados e amostras recebidas', 'Ficha de cada produto, aprovada por escrito pela marca',
         'Agenda do mês e plano de ofertas aprovado até 3 dias antes', 'Roteiro da live', '1 a 3 vídeos curtos de aquecimento']
DURANTE = ['Live de 2 h com ciclos de 20 a 25 min por produto', 'Demonstração em uso e respostas ao chat',
           '1 a 2 promoções relâmpago nos picos de audiência', 'Contato com a marca no WhatsApp para estoque e preço']
DEPOIS = ['Relatório da live no dia seguinte, até 12 h', 'Relatório semanal toda segunda', 'Relatório mensal no dia 1, com comissão apurada',
          '2 a 3 momentos marcados para cortes']
ADICIONAIS = f'Vídeos curtos extras, cortes e cenário personalizado: sob orçamento. Outras despesas (frete de amostras, brindes): {TBD}'
CLIENTE_FORNECE = ['Dados da empresa e contato financeiro', 'Link da loja e @ da conta TikTok', 'Produtos foco (3 a 5): SKU, preço normal, preço mínimo de live, estoque, diferenciais, perguntas frequentes e o que não pode ser dito',
                   'Acesso à conta como membro da equipe', 'Amostras: 1 unidade por SKU (2 se for consumível)', 'Logo e materiais de marca', 'Autorização de uso de imagem e dos cortes',
                   'Uma pessoa disponível no WhatsApp durante a live']
RESP_MARCA = ['Estoque e prazo de envio', 'Preços e ofertas aprovados', 'Processamento dos pedidos e entrega', 'Atendimento pós-venda, trocas e devoluções']
RESP_ZHIBO = ['Condução da live conforme a ficha aprovada', 'Operação do carrinho e das ofertas aprovadas', 'Registro de cada live e incidentes', 'Relatórios e recomendações']
INDICADORES = ['Espectadores, pico e tempo médio de visualização', 'Cliques no produto, pedidos e itens vendidos', 'GMV (vendas brutas atribuídas à live)',
               'Conversão (pedidos ÷ espectadores) e GPM (vendas por mil espectadores)', 'Vendas por hora e produto campeão']
MODALIDADES = [('Teste de 30 dias', 'Só comissão sobre as vendas das lives, líquidas de cancelamentos e devoluções. A marca só paga se vender.'),
               ('Plano mensal', 'A partir do 2º mês: valor fixo + comissão, por pacote de horas de live por mês.'),
               ('Adicionais', 'Vídeos curtos extras, cortes e cenário personalizado, sob orçamento.')]
NOTA_VALORES = 'Valores e condições de cada marca ficam na proposta comercial.'
ESTRUTURA = [('Cenários', '2 a 3 cenários móveis, personalizáveis com painel, banner da marca ou arco de balões.'),
             ('Áudio', 'Microfone de lapela sem fio. O som pesa mais que a imagem.'),
             ('Luz', 'Painéis LED reguláveis ou ring light com luz de preenchimento.'),
             ('Transmissão', 'Celular em tripé firme, ligado na tomada; tablet ou notebook para chat, painel e roteiro.'),
             ('Produto', 'Bancada e suporte para close de produto.'),
             ('Internet', 'Upload testado e 4G de reserva.')]
CAPACIDADE = 'Com a equipe atual, até 2 lives simultâneas. Grade fixa por marca.'
ETAPAS_LIVE = [('D-1', 'Ofertas aprovadas, roteiro pronto, amostras separadas, equipe confirmada, aquecimento postado, marca avisada.'),
               ('T-20 min', 'Login na conta certa, produtos e preços conferidos, relâmpago configurado, som, luz e internet testados.'),
               ('Ao vivo', 'Abertura, ciclos por produto, relâmpago nos picos, fechamento com a próxima live anunciada.'),
               ('Depois', 'Painel exportado, registro preenchido, amostras guardadas, cortes marcados, relatório em D+1.')]
FORMATOS = [('Live de venda', '2 h, 5 ciclos de produto, oferta com preço na tela e relâmpago.'),
            ('Lançamento', 'Produto novo apresentado com demonstração e oferta de estreia.'),
            ('Datas sazonais', 'Black Friday, Natal e campanhas da marca.'),
            ('Vídeos curtos', 'Aquecimento antes da live e cortes depois.')]
LOCAL = f'São Paulo, SP. Endereço e bairro: {TBD}'
