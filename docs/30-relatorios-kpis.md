# 30 — Relatórios e KPIs

## 1. Regras de dados
- Cada número tem **fonte, período e data da extração**. Guardar o print ou a exportação original na pasta do cliente.
- **GMV não é lucro** e venda atribuída não é necessariamente venda incremental. Deixar isso claro no relatório.
- A comissão é calculada sobre **GMV líquido**: GMV menos cancelamentos e devoluções do período.
- Campo vazio = "não disponível", nunca zero.

## 2. Indicadores por live (preenchidos no Registro de Lives)
| Campo | Fonte |
|---|---|
| ID interno (CL-AAAA-NNN), cliente, conta, data, início e fim reais, duração | Nosso registro |
| Host, moderador, cenário | Nosso registro |
| Espectadores únicos, pico, tempo médio de visualização | Painel da live (LIVE Manager / Seller Center) |
| Novos seguidores, curtidas, comentários, compartilhamentos | Painel da live |
| Cliques no produto, pedidos, itens vendidos, **GMV** | Painel da live |
| Conversão (pedidos ÷ espectadores) e GPM (GMV por mil espectadores) | Calculado |
| Produto campeão, promoção relâmpago usada | Nosso registro |
| Incidentes (falha nossa ou do cliente) | Nosso registro |
| Nota do host | Coordenação |

[A VERIFICAR] Os nomes exatos das métricas no painel do TikTok Shop Brasil serão conferidos na primeira live e ajustados aqui e nos cabeçalhos da planilha.

**Onde fica:** planilha **Casa Live — Registro de Lives** (`1r_hgNWirrSL0AUcE8nDDMRjJt9cQz9qlTftfsgfLxn4`), aba Registro, uma linha por live. Fórmulas (auto) da linha:
- Duração (h) = fim real − início real;
- Atraso (min) = início real − início previsto (negativo se começou antes);
- No horário = Sim se o atraso for de até **5 minutos** [PROPOSTA, parâmetro na aba Listas];
- Conversão = pedidos ÷ espectadores únicos;
- GPM = GMV ÷ espectadores únicos × 1.000;
- GMV por hora = GMV ÷ duração;
- Semana (segunda) e Mês, para os resumos.

O Registro guarda o **GMV bruto** do painel. GMV líquido e comissão ficam na planilha Financeiro, aba Comissões, ligados pelo ID da live.

## 3. Relatório da live (D+1) — modelo
```
📊 Live [Marca] — [dia/mês], [hora] ([duração])
• Espectadores: X (pico de Y às HH:MM)
• Vendas: R$ X em N pedidos (N itens)
• Produto campeão: ___
• Conversão: X% | GPM: R$ X
✅ O que funcionou: ___
🔧 O que vamos mudar na próxima: ___
📅 Próxima live: [dia], [hora] — produtos: ___
```

## 4. Relatório semanal (segunda) e mensal (dia 1)
- **Semanal:**
  - soma da semana × semana anterior;
  - melhor live;
  - produto campeão;
  - aprendizados;
  - plano da semana.
- **Mensal:**
  - resultado do mês (lives, horas, GMV bruto e líquido, pedidos);
  - **comissão apurada (demonstrativo)**;
  - evolução por semana;
  - top produtos;
  - recomendações;
  - no fim do teste, a proposta do plano.
- **Formato:** um Google Doc ou PDF a partir de um modelo, preenchido automaticamente com os dados da planilha e o texto escrito pelo Claude.
- **De onde vêm os números:** aba **Resumo semanal** (por semana, filtrável por cliente, com a variação do GMV contra a semana anterior) e aba **Resumo por cliente** (qualquer período: lives, horas, GMV, pedidos, conversão, GPM, GMV por hora, % no horário, incidentes, % de relatórios D+1 enviados, nota média do host).

## 5. Painel interno da agência (semanal)
| Bloco | KPI | Definição |
|---|---|---|
| Comercial | Leads novos, taxa de qualificação, testes fechados | Funil do CRM E0→E2 |
| Comercial | Conversão de teste em pagante | Clientes no fixo ÷ testes encerrados |
| Operação | Horas de live entregues | Soma das durações |
| Operação | Ocupação | Horas entregues ÷ capacidade (definir a capacidade dos sócios) |
| Operação | Pontualidade e incidentes | % de lives no horário; nº de incidentes por falha nossa |
| Resultado do cliente | GMV total, GMV por hora, GPM | Do Registro de Lives |
| Financeiro | Receita (fixo + comissão), a receber, inadimplência | Planilha financeira |
| Financeiro | Receita por hora de live | Receita ÷ horas. **Este é o principal número do negócio** |
| Financeiro | Custos do mês e saldo de aportes por sócio | Planilha financeira |
| Hosts | Nota média e GMV por hora por host | Registro + avaliação |

**Ferramenta:** começa como aba "Painel" no Google Sheets e depois migra para o Looker Studio, conectado às planilhas. Os blocos Operação, Resultado do cliente e Hosts já saem do Registro de Lives (abas Resumo por cliente e Hosts).
