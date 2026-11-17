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
- **Mês 1 (teste):** comissão sobre o GMV líquido das nossas lives. Referência de 10%, mas a taxa é combinada com cada cliente (ver CRM, aba Leads). Os valores do mês 2 (fixo, horas, comissão) ainda não foram definidos e são negociados por cliente.
- **Mês 2 em diante:**
  - fixo cobrado no início do mês (pré-pago);
  - comissão cobrada no fechamento.
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
   - escopo: nº de lives, duração, conta da marca;
   - comissão de [X]% (combinada com o cliente; referência 10%) sobre o GMV líquido atribuído às nossas lives, com fonte = painel TikTok Shop e conferência conjunta;
   - pagamento até o dia 5;
   - responsabilidades do cliente: preço, estoque, envio, nota, pós-venda, veracidade das informações do produto;
   - nossas responsabilidades: estrutura, host, moderação, roteiro, relatório;
   - aprovação da ficha de produto;
   - uso de imagem e dos cortes (prazo e canais);
   - amostras: devolução ou retenção;
   - acesso à conta: concedido e revogável pelo cliente, sem senha pessoal;
   - **condições do mês 2** já informadas;
   - encerramento livre ao fim do teste.
2. **Contrato de prestação de serviço (mês 2 em diante, valores por cliente):** de 3 a 6 meses, horas por mês, fixo + comissão, reagendamento, horas não usadas, inadimplência (pausa), reajuste, rescisão.
3. **Termo de uso de imagem** para hosts e creators externos (fase 2).
- **Assinatura digital** (ZapSign, Autentique ou similar, com API).
