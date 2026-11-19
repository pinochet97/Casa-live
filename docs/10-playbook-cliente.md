# 10 — Playbook do Cliente (do 1º contato à renovação)

> O que fazer, exatamente, quando chega um cliente novo. Cada etapa tem dono, checklist, saída obrigatória, prazo e automação.
> Status do cliente no CRM = código da etapa (E0…E9).

## Visão geral
| Etapa | Nome | Dono | Saída obrigatória | Prazo |
|---|---|---|---|---|
| E0 | Lead | Felipe | Lead no CRM com origem | no mesmo dia |
| E1 | Qualificação | Felipe | Checklist preenchido + nota ≥ 70 | até 2 dias |
| E2 | Fechamento do teste | Felipe | Acordo de teste assinado | até 3 dias |
| E3 | Onboarding | Duda | Formulário + acessos + amostras + fichas aprovadas | D-7 a D-1 |
| E4 | Planejamento | Duda | Agenda do mês + roteiro + ofertas | D-3 |
| E5 | Live | Host + moderador | Live feita + registro preenchido | dia da live |
| E6 | Relatório | Duda | Relatório da live (D+1), semanal e mensal | D+1 / segunda / dia 1 |
| E7 | Cobrança | Duda | Fatura + nota + pagamento | até o dia 5 |
| E8 | Conversão (fim do teste) | Felipe | Cliente no contrato ou encerrado | dia 25 a 30 do teste |
| E9 | Ativo / renovação | Felipe + Duda | Revisão mensal + upsell | mensal |

---

## E0 — Lead
**Entrada:** cadastro na landing page (vindo de conteúdo, Meta Ads ou indicação), mensagem nos perfis, contatos do Felipe. Não fazemos prospecção fria.
1. Cadastrar no CRM: marca, contato, WhatsApp, @ do TikTok, link da loja, categoria, origem, quem trouxe.
2. Olhar rapidamente a loja: tem TikTok Shop? Quantos produtos? Já faz live? Quantos vendidos?
3. Mandar a mensagem de primeiro contato (modelo M1).

**Automação:** formulário "Quero live" na bio da agência → linha no CRM → aviso no WhatsApp do Felipe.

## E1 — Qualificação (call de 20 min)
**Checklist de qualificação (nota até 100)**
| Critério | Peso | Como avaliar |
|---|---|---|
| Loja TikTok Shop aprovada, produto no carrinho | 25 | Ver a loja. Se não tiver, só entra pela rota de afiliado ou fica para depois |
| Produto bom de demonstrar ao vivo | 20 | Visual, uso fácil de mostrar, "efeito uau" |
| Preço de impulso e margem para oferta relâmpago | 15 | Ticket até cerca de R$ 150 e desconto possível na live |
| Estoque e capacidade de entrega | 15 | Aguenta 100 ou mais pedidos numa live? Envia em até 2 dias? |
| Responsividade (alguém disponível na live) | 10 | Decisor acessível |
| Potencial de virar contrato (meta: R$ 120 mil de GMV por mês nas nossas lives) | 15 | Faturamento atual, ambição, budget |

- **≥ 70:** segue para E2.
- **50–69:** entra só se tivermos vaga.
- **< 50:** recusar com educação e deixar na lista de "futuro".

**Perguntas da call:**
- O que vende melhor hoje?
- Quanto fatura no TikTok Shop?
- Qual é o preço mínimo que topa na live?
- Quem fica de plantão na live?
- Como é a logística?
- Já fez live? Como foi?

**Saída:** nota no CRM + decisão + os 3 a 5 SKUs candidatos.

## E2 — Fechamento do teste
1. Enviar a proposta de teste (modelo M2): 30 dias só por comissão (revenda 8%, fabricante 10% a 12%, pela margem do cliente), mínimo de 60 h de live em pelo menos 22 dias, e o aviso de que, aprovado o teste, segue contrato de 3 meses (depois, renovações de 6) com gestão de R$ 3.000 antecipada + comissão. Registrar no CRM (aba Leads) a comissão combinada. Ficam gravadas só na linha desse cliente.
2. Enviar o **acordo de teste** (modelo em `40-financeiro-juridico`) por assinatura digital.
3. Criar a pasta do cliente no Drive: `08 Clientes/<Marca>/` com Acordo, Fichas, Relatórios e Mídia.
4. Criar o grupo de WhatsApp "<Marca> x Casa Live", com o decisor e o responsável pela operação.

