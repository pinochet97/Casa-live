# 🤝 Comercial e Clientes

**Escopo:** leads, qualificação, propostas, acordos de teste, onboarding, conversão do teste em plano pago e relacionamento (etapas E0 a E3, E8 e E9).

**Regras:** `docs/11-estrutura-comercial.md` (preço, contrato, vendedores, canais; Doc `1tq_zOP7MthS7cTaJ0xAIrZxrZAX4iVswgR9MCoC-1JE`) e `docs/10-playbook-cliente.md` (passo a passo E0 a E9).

**Dados:** planilha "Casa Live — CRM" (Drive, pasta 02), ID `1pyNO4KHIYvxK9u9UO8HJghY4WT6obF5gCSq-XM6RryU`. Cada cliente tem uma pasta em `08 Clientes/<Marca>/` com Acordo, Fichas, Relatórios e Mídia.

## Planilha CRM (criada em 17/11/2026)
Padrão brasileiro (pt_BR, fuso de São Paulo). Nas fórmulas, o separador é `;`.

| Aba | Para quê | Quem preenche |
|---|---|---|
| Como usar | Passo a passo e legenda | — |
| Leads | Uma linha por marca: contato, origem, **Etapa** (lista E0 a E9, Encerrado, Futuro), próxima ação, prazo, responsável, início do teste e **condições do cliente**: tipo de cliente (revenda ou fabricante), comissão do teste, horas mínimas, gestão mensal no contrato, comissão do contrato, início e meses de contrato. Calcula sozinha a nota, a decisão, as datas dos dias 20, 25 e 30 do teste e o fim do contrato | Felipe |
| Qualificação | Checklist de 100 pontos do E1 (limite de nota por critério). Calcula a nota e a decisão (≥ 70 segue; 50 a 69 só com vaga; < 50 recusar) | Felipe |
| Onboarding | Caixas de seleção do E2/E3. Mostra os 3 OKs (Comercial, Conteúdo, Técnico) e "Pronto para a 1ª live" | Duda |
| Painel | Quantidade por etapa, vagas de teste livres (limite 3), nota média, próximas ações vencidas | automático |
| Listas | Opções dos menus: **Responsáveis** e **Taxas de comissão**. São só sugestões de menu: cadastre aqui na primeira linha vazia (taxa com %, ex.: 12%). Também dá para digitar uma taxa direto na linha do cliente | Felipe/Kaio |
| Parâmetros | Notas de corte, limite de testes, dias do teste, **tabela comercial de referência** (teste só por comissão; revenda 8%, fabricante 10% a 12%; contrato de 3 meses e renovações de 6 com gestão de R$ 3.000 antecipada + comissão; multa de 50%; meta de R$ 120 mil de GMV por cliente; 60 h em 22 dias; boleto dia 05, vendedor R$ 40/h (mínimo 3 h) + 2% do GMV da live), lista de etapas e donos. É só referência: nenhuma conta dos clientes depende dela | Kaio/Felipe |

- **ID do lead:** `LEAD-001`, `LEAD-002`… Mesmo ID nas três abas.
- Cabeçalho azul = preencher. Cabeçalho cinza "(auto)" = fórmula, não digitar.
- `LEAD-000` é linha de exemplo nas abas Leads, Qualificação e Onboarding. Fica fora das contas do Painel. Apagar quando entrar o primeiro lead real.
- **Taxa por cliente:** as colunas de comissão da aba Leads (teste e mês 2) guardam a taxa combinada com cada cliente, digitada ou escolhida no menu da aba Listas. Não existe taxa padrão automática: mudar a aba Listas ou Parâmetros não altera nenhum cliente já cadastrado.
- Donos das etapas na aba Parâmetros seguem a decisão de 17/11 (Duda na operação, Felipe no comercial).

## Como usar
- "Novo lead: <marca>, <contato>, <@tiktok>, <origem>" → o Claude cadastra o lead (`LEAD-NNN`) e sugere a mensagem M1.
- "Qualificar <marca>" → roda o checklist de 100 pontos.
- "Fechar teste com <marca>" → gera a proposta, o acordo de teste, a pasta do cliente e o formulário de onboarding.

## Documentos para aprovação
- `areas/comercial/estrutura-comercial-aprovacao-2026-11-19.pdf` (cópia no Drive, pasta 02, ID `1-uipKJViPI9YY04dC-bcc-c-p9aJajM8`): resumo da estrutura comercial para Kaio e Felipe assinarem.

## Modelos (pasta `areas/comercial/modelos/` e Drive, pasta 02)
| Modelo | Editar (Google Doc) | PDF |
|---|---|---|
| Proposta comercial para lojista | `18-E0oBI6T_1I5X9TO0NLZ9JVMjQLh_kO4SVTsuyYdj0` | `1AZAniaJpBp-hH1JH3GaMOFDdZDSfxBaV` |
| Proposta e contrato do vendedor de live (minuta) | `1J269NPnJeX8UUeDs4T145rEMdCjBnGfCESEtrZHI1eE` | `1WBpqV0qq-mLzcTC4p98vlTu2HB4MVFfJ` |

- Fonte: `proposta-lojista.html` e `contrato-vendedor.html` (estilo em `_estilo.css`). Ao mudar o modelo, gerar o PDF de novo e atualizar o Doc.
- Campos em amarelo são preenchidos por cliente. Na proposta do lojista, a taxa `[X]%` segue o tipo de cliente: revenda 8%, fabricante 10% a 12%.
- A proposta do lojista não mostra números internos (pagamento do vendedor, margem).
- O contrato do vendedor é **minuta**: revisar com advogado e contador. Campos ainda a definir: GMV bruto ou líquido para os 2%, pagamento se a marca atrasar, live encerrada antes de 3 h, formato da nota (MEI ou RPA).

## Pendências da área
- [ ] Responder os itens [A DEFINIR] de `docs/11-estrutura-comercial.md` (multa, vendedor, entrega de horas).
- [ ] Advogado: revisar multa e contrato do vendedor freelancer.
- [ ] Modelo do acordo de teste e da proposta (M2) em arquivo pronto para assinatura.
- [ ] Formulário de onboarding do cliente (Google Forms) ligado à aba Onboarding.
- [ ] Landing page + campanha de Meta Ads (sem prospecção fria).
