# ⚙️ Automação e Integrações

**Escopo:** automações A1 a A12, n8n, Apps Script, integrações (TikTok Shop, Asaas, WhatsApp, Claude API, assinatura digital), padrões de IDs e segurança.

**Regras:** `docs/50-automacao-integracoes.md`.

**Planilha da área:** "Casa Live — Automação (Config e Log)", na pasta 06 (`1qgjsBVpLnkB_weRbK6DngA_Ron0-tSntiv5WhufS4Eo`). Abas:
- **Catálogo:** status de cada automação (A1 a A12).
- **Config:** IDs das planilhas e pastas.
- **Pastas de clientes:** usada pela A2.
- **Log:** uma linha por execução.

## Status (17/11/2026)
| # | O quê | Status | Onde |
|---|---|---|---|
| A1 | Formulário "Quero live" → lead no CRM → e-mail ao Felipe | Código pronto, falta o Kaio instalar | `apps-script/casa-live-automacao/A1_Lead.gs` |
| A2 | CRM em E3 → pasta do cliente em 08 Clientes → e-mail à Duda | Código pronto, falta o Kaio instalar | `apps-script/casa-live-automacao/A2_PastaCliente.gs` |
| A9 | Custo no chat → aba Custos | No ar (sessão Financeiro) | `a9-custos.md` |
| A3 a A8, A10 a A12 | — | Planejadas | Catálogo na planilha |

**Próxima ação humana:** o Kaio segue o `instalacao.md` (cerca de 15 minutos).

## Código
```
areas/automacao/
├── instalacao.md                  ← passo a passo para o Kaio instalar A1 e A2
├── a9-custos.md                   ← como a A9 funciona
├── apps-script/COLAR-NO-APPS-SCRIPT.gs ← arquivo único que o Kaio cola no Apps Script (gerado)
├── apps-script/casa-live-automacao/   ← código-fonte, separado por assunto
│   ├── appsscript.json   (fuso, permissões)
│   ├── Config.gs         (lê a aba Config e as Propriedades do script; acha colunas pelo nome)
│   ├── Log.gs            (registrarLog, avisarErro)
│   ├── Ids.gs            (proximoId: LEAD-001, CLI-001…)
│   ├── A1_Lead.gs
│   ├── A2_PastaCliente.gs
│   └── Instalacao.gs     (verificarInstalacao)
├── n8n/      (workflows exportados em JSON, a partir da fase 1)
└── scripts/juntar-apps-script.sh  (gera o arquivo único)
```

## Regras de código
- **Colunas pelo nome do cabeçalho, nunca pela letra.** Se outra área renomear um cabeçalho usado, o script para e registra o erro no Log, em vez de gravar na coluna errada.
- **Nunca escrever nas colunas "(auto)"** das planilhas das outras áreas: elas são fórmulas.
- **Toda execução grava no Log:** OK, ERRO ou TESTE. Erros também vão por e-mail para o Kaio.
- **Segredos e e-mails:** só nas Propriedades do script ou no cofre do n8n.
- **Fórmulas por API ou script:** separador `;` (as planilhas estão em pt-BR).
- Cada automação tem uma função `testar…` que não altera dados.
- Ao mudar qualquer `.gs`, rodar `bash areas/automacao/scripts/juntar-apps-script.sh` e colar o `COLAR-NO-APPS-SCRIPT.gs` de novo no Apps Script (Ctrl+A, Ctrl+V). O GitHub é a fonte da verdade.

**Regra de segurança:** tokens e senhas **nunca** no repositório nem nas planilhas. Usar o cofre do n8n e variáveis de ambiente.
