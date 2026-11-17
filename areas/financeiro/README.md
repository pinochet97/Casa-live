# 💰 Financeiro

**Escopo:** custos, aportes por sócio, receitas (fixo, comissão, afiliado), contas a receber, cobrança, notas, fechamento mensal, CNPJ e acordo de sócios.

**Regras:** `docs/40-financeiro-juridico.md`.

**Dados:** planilha "Casa Live — Financeiro" (Drive, pasta 05). Abas: Custos, Aportes, Receitas, A receber, Resultado mensal, Caixa 13 semanas.

**Como lançar um custo:** escreva "paguei R$ X de <o quê> em DD/MM, <quem pagou>, <forma>". O Claude registra com ID `CST-NNN` e categoria, e atualiza o saldo de aportes.

**Rotinas:**
- **Dia 1:** apurar a comissão de cada cliente e gerar o demonstrativo.
- **Dia 5:** conferir os pagamentos.
- **Segunda:** caixa e a receber para a reunião.
