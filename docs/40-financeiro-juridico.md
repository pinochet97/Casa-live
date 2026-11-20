# 40 — Financeiro e Jurídico

> Validar com contador e advogado. Os itens marcados como [A VERIFICAR] não são orientação definitiva.

## 1. Empresa (CNPJ)
- **[DECIDIDO]** CNPJ em abertura, em nome do Felipe.
- **[A VERIFICAR com o contador]**
  - CNAE principal e secundários para "promoção de vendas / operação de lives / agenciamento":
    - 7319-0/02 Promoção de vendas;
    - 7490-1/04 Intermediação e agenciamento de serviços;
    - 7311-4/00 Agências de publicidade;
    - 5911-1/99 Produção audiovisual.
  - Regime: provavelmente Simples Nacional. Confirmar o anexo e a alíquota do serviço (Fator R).
  - O serviço é faturado com **NFS-e** da prefeitura do endereço da empresa.
  - Se a empresa for ter **marca própria** (venda de produto), incluir CNAE de comércio já agora ou abrir outro CNPJ depois.
- MEI não serve (não permite sócio e tem limite de faturamento e de atividades).

## 2. Sociedade: acordo de sócios (antes da 1ª receita)
O CNPJ está só com o Felipe, então o acordo protege os dois. Ele precisa definir:
1. **Participação:** % de cada um (Kaio e Felipe) e o prazo para o Kaio entrar no contrato social.
2. **Papéis e dedicação:** Felipe no comercial, Kaio em gestão, operação e tecnologia; horas mínimas.
3. **Divisão do resultado:** pró-labore (quando houver), distribuição de lucro, reserva de caixa mínima.
4. **Aportes:** como os custos pagos por cada um são registrados e reembolsados (ver seção 3).
5. **Decisões conjuntas:** contratar, alugar imóvel, gastos acima de R$ X, novos sócios ou investidores (ex.: Gustavo).
6. **Ativos:** a quem pertencem a marca, os perfis da agência, a base de clientes, os processos e os sistemas desenvolvidos pelo Kaio.
7. **Saída de sócio**, não concorrência, confidencialidade, solução de impasses.

## 3. Custos sem aporte inicial [DECIDIDO: dinheiro entra conforme a necessidade]
**Fluxo:**
1. Alguém paga um custo (Claude, anúncios, equipamento, frete etc.).
2. O Kaio manda para o Claude: "paguei X de Y em DD/MM".
3. O Claude registra na planilha financeira (aba Custos).
4. A planilha mantém o **saldo de aportes por sócio**.
5. Quando houver receita, primeiro se reembolsa quem aportou, na proporção combinada no acordo; depois vem a distribuição.

**Categorias de custo:**
- Ferramentas (Claude, editores, apps)
- Ads
- Equipamento (estúdio)
- Amostras e fretes
- Contas e taxas (CNPJ, contador, banco)
- Marketing
- Deslocamento
- Outros

## 4. Receita e comissão
- **Teste (30 dias) e contrato:** teste só por comissão (revenda 8%, fabricante 10% a 12%, taxa por cliente, ver CRM) sobre o GMV líquido das nossas lives; no contrato (3 meses, depois renovações de 6), gestão de R$ 3.000 + comissão.
- **Cobrança:**
  - gestão do contrato paga antecipada, no início de cada mês; comissão no boleto do dia 05, referente ao mês anterior;
  - boleto não pago: lives interrompidas imediatamente. Vendedores de live: R$ 40 por hora (mínimo de 3 h) + 2% do GMV da live, pagos pela Casa no dia 05 do mês seguinte, junto com a nossa comissão (no teste, as lives são feitas pelos sócios; a partir de 10 empresas, por 2 colaboradoras fixas; ver 11-estrutura-comercial).
- **Demonstrativo de comissão:** lista de lives (ID, data, GMV, cancelamentos e devoluções, GMV líquido) × % = valor. Vai junto com o relatório mensal.
- **Rota de afiliado:** a comissão é paga pelo TikTok Shop na nossa conta. Registrar como receita separada.
- **Cobrança:** Pix/boleto com vencimento no dia 5, via plataforma com emissão de NFS-e integrada (ex.: Asaas). [A VERIFICAR: tarifas]

