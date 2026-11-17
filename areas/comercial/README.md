# 🤝 Comercial e Clientes

**Escopo:** leads, qualificação, propostas, acordos de teste, onboarding, conversão do teste em plano pago e relacionamento (etapas E0 a E3, E8 e E9).

**Regras:** `docs/10-playbook-cliente.md`.

**Dados:** planilha "Casa Live — CRM" (Drive, pasta 02), ID `1pyNO4KHIYvxK9u9UO8HJghY4WT6obF5gCSq-XM6RryU`. Cada cliente tem uma pasta em `08 Clientes/<Marca>/` com Acordo, Fichas, Relatórios e Mídia.

## Planilha CRM (criada em 17/11/2026)
Padrão brasileiro (pt_BR, fuso de São Paulo). Nas fórmulas, o separador é `;`.

| Aba | Para quê | Quem preenche |
|---|---|---|
| Como usar | Passo a passo e legenda | — |
| Leads | Uma linha por marca: contato, origem, **Etapa** (lista E0 a E9, Encerrado, Futuro), próxima ação, prazo, responsável, início do teste e **condições comerciais do cliente** (comissão do teste, horas, fixo e comissão a partir do mês 2). Calcula sozinha a nota, a decisão, a comissão do teste aplicada e as datas dos dias 20, 25 e 30 do teste | Felipe |
| Qualificação | Checklist de 100 pontos do E1 (limite de nota por critério). Calcula a nota e a decisão (≥ 70 segue; 50 a 69 só com vaga; < 50 recusar) | Felipe |
| Onboarding | Caixas de seleção do E2/E3. Mostra os 3 OKs (Comercial, Conteúdo, Técnico) e "Pronto para a 1ª live" | Duda |
| Painel | Quantidade por etapa, vagas de teste livres (limite 3), nota média, próximas ações vencidas | automático |
| Listas | Opções dos menus: **Responsáveis** e **Taxas de comissão**. Para usar um responsável ou uma taxa nova, cadastre aqui na primeira linha vazia (taxa com %, ex.: 12%) e ela aparece no menu de todos os clientes | Felipe/Kaio |
| Parâmetros | Notas de corte, comissão de referência do teste (10%), dias do teste, lista de etapas e donos. **Não há tabela de planos:** os valores do mês 2 são por cliente | Kaio/Felipe |

- **ID do lead:** `LEAD-001`, `LEAD-002`… Mesmo ID nas três abas.
- Cabeçalho azul = preencher. Cabeçalho cinza "(auto)" = fórmula, não digitar.
- `LEAD-000` é linha de exemplo nas abas Leads, Qualificação e Onboarding. Fica fora das contas do Painel. Apagar quando entrar o primeiro lead real.
- As colunas de comissão da aba Leads (teste e mês 2) só aceitam taxas cadastradas na aba Listas. A coluna Responsável usa o menu da aba Listas.
- Donos das etapas na aba Parâmetros seguem a decisão de 17/11 (Duda na operação, Felipe no comercial).

## Como usar
- "Novo lead: <marca>, <contato>, <@tiktok>, <origem>" → o Claude cadastra o lead (`LEAD-NNN`) e sugere a mensagem M1.
- "Qualificar <marca>" → roda o checklist de 100 pontos.
- "Fechar teste com <marca>" → gera a proposta, o acordo de teste, a pasta do cliente e o formulário de onboarding.

## Pendências da área
- [ ] Definir a política de preços do mês 2 (ou seguir só caso a caso), quando houver números dos primeiros testes.
- [ ] Modelo do acordo de teste e da proposta (M2) em arquivo pronto para assinatura.
- [ ] Formulário de onboarding do cliente (Google Forms) ligado à aba Onboarding.
- [ ] Lista de prospecção: marcas que vendem no TikTok Shop e não fazem live.
