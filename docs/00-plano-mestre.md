# Casa Live — Plano Mestre

> Versão 1, de 17/11/2026. Este é o documento-mãe da operação: tudo começa aqui e aponta para os documentos detalhados.
> Legenda: **[DECIDIDO]** = combinado entre os sócios · **[PROPOSTA]** = sugestão para aprovar · **[A VERIFICAR]** = depende de regra da plataforma, do contador ou de cotação.

---

## 1. A ideia
**Uma casa de lives que vende pelas marcas.** A marca manda o produto e nós fazemos as lives de venda e os vídeos curtos no TikTok Shop. Cuidamos de estúdio, apresentador (host), moderação, roteiro e relatório. No teste de 30 dias cobramos só comissão (8% a 12%). Aprovado o teste, o contrato de 6 meses tem gestão mensal de R$ 3.000 mais a comissão.

**Por que agora:**
- O TikTok Shop está crescendo rápido no Brasil e a maioria das marcas não sabe fazer live.
- Montar a estrutura internamente custa caro e é difícil para elas.
- A LiveHouse comprova que existe demanda e preço: R$ 4 mil + 10% por 80 h.

**Diferencial que vamos construir:**
1. **Operação com processo e dados.** Cada live vira registro, relatório e aprendizado. O cliente vê o resultado no dia seguinte.
2. **Automação desde o início.** Menos trabalho manual, escala com equipe enxuta.
3. **Duas formas de ganhar comissão:** a live na conta da marca e os vídeos e lives na nossa conta como afiliado.
4. **Gestão de R$ 3.000** no contrato (a LiveHouse cobra R$ 4 mil por 80 h), com teste de 30 dias só por comissão e vendedor exclusivo da marca.

**Visão de 12 meses [PROPOSTA]:**
- Casa própria com 3 ou mais estúdios.
- 10 ou mais marcas no fixo.
- Hosts contratados e treinados (captados via Vyre).
- Plataforma própria de gestão.
- Marcas próprias vendidas pela casa (cosméticos masculinos).

## 2. Sociedade e papéis [DECIDIDO]
| Quem | Papel | Responsável por |
|---|---|---|
| **Felipe** | Comercial | Prospecção, fechamento, relacionamento com as marcas, host, CNPJ (titular) |
| **Duda** (pelo lado do Kaio) | **Operação (tudo do dia a dia)** | Onboarding, agenda, fichas, lives, relatórios, cobrança, controles, host |
| **Kaio** | Estratégia e tecnologia | Plano, decisões, automações, integrações e APIs, dados, host |
| Primo do Kaio, amigos | Hosts e moderadores eventuais | Cobrir escala |

> ⚠️ **Atenção jurídica:** o CNPJ está só em nome do Felipe. Até o Kaio entrar no contrato social, assinar um **acordo de sócios** que defina % de participação, divisão de lucro, quem decide o quê, aportes, saída de sócio e propriedade de marca, contas e clientes. Detalhes em `40-financeiro-juridico`.

## 3. Modelo comercial [DECIDIDO]
| Fase do cliente | Cobrança |
|---|---|
| **Teste (30 dias)** [DECIDIDO] | **Só comissão de 8% a 12%** (negociada e gravada por cliente) sobre as vendas das nossas lives, líquidas de cancelamentos e devoluções |
| **Contrato de 6 meses (teste aprovado)** [DECIDIDO] | Gestão de R$ 3.000 + comissão de 8% a 12%. Multa se o cliente cancelar: valor integral dos meses restantes. Sem multa se a Casa não entregar as horas |

**O que está incluso:** no mínimo 60 h de live por mês em pelo menos 22 dias, vendedor exclusivo da marca, studio da marca, vários perfis de vendedores para teste, plataforma de UGC e lojas de vendedores afiliados. As condições de cada cliente ficam no CRM (aba Leads) e no contrato dele. Detalhes de contrato, vendedores e canais em 11-estrutura-comercial.

Adicionais (vídeos curtos extras, cortes, cenário personalizado): sob orçamento.

## 4. Mapa da operação
```
 ATRAIR → QUALIFICAR → FECHAR TESTE → ONBOARDING → PLANEJAR → LIVE → RELATAR → COBRAR → CONVERTER/RENOVAR
   E0        E1            E2             E3           E4       E5      E6        E7          E8/E9
```
Cada etapa tem dono, entrada, checklist, saída, prazo (SLA), modelo de mensagem e automação. Tudo isso está em **`10-playbook-cliente`**.

Processos de apoio (internos):
- **Estúdio e equipamentos:** montagem, manutenção, checklist técnico (`20-operacao-live`)
- **Hosts:** recrutamento, teste, treinamento, escala, avaliação (`20-operacao-live`)
- **Conteúdo:** vídeos curtos e cortes para os clientes e para a nossa conta (`20-operacao-live`)
- **Dados e relatórios:** KPIs, relatório por live, semanal e mensal, painel interno (`30-relatorios-kpis`)
- **Financeiro e jurídico:** custos, aportes, comissão, notas, contratos (`40-financeiro-juridico`)
- **Automação:** ferramentas, integrações, APIs e roadmap técnico (`50-automacao-integracoes`)
- **Marketing da agência:** perfis próprios, prova social, captação de marcas (seção 7)

