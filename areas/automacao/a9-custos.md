# A9: lançar custos pelo chat (no ar, sem código)

**Como funciona:** quem pagou manda a mensagem na **sessão Financeiro** do Claude. O Claude grava na planilha "Casa Live — Financeiro", aba **Custos**, pelo conector Google Sheets. Não tem script: o conector é a automação.

**Mensagem padrão (Kaio ou Duda):**
```
paguei R$ 149,90 de ring light em 17/11, Kaio, Pix
```

**O que o Claude faz:**
1. Gera o próximo ID `CST-NNN`, olhando a coluna ID da aba Custos.
2. Preenche Data, Descrição, Categoria (da aba Listas), Valor, Quem pagou e Forma.
3. Pede o link do comprovante, se não vier junto.
4. A aba Aportes recalcula sozinha o saldo por sócio.

**Regras técnicas:**
- Valores são gravados como número (149.9) e não como texto, para as somas funcionarem.
- As datas são gravadas no formato DD/MM/AAAA, porque a planilha está em Português (Brasil).
- Fórmulas usam `;` como separador.

**Evolução (fase 2):** um bot de WhatsApp (n8n), que recebe a foto do comprovante e lança sozinho.
