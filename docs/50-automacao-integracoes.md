# 50 — Automação e Integrações

> Princípio: **primeiro o processo manual bem definido, depois automatizar o que se repete.** Cada automação tem um gatilho, uma ação e um registro.

## 1. Arquitetura por fase
### Fase 0–1 (agora): Google Workspace + Claude
```
Google Forms (lead, onboarding) ──► Google Sheets (CRM, Agenda, Registro de Lives, Financeiro)
                                         │
                       Apps Script / n8n ┼──► Google Agenda (lives) ──► lembretes
                                         ├──► Google Drive (pasta do cliente, relatórios em Docs/PDF)
                                         ├──► Claude API (texto de relatório, roteiro, fichas, análise)
                                         └──► WhatsApp (avisos e relatórios)
```
- **Banco de dados:** Google Sheets, uma planilha com abas e IDs padronizados (CLI-001, CL-2026-001).
- **Orquestração:** [DECIDIDO 17/11] na Fase 0, **Google Apps Script** (projeto "Casa Live — Automações"). O n8n (self-hosted ou cloud) entra quando houver WhatsApp API ou Claude API (A3, A5).
- **Avisos:** [DECIDIDO 17/11] por e-mail até existir o número da empresa na WhatsApp Cloud API.
- **IA:** Claude, para gerar relatórios, roteiros, fichas de produto, roteiros de vídeo curto e análises.

### Fase 2 (jan–fev): integrações de dados e cobrança
- **TikTok Shop Open API** (Partner Center): app de serviço autorizado pelo seller para ler pedidos, produtos e finanças da loja do cliente. [A VERIFICAR: disponibilidade no Brasil, processo de aprovação do app, se existe endpoint de métricas de LIVE ou apenas de pedidos; se não existir, as métricas de live continuam por exportação ou print.]
- **Asaas API:** cobrança Pix/boleto + NFS-e + webhooks de pagamento → aba Receitas.
- **WhatsApp Business Platform (Cloud API):** mensagens com modelos aprovados (lembretes, relatórios). Exige número próprio da empresa e Meta Business verificado.
- **Assinatura digital (ZapSign ou Autentique API):** envio do acordo e webhook de "assinado" → muda o status no CRM.
- **Looker Studio:** painel conectado às planilhas.

### Fase 3: plataforma própria
Migrar de Sheets para banco de dados (Postgres/Supabase) e app próprio: agenda, sessões, casting e resultado. É o MVP descrito no plano Vyre, e o embrião da Central Marketplaces.

## 2. Catálogo de automações (por prioridade)
| # | Gatilho | Ação | Fase | Ferramenta |
|---|---|---|---|---|
| A1 | Formulário "Quero live" enviado | Cria o lead no CRM (E0) + avisa o Felipe (e-mail agora, WhatsApp na fase 2) | 0 | Forms + Apps Script |
| A2 | CRM muda para "E3 Onboarding" (acordo assinado) | Cria a pasta do cliente em 08 Clientes (Acordo, Fichas, Relatórios, Mídia) + avisa a Duda. Formulário de onboarding fica para a A3 | 1 | Apps Script |
| A3 | Formulário de onboarding enviado | Gera as **fichas de produto** em rascunho com o Claude a partir das respostas → Doc para o cliente aprovar | 1 | n8n + Claude API |
| A4 | Live criada na Agenda | Convite para a equipe + lembrete para o cliente em D-1 + checklist T-20 para o moderador | 1 | Google Agenda + n8n |
| A5 | Registro de Live preenchido | Claude escreve o **relatório D+1** → envia ao cliente | 1 | n8n + Claude API |
| A6 | Toda segunda, 8h | Relatório semanal por cliente + painel interno + pauta da reunião | 1 | n8n + Claude |
| A7 | Dia 1 do mês | Apura a comissão, gera o demonstrativo e o relatório mensal | 1 | Apps Script + Claude |
| A8 | Demonstrativo aprovado | Cria a cobrança e a NFS-e no Asaas; webhook de pago → Receitas | 2 | Asaas API |
| A9 | Kaio manda um custo no chat | Registra na aba Custos + atualiza o saldo de aportes | 0 | Claude (nesta sessão) → Sheets |
| A10 | Pedidos da loja do cliente (API) | Puxa o GMV por janela de live automaticamente | 2 | TikTok Shop API [A VERIFICAR] |
| A11 | Dia 20 do teste | Alerta de conversão + rascunho da proposta do mês 2 com os números | 1 | n8n + Claude |
| A12 | Foto do produto + medidas | Roteiro de vídeo curto e de live | 1 | Claude |

**Status atualizado** de cada automação: aba Catálogo da planilha "Casa Live — Automação (Config e Log)" e `areas/automacao/README.md`. Em 17/11: A1 no ar (teste real OK), A2 instalada e em teste até o primeiro cliente chegar em E3; A9 no ar pela sessão Financeiro.

## 3. Padrões técnicos
- **IDs:**
  - cliente `CLI-001`;
  - live `CL-2026-001`;
  - lead `LEAD-001`;
  - custo `CST-001`.
- **Segredos** (tokens de API, acessos de clientes) **nunca** em planilha ou documento. Usar o cofre do n8n e variáveis de ambiente.
- **Acessos de cliente:** sempre por convite e papel na conta do cliente, revogáveis; registrar quem concedeu e quando.
- **Dados separados por cliente:** relatórios e pastas por cliente; cada cliente vê só o que é seu.
- **Log:** cada automação grava data, gatilho, referência, resultado (OK, ERRO, TESTE) e erro na aba "Log" da planilha "Casa Live — Automação (Config e Log)". Erros também vão por e-mail ao Kaio.
- **Configuração:** IDs de planilhas e pastas na aba "Config" dessa planilha; e-mails nas Propriedades do script.
- **Colunas pelo nome do cabeçalho**, nunca pela letra. Renomear um cabeçalho usado por automação quebra a automação (ela para e registra o erro, não grava errado).
- **Locale pt-BR:** fórmulas gravadas por API ou script usam `;` como separador (`=SE(A2="";"";A2*2)`). Com `,` a célula mostra #ERROR!.
- **Não escrever em colunas "(auto)"** (fórmulas) das planilhas das outras áreas.

## 4. Contas e ferramentas a criar
| Ferramenta | Para quê | Fase | Custo |
|---|---|---|---|
| Google Workspace (e-mail da empresa) ou conta Google dedicada | Drive, Sheets, Forms, Agenda | 0 | [A VERIFICAR] |
| TikTok (conta da agência) + Instagram | Marketing + afiliado | 0 | Grátis |
| n8n | Automações | 1 | Self-hosted grátis ou cloud pago |
| Claude (Pro já assinado pelo Felipe) + API | IA | 0–1 | Uso |
| WhatsApp Business (número da empresa) | Comunicação | 0 (app) / 2 (API) | Grátis / por conversa |
| Asaas | Cobrança + NFS-e | 2 | Tarifas por cobrança |
| ZapSign / Autentique | Assinatura | 1 | Plano gratuito/pago |
| TikTok Shop Partner Center | API | 2 | A verificar |