## 5. Estrutura do Google Drive
```
Casa Live/
├── 00 Comece aqui — Plano Mestre          ← este documento
├── 01 Estratégia/                          (plano de validação, diagnóstico, decisões)
├── 02 Comercial/                           (playbook do cliente, propostas, contratos, modelos de mensagem)
├── 03 Operação/                            (manual de live, roteiros, fichas de produto, estúdio, hosts)
├── 04 Dados e Relatórios/                  (KPIs, modelos de relatório, planilhas de controle)
├── 05 Financeiro e Jurídico/               (custos, aportes, comissões, CNPJ, acordo de sócios)
├── 06 Automação e Integrações/             (arquitetura, ferramentas, APIs)
├── 07 Marketing/                           (perfis da agência, conteúdo, cases)
├── 08 Clientes/                            (uma pasta por cliente: acordo, fichas, relatórios)
└── 99 Fontes/                              (transcrições, briefing, PDFs originais)
```
O repositório GitHub `casa-live` guarda a mesma documentação em Markdown, para o Claude ter o contexto completo em toda sessão.

## 6. Roadmap
### Fase 0 — Estrutura mínima (17/11 a 23/11)
- [ ] Documentação e processos (este plano) ✅ em andamento
- [ ] Planilhas: CRM, agenda, registro de lives, financeiro
- [ ] Formulário de onboarding do cliente
- [ ] Modelos: acordo de teste, mensagens, ficha de produto, relatório
- [ ] Estúdio montado na sexta (20/11) + ensaio de 30 min
- [ ] Contas da agência criadas (TikTok + Instagram) e primeiros vídeos
- [ ] Acordo de sócios em rascunho; CNPJ em andamento

### Fase 1 — Validação (24/11 a 31/12)
- [ ] 3 clientes de teste com lives semanais. **Black Friday (27/11) e Natal** como primeiras campanhas
- [ ] Relatório por live em D+1 e semanal toda segunda
- [ ] Primeiras automações: formulário → CRM, agenda → lembretes, registro de live → relatório
- [ ] Fechamento do teste de cada cliente e contrato de 6 meses

### Fase 2 — Recorrência (jan a fev/2027)
- [ ] Converter 3 clientes de teste para o contrato de 6 meses. Meta: 5 pagantes
- [ ] O Felipe em tempo integral (desde o fim de dezembro)
- [ ] Cobrança automatizada (Pix/boleto + nota fiscal)
- [ ] Integração com a API do TikTok Shop para puxar vendas automaticamente [A VERIFICAR]
- [ ] Captação dos primeiros hosts externos via Vyre

### Fase 3 — Escala (a partir de mar/2027)
Só avança se atingir os critérios abaixo.
- **Casa alugada:** pelo menos 6 clientes pagantes por 2 meses e caixa para 3 meses de aluguel
- **Host contratado:** ocupação acima de 75% da capacidade dos sócios por 4 semanas
- **Segundo estúdio simultâneo:** agenda com conflito de horário recorrente
- Plataforma própria (evolução da Central Marketplaces) e marca própria de cosméticos

## 7. Marketing da agência
- **Perfis próprios** (TikTok + Instagram), criados do zero. Não comprar conta, porque isso viola as regras do TikTok.
- **Linhas de conteúdo:**
  - bastidores da casa;
  - cortes das lives;
  - antes e depois dos clientes (com autorização);
  - série "construindo uma casa de lives do zero".
- **Captação de leads quentes** (sem prospecção fria):
  - conteúdo e Meta Ads levando para a landing page com cadastro;
  - indicações (Gustavo, contatos da fábrica), pelo mesmo cadastro;
  - o Felipe analisa o cadastro e só entra em contato se fizer sentido.
- **Prova social:** cada cliente de teste vira um case com números. É o principal ativo para vender o contrato de 6 meses.

## 8. Governança
- **Reunião semanal de 45 min (segunda):**
  - pipeline comercial;
  - lives da semana;
  - incidentes;
  - números;
  - caixa;
  - decisões.
  - Termina com dono, ação e prazo.
- **Decisões** registradas em `docs/decisoes.md` (GitHub) e na pasta 01 Estratégia.
- **Custos:** o Kaio manda cada custo para o Claude, que registra na planilha financeira com quem pagou. O acerto entre os sócios é feito quando houver receita.

## 9. Metas da validação (até 31/12) [PROPOSTA]
| Indicador | Meta |
|---|---|
| Clientes em teste | 3 |
| Lives realizadas | 60 h e 22 dias de live por cliente por mês (mínimo do contrato) |
| Relatórios entregues em D+1 | 100% |
| GMV médio por live | Medir. Definir a meta depois das 5 primeiras |
| Clientes que aceitam o contrato de 6 meses | 2 de 3 |
| Seguidores na conta TikTok da agência | Medir |

## 10. Riscos principais
| Risco | Mitigação |
|---|---|
| A live vende pouco no teste (pouca comissão para a Casa e para o vendedor) | Qualificar bem o cliente, rota de afiliado em paralelo, limite de 3 clientes |
| O cliente não paga a comissão | Acordo escrito, dados do painel conferidos juntos, pagamento em até 5 dias |
| Conta do cliente penalizada por erro na live | Ficha do produto aprovada, frases proibidas, checklist T-20 |
| Capacidade dos sócios (o Felipe empregado até dezembro) | 60 h por cliente (mínimo do contrato), comunidade de vendedores freelancers, grade fixa |
| Sociedade informal | Acordo de sócios antes da primeira receita |
| Dependência do TikTok | Depois, levar os clientes também para a Shopee Live e o Mercado Livre |

## Documentos detalhados
- `10-playbook-cliente`: passo a passo de cada cliente, do 1º contato à renovação
- `20-operacao-live`: estúdio, hosts, roteiro, checklist, incidentes, vídeos curtos
- `30-relatorios-kpis`: indicadores, modelos de relatório e painel
- `40-financeiro-juridico`: custos, comissão, cobrança, notas, CNPJ, acordo de sócios
- `50-automacao-integracoes`: ferramentas, APIs e roadmap de automação
