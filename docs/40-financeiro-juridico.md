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
- **Mês 1 (teste):** 10% sobre o GMV líquido das nossas lives.
- **Mês 2 em diante:**
  - fixo cobrado no início do mês (pré-pago);
  - comissão cobrada no fechamento.
- **Demonstrativo de comissão:** lista de lives (ID, data, GMV, cancelamentos e devoluções, GMV líquido) × % = valor. Vai junto com o relatório mensal.
- **Rota de afiliado:** a comissão é paga pelo TikTok Shop na nossa conta. Registrar como receita separada.
- **Cobrança:** Pix/boleto com vencimento no dia 5, via plataforma com emissão de NFS-e integrada (ex.: Asaas). [A VERIFICAR: tarifas]

## 5. Planilha financeira (abas)
| Aba | Conteúdo |
|---|---|
| Custos | Data, descrição, categoria, valor, quem pagou, forma, comprovante (link) |
| Aportes | Saldo por sócio (soma dos custos pagos − reembolsos) |
| Receitas | Cliente, competência, tipo (fixo, comissão, afiliado), valor, vencimento, pago em, NF |
| A receber | Abertos e vencidos |
| Resultado mensal | Receita − custos, receita por hora de live |
| Caixa 13 semanas | Projeção simples |

## 6. Contratos (modelos a criar na pasta 05)
1. **Acordo de teste (30 dias, só comissão)**, com estes pontos:
   - escopo: nº de lives, duração, conta da marca;
   - comissão de 10% sobre o GMV líquido atribuído às nossas lives, com fonte = painel TikTok Shop e conferência conjunta;
   - pagamento até o dia 5;
   - responsabilidades do cliente: preço, estoque, envio, nota, pós-venda, veracidade das informações do produto;
   - nossas responsabilidades: estrutura, host, moderação, roteiro, relatório;
   - aprovação da ficha de produto;
   - uso de imagem e dos cortes (prazo e canais);
   - amostras: devolução ou retenção;
   - acesso à conta: concedido e revogável pelo cliente, sem senha pessoal;
   - **condições do mês 2** já informadas;
   - encerramento livre ao fim do teste.
2. **Contrato de prestação de serviço (plano Start/Pro):** de 3 a 6 meses, horas por mês, fixo + comissão, reagendamento, horas não usadas, inadimplência (pausa), reajuste, rescisão.
3. **Termo de uso de imagem** para hosts e creators externos (fase 2).
- **Assinatura digital** (ZapSign, Autentique ou similar, com API).