**Saída:** acordo assinado → CRM em E3.
**Automação:** status "E2 assinado" → cria a pasta, o grupo e envia o formulário de onboarding.

## E3 — Onboarding (D-7 a D-1)
**1. Formulário de onboarding** (o cliente preenche)
- Dados da empresa: razão social, CNPJ, contato financeiro.
- Loja: link e @ da conta TikTok.
- Produtos foco (3 a 5): nome, SKU/ID, preço normal, **preço mínimo de live**, estoque, diferenciais, perguntas frequentes, o que **não** pode ser dito.
- Público-alvo, tom da marca, concorrentes.
- Datas importantes: lançamentos, promoções, datas comemorativas.
- Logo e materiais de marca.
- Autorização de uso de imagem e dos cortes.

**2. Acessos**
- O cliente adiciona o nosso usuário como membro da equipe na conta e na loja do TikTok Shop, com o papel adequado para operar a live. [A VERIFICAR: nomes dos papéis no Seller Center]
- Testar o login e a criação de uma live de teste, sem transmitir.
- Registrar no CRM quem concedeu e quando. Nunca pedir senha pessoal.

**3. Amostras**
- O cliente envia pelo menos 1 unidade de cada SKU (2 se for consumível).
- Conferir na chegada, fotografar e registrar na planilha **Casa Live — Agenda**, aba **Amostras** (ID AMO-001, onde está guardada, se volta para o cliente).

**4. Ficha de produto** (uma por SKU, modelo em `20-operacao-live`)
- Benefícios, modo de uso, perguntas e respostas, objeções, frases proibidas, preço e oferta.
- **O cliente aprova por escrito.**

**5. Kickoff (call de 30 min):** apresentar a agenda, o roteiro, a ficha e o fluxo do dia da live. Explicar o relatório.

**Saída:** os 3 "OK" registrados no CRM, sem os quais a live não acontece:
- ✅ **Comercial:** acordo assinado.
- ✅ **Conteúdo:** fichas aprovadas.
- ✅ **Técnico:** acesso testado + amostras recebidas.

## E4 — Planejamento
1. **Agenda do mês** na planilha **Casa Live — Agenda** (aba Agenda) e no Google Agenda: ID da live (CL-AAAA-NNN), dia, horário, duração (2 h), cenário, host, moderador, produtos e ofertas.
   - Grade fixa: o mesmo dia e horário toda semana, para formar audiência.
   - Antes de confirmar, conferir as colunas de alerta (cenário ocupado, pessoa em duas lives, acima do limite). Nenhuma pode estar em vermelho.
   - Na véspera, marcar o checklist D-1 na própria linha da live.
2. **Plano de ofertas por live:** produto âncora, promoção relâmpago, kit e brinde. Aprovado pelo cliente até D-3.
3. **Roteiro** a partir do roteiro-base, com a ordem dos produtos e os ganchos.
4. **Aquecimento:** 1 a 3 vídeos curtos anunciando a live (na conta do cliente e na nossa).

**Saída:** agenda publicada + roteiro + ofertas aprovadas.
**Automação:** agenda → convite no Google Agenda para a equipe + mensagem para o cliente em D-1 ("live amanhã às 14h").

## E5 — Dia da live
Siga o **Manual da Live** em `20-operacao-live`: checklist T-20, condução, incidentes e fechamento.
**Saída:** linha na planilha **Casa Live — Registro de Lives** (aba Registro), com o mesmo ID da Agenda e status da live mudado para Realizada na Agenda. Campos principais:
- início e fim;
- espectadores;
- pico;
- GMV;
- pedidos;
- itens;
- produto campeão;
- incidentes;
- prints do painel.

## E6 — Relatórios
| Relatório | Quando | Para quem | Conteúdo |
|---|---|---|---|
| Da live | D+1 até 12h | Cliente | Números da live, destaques, o que muda na próxima |
| Semanal | Segunda | Cliente + interno | Soma da semana, evolução, plano da semana |
| Mensal | Dia 1 | Cliente | Resultado do mês, comissão apurada, recomendações, proposta |

