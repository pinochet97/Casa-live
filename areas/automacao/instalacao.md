# Instalação das automações A1 e A2 (Kaio, cerca de 15 minutos, uma vez só)

> **Quem faz:** Kaio, no computador, logado na conta Google dona do Drive "Casa Live".
> **Resultado:** o formulário "Quero live" passa a criar leads no CRM e a avisar o Felipe por e-mail (A1). Cada cliente que chegar em E3 Onboarding ganha sua pasta em 08 Clientes (A2).
> **Código:** um arquivo só, `areas/automacao/apps-script/COLAR-NO-APPS-SCRIPT.gs`.

## Passo 1: criar o projeto do Apps Script
1. Abra a [pasta 06 Automação e Integrações](https://drive.google.com/drive/folders/1Tr203So05XuVRbJvr9_jaAItTy04F1T5) no Drive.
2. Clique em **+ Novo** → **Mais** → **Google Apps Script**. Se não aparecer, abra script.google.com e clique em **Novo projeto**.
3. No topo, clique em "Projeto sem título" e renomeie para `Casa Live — Automações`.

## Passo 2: colar o código (um arquivo só)
1. Abra no navegador: https://github.com/pinochet97/Casa-live/blob/main/areas/automacao/apps-script/COLAR-NO-APPS-SCRIPT.gs
2. No canto direito, acima do código, clique no ícone de **copiar** (dois quadradinhos, "Copy raw file"). O código inteiro vai para a área de transferência.
3. Volte ao Apps Script e clique dentro do arquivo **Código.gs**.
4. Aperte **Ctrl+A** para selecionar tudo o que está lá e depois **Ctrl+V** para colar.
5. Aperte **Ctrl+S** para salvar.
6. Clique na engrenagem **Configurações do projeto** (barra da esquerda). Em **Fuso horário**, confira se está `(GMT-03:00) Horário de Brasília` ou `São Paulo`.

**Como saber que deu certo:**
- a bolinha laranja ao lado de Código.gs some;
- a primeira linha do arquivo é `/**`, a segunda diz `CASA LIVE — AUTOMAÇÕES`;
- no menu de funções, no topo, ao lado de **Depuração**, aparecem nomes como `verificarInstalacao`, `instalarA1` e `instalarA2`.

> Não precisa criar outros arquivos nem mexer no `appsscript.json`. As permissões são pedidas sozinhas no Passo 4.

## Passo 3: cadastrar os e-mails (fora do código)
1. Clique na engrenagem **Configurações do projeto**, role até **Propriedades do script** e clique em **Adicionar propriedade do script**.
2. Crie estas três:

| Propriedade | Valor |
|---|---|
| `EMAIL_FELIPE` | e-mail onde o Felipe quer receber os leads novos |
| `EMAIL_DUDA` | e-mail da Duda (recebe o aviso de pasta criada) |
| `EMAIL_KAIO` | seu e-mail (recebe os avisos de erro) |

3. Clique em **Salvar propriedades do script**.

## Passo 4: verificar
1. Volte ao Editor (ícone `< >`).
2. No topo, no menu de funções ao lado de **Depuração**, escolha `verificarInstalacao` e clique em **Executar**.
3. Na primeira vez, o Google pede autorização: **Revisar permissões** → escolha sua conta → **Avançado** → **Acessar Casa Live — Automações (não seguro)** → **Permitir**. Esse aviso é normal, porque o script é seu e não foi publicado.
4. **Como saber que deu certo:** abra a planilha [Casa Live — Automação (Config e Log)](https://docs.google.com/spreadsheets/d/1qgjsBVpLnkB_weRbK6DngA_Ron0-tSntiv5WhufS4Eo/edit), aba **Log**. A última linha deve dizer `Instalação | OK | Tudo certo`. Se aparecer ERRO, a coluna F diz o que falta. Corrija e rode de novo.

## Passo 5: instalar a A1 (formulário "Quero live")
1. No menu de funções, escolha `testarA1` e clique em **Executar**. No Log deve aparecer uma linha `A1 | TESTE` com o próximo ID (ex.: LEAD-001). Esse teste não mexe no CRM.
2. No menu de funções, escolha `instalarA1` e clique em **Executar**.
3. **Como saber que deu certo:**
   - na aba **Config**, as linhas `FORM_QUERO_LIVE_ID` e `FORM_QUERO_LIVE_URL` agora têm valor;
   - na pasta 06 apareceu o formulário "Quero live na Casa Live".
4. Teste de verdade: abra o link de `FORM_QUERO_LIVE_URL` numa aba anônima e envie uma resposta com a marca `TESTE APAGAR`. Em até 1 minuto:
   - o CRM, aba Leads, ganha uma linha nova em E0 Lead;
   - o Felipe recebe o e-mail "[Casa Live] Novo lead";
   - o Log mostra `A1 | OK`.
5. Apague a linha `TESTE APAGAR` do CRM. Selecione a linha inteira e use **Excluir linha**: não basta limpar o conteúdo.
6. Mande o link `FORM_QUERO_LIVE_URL` para quem cuida da bio da agência (TikTok e Instagram).

## Passo 6: instalar a A2 (pasta do cliente)
1. No menu de funções, escolha `instalarA2` e clique em **Executar**.
2. **Como saber que deu certo:** o Log mostra `A2 | instalação | OK`. Em **Acionadores** (ícone de relógio na esquerda) aparecem dois gatilhos: `aoEnviarQueroLive` (ao enviar formulário) e `verificarPastasA2` (a cada 15 minutos).
3. A partir de agora, quando alguém mudar a Etapa de um lead para **E3 Onboarding** no CRM, a pasta `08 Clientes/<Marca>/`, com Acordo, Fichas, Relatórios e Mídia, aparece em até 15 minutos. A Duda recebe o link por e-mail.

## Passo 7: marcar como no ar
Na planilha de automação, aba **Catálogo**, mude o Status da A1 e da A2 para **No ar**. Ou avise a sessão Automação, que ela atualiza.

## Se der problema
- **Erro "Falta a Propriedade do script"**: refaça o Passo 3.
- **Erro "faltam as colunas"**: alguém renomeou um cabeçalho da aba Leads do CRM. Os scripts acham as colunas pelo nome exato. Volte o nome ou avise a sessão Automação.
- **Nada acontece ao enviar o formulário**: em **Acionadores**, veja se `aoEnviarQueroLive` existe. Em **Execuções**, veja o erro.
- Todo erro também chega por e-mail para o `EMAIL_KAIO`.
