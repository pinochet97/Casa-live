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

[A VERIFICAR] Os nomes exatos das métricas no painel do TikTok Shop Brasil serão conferidos na primeira live e ajustados aqui.

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

**Ferramenta:** começa como aba "Painel" no Google Sheets e depois migra para o Looker Studio, conectado às planilhas.
