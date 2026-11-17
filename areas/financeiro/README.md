# 💰 Financeiro

**Escopo:** custos, aportes por sócio, receitas (fixo, comissão, afiliado), contas a receber, cobrança, notas, fechamento mensal, CNPJ e acordo de sócios.

**Regras:** `docs/40-financeiro-juridico.md`.

**Dados:** planilha "Casa Live — Financeiro" (Drive, pasta 05), ID `1CVGQsrUnb3zHe6a_VcUQhhQPGH2YpUlXK6iVwyhwssA`. Criada em 17/11/2026, ainda sem lançamentos.
Abas: Leia-me, Custos, Aportes, Reembolsos, Receitas, Comissões, A receber, Resultado mensal, Caixa 13 semanas, Listas. Detalhes em `docs/40-financeiro-juridico.md`, seção 5.
**Para o Claude:** a planilha está em pt_BR, então as fórmulas usam `;` como separador. As colunas automáticas (Custos!J, Receitas!F, J, L, Comissões!B, G, I) são fórmulas ARRAYFORMULA na linha 2: nunca escrever nelas. Lançar sempre na primeira linha vazia.

**Como lançar um custo:** escreva "paguei R$ X de <o quê> em DD/MM, <quem pagou>, <forma>". O Claude registra com ID `CST-NNN` e categoria, e atualiza o saldo de aportes.

**Como lançar uma receita:** cadastrar o cliente em Listas (coluna E). Para comissão: uma linha por live na aba Comissões, e uma linha em Receitas com Tipo = Comissão (o valor é calculado sozinho). Para fixo ou afiliado: valor na coluna "Valor informado".

**Rotinas:**
- **Dia 1:** apurar a comissão de cada cliente e gerar o demonstrativo.
- **Dia 5:** conferir os pagamentos.
- **Segunda:** caixa e a receber para a reunião.