## 5. Planilha financeira (abas)
Planilha **"Casa Live — Financeiro"** (Drive, pasta 05): ID `1CVGQsrUnb3zHe6a_VcUQhhQPGH2YpUlXK6iVwyhwssA`.
Convenções: texto azul = campo para digitar; texto preto = fórmula (não digitar por cima); fundo amarelo = depende de decisão. Datas em DD/MM/AAAA, valores com vírgula nos centavos. Planilha em português (pt_BR): nas fórmulas, o separador é `;`.

| Aba | Conteúdo |
|---|---|
| Leia-me | Legenda, descrição das abas e regras de preenchimento |
| Custos | ID (`CST-001`), data, descrição, categoria, valor, quem pagou (Kaio, Duda, Felipe ou Casa Live), forma, comprovante (link), observação. Coluna "Mês" automática |
| Aportes | Por pessoa: custos pagos − reembolsos = saldo a reembolsar. Subtotal "Lado Kaio (Kaio + Duda)" e % de cada lado. Linha de conferência (deve dar zero) |
| Reembolsos | ID (`REE-001`), data, para quem, valor, origem do dinheiro |
| Receitas | ID (`REC-001`), cliente, competência (dia 1 do mês), tipo (Fixo, Comissão, Afiliado), valor informado (fixo/afiliado), valor (comissão vem da aba Comissões), vencimento, pago em, valor pago, saldo, NF, status automático (Em aberto, Vencido, Pago, Sem vencimento, Sem valor) |
| Comissões | Demonstrativo por live: cliente, ID e data da live, GMV bruto, cancelamentos/devoluções, GMV líquido, %, comissão. Competência automática pela data |
| A receber | Totais em aberto, vencido e sem vencimento + lista automática ordenada por vencimento |
| Resultado mensal | Nov/2026 a dez/2027: fixo, comissão, afiliado, receita, custos, resultado, horas de live (digitar), receita por hora, acumulado |
| Caixa 13 semanas | Saldo de hoje (digitar), recebimentos previstos pelo vencimento, saídas previstas (digitar), saldo semana a semana |
| Listas | Opções dos menus: categorias, quem pagou, formas de pagamento, tipos de receita, **clientes** (cadastrar o cliente aqui antes de lançar receita ou comissão) |

## 6. Contratos (modelos a criar na pasta 05)
1. **Acordo de teste (30 dias, só comissão)**, com estes pontos:
   - escopo: mínimo de 60 h de live em pelo menos 22 dias no mês, conta da marca, vendedor exclusivo;
   - comissão de [X]% (revenda 8%, fabricante 10% a 12%) sobre o GMV líquido atribuído às nossas lives, com fonte = painel TikTok Shop e conferência conjunta;
   - boleto no dia 05, referente ao mês anterior; não pago, lives interrompidas;
   - responsabilidades do cliente: preço, estoque, envio, nota, pós-venda, veracidade das informações do produto;
   - nossas responsabilidades: estrutura, host, moderação, roteiro, relatório;
   - aprovação da ficha de produto;
   - uso de imagem e dos cortes (prazo e canais);
   - amostras: devolução ou retenção;
   - acesso à conta: concedido e revogável pelo cliente, sem senha pessoal;
   - **condições do contrato** já informadas;
   - encerramento livre ao fim do teste.
2. **Contrato de prestação de serviço (após o teste: 3 meses, depois renovações de 6):** gestão de R$ 3.000 antecipada + comissão, 60 h em 22 dias por mês, multa do cliente = 50% dos meses restantes [A VERIFICAR com advogado], cancelamento sem multa se a Casa não entregar as horas, inadimplência (interrupção imediata), reajuste.
3. **Termo de uso de imagem** para hosts e creators externos, e contrato de prestação de serviço do vendedor de live freelancer (R$ 40/h + 2% do GMV da live).
- **Assinatura digital** (ZapSign, Autentique ou similar, com API).
