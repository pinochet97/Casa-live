# Instalação das automações A1 e A2 (Kaio, cerca de 15 minutos, uma vez só)

> **Quem faz:** Kaio, no computador, logado na conta Google dona do Drive "Casa Live".
> **Resultado:** o formulário "Quero live" passa a criar leads no CRM e a avisar o Felipe por e-mail (A1). Cada cliente que chegar em E3 Onboarding ganha sua pasta em 08 Clientes (A2).
> **Código:** `areas/automacao/apps-script/casa-live-automacao/` (7 arquivos).

## Passo 1: criar o projeto do Apps Script
1. Abra a [pasta 06 Automação e Integrações](https://drive.google.com/drive/folders/1Tr203So05XuVRbJvr9_jaAItTy04F1T5) no Drive.
2. Clique em **+ Novo** → **Mais** → **Google Apps Script**. Se não aparecer, abra script.google.com e clique em **Novo projeto**.
3. No topo, clique em "Projeto sem título" e renomeie para `Casa Live — Automações`.

## Passo 2: colar o código
1. No GitHub, abra a pasta `areas/automacao/apps-script/casa-live-automacao/`.
2. O projeto já vem com um arquivo `Código.gs`. Apague todo o conteúdo dele e cole o de `Config.gs`. Depois renomeie o arquivo para `Config`: três pontinhos ao lado do nome → **Renomear**.
3. Para cada um dos outros arquivos (`Log.gs`, `Ids.gs`, `A1_Lead.gs`, `A2_PastaCliente.gs`, `Instalacao.gs`), clique em **+** ao lado de "Arquivos" → **Script**, dê o nome sem o `.gs` e cole o conteúdo.
4. **Configurações do projeto** (engrenagem na barra da esquerda):
   - em **Fuso horário**, deixe `(GMT-03:00) São Paulo`;
   - marque **Mostrar arquivo de manifesto "appsscript.json" no editor**.
5. Volte ao **Editor** (ícone `< >`), abra o `appsscript.json` e substitua todo o conteúdo pelo arquivo de mesmo nome do GitHub.
6. Salve (Ctrl+S).

**Como saber que deu certo:** à esquerda aparecem 7 arquivos: appsscript.json, Config, Log, Ids, A1_Lead, A2_PastaCliente e Instalacao.

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
1. Volte ao Editor, abra o arquivo `Instalacao`.
2. No topo, escolha a função `verificarInstalacao` e clique em **Executar**.
3. Na primeira vez, o Google pede autorização: **Revisar permissões** → escolha sua conta → **Avançado** → **Acessar Casa Live — Automações (não seguro)** → **Permitir**. Esse aviso é normal, porque o script é seu e não foi publicado.
4. **Como saber que deu certo:** abra a planilha [Casa Live — Automação (Config e Log)](https://docs.google.com/spreadsheets/d/1qgjsBVpLnkB_weRbK6DngA_Ron0-tSntiv5WhufS4Eo/edit), aba **Log**. A última linha deve dizer `Instalação | OK | Tudo certo`. Se aparecer ERRO, a coluna F diz o que falta. Corrija e rode de novo.

## Passo 5: instalar a A1 (formulário "Quero live")
1. Abra o arquivo `A1_Lead`, escolha a função `testarA1` e clique em **Executar**. No Log deve aparecer uma linha `A1 | TESTE` com o próximo ID (ex.: LEAD-001). Esse teste não mexe no CRM.
2. Escolha a função `instalarA1` e clique em **Executar**.
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
1. Abra o arquivo `A2_PastaCliente`, escolha a função `instalarA2` e clique em **Executar**.
2. **Como saber que deu certo:** o Log mostra `A2 | instalação | OK`. Em **Acionadores** (ícone de relógio na esquerda) aparecem dois gatilhos: `aoEnviarQueroLive` (ao enviar formulário) e `verificarPastasA2` (a cada 15 minutos).
3. A partir de agora, quando alguém mudar a Etapa de um lead para **E3 Onboarding** no CRM, a pasta `08 Clientes/<Marca>/`, com Acordo, Fichas, Relatórios e Mídia, aparece em até 15 minutos. A Duda recebe o link por e-mail.

## Passo 7: marcar como no ar
Na planilha de automação, aba **Catálogo**, mude o Status da A1 e da A2 para **No ar**. Ou avise a sessão Automação, que ela atualiza.

## Se der problema
- **Erro "Falta a Propriedade do script"**: refaça o Passo 3.
- **Erro "faltam as colunas"**: alguém renomeou um cabeçalho da aba Leads do CRM. Os scripts acham as colunas pelo nome exato. Volte o nome ou avise a sessão Automação.
- **Nada acontece ao enviar o formulário**: em **Acionadores**, veja se `aoEnviarQueroLive` existe. Em **Execuções**, veja o erro.
- Todo erro também chega por e-mail para o `EMAIL_KAIO`.