Diário (todo dia de live, no grupo do cliente): vídeo da live acontecendo, print do GMV do dia, horas de live do dia e relatório dos itens vendidos. Modelos e indicadores em `30-relatorios-kpis`.
**Automação:** registro preenchido → Claude gera o texto do relatório → PDF ou mensagem → envio no grupo.

## E7 — Cobrança
1. No dia 1, apurar a comissão do mês anterior (GMV das nossas lives menos cancelamentos e devoluções, vezes a taxa do cliente: coluna "Comissão do teste (%)" ou "Comissão contrato 6 meses (%)"). Usar a exportação do painel. A gestão do contrato (coluna "Gestão mensal no contrato (R$)") é cobrada antecipada, no início de cada mês.
2. Enviar o demonstrativo para conferência. O cliente tem 2 dias para contestar.
3. Emitir a cobrança (Pix/boleto) e a nota fiscal de serviço. Vencimento no dia 5.
4. Lembretes automáticos: D-1, no vencimento e D+3.
5. Boleto não pago no vencimento: as lives são interrompidas imediatamente até regularizar (regra do contrato). Com o pagamento recebido, pagar os vendedores de live no dia 05: R$ 40 por hora (mínimo de 3 h) e o bônus por meta de cada live (contrato; no teste, as lives são feitas pelos sócios).

## E8 — Conversão (fim do teste)
1. **Dia 20 do teste:** fazer a análise interna. Vale continuar? O GMV justifica? O cliente é bom de trabalhar?
2. **Dia 25:** reunião de resultado com o cliente (relatório do teste + proposta do contrato de 3 meses: gestão, horas e comissão). Registrar no CRM as condições aceitas e a data de início do contrato.
3. **Dia 30:** assinar o contrato de 3 meses (depois, renovações de 6). Se não fechar, encerrar com educação, pedir depoimento e manter na lista.

**Argumento:** os números do teste. Por exemplo: "Em 8 lives vendemos R$ X. Com 40 h/mês projetamos R$ Y."

## E9 — Cliente ativo e renovação
- **Revisão mensal de 30 min:**
  - resultado;
  - o que testar;
  - novos produtos;
  - campanhas sazonais.
- **Upsell:**
  - mais horas;
  - vídeos curtos extras;
  - Shopee Live;
  - criadores da Vyre (fase 2).
- **Sinais de risco de perder o cliente:**
  - GMV caindo 3 semanas seguidas;
  - atraso de pagamento;
  - cliente demora a responder.
- **Ação:** reunião em até 48 h.

---

## Modelos de mensagem
**M1 — Primeiro contato**
> Oi, [nome]! Sou o Felipe, da [Casa Live]. Recebi o cadastro da [marca] e acho que os produtos de vocês vendem muito em live. A gente opera lives de venda para marcas: estúdio, apresentador, moderação e relatório. Começamos com um teste de 30 dias, com vendedor exclusivo da marca e no mínimo 60 horas de live no mês. Posso te mostrar em 15 minutos como funciona?

**M2 — Proposta de teste**
> Fechado, [nome]! Proposta do teste:
> • 30 dias de teste, com no mínimo 60 h de live em pelo menos 22 dias, na conta de vocês
> • Studio da marca, vendedor exclusivo, roteiro e acompanhamento diário no grupo (vídeo da live, GMV, horas e itens vendidos)
> • Comissão de [X]% sobre as vendas das lives (líquidas de cancelamentos e devoluções)
> • Aprovado o teste, seguimos com contrato de 3 meses (depois, renovações de 6): gestão de R$ 3.000/mês + comissão
> Te mando o acordo para assinar e o formulário de cadastro dos produtos.

**M3 — Lembrete D-1**
> Amanhã tem live da [marca] às [hora]! Produtos: [lista]. Oferta: [oferta]. Preciso de alguém de vocês disponível no WhatsApp durante a live para estoque e preço. 🚀

**M4 — Relatório D+1** (gerado automaticamente; ver `30-relatorios-kpis`)
