# Como usamos o Claude: sessões e memória

## Regra de ouro
**A memória da operação fica nos arquivos, não nas conversas.**
- Toda sessão nova clona o GitHub e lê o `CLAUDE.md`. Ela só "sabe" o que estiver commitado e enviado (push).
- Os dados do dia a dia (custos, leads, lives) ficam nas **planilhas do Drive**.
- Regras, processos e decisões ficam no **GitHub** (`docs/` e `areas/`).
- Toda sessão termina com: atualizar arquivos → commit → **push**. Sem push, as outras sessões não enxergam o que mudou.

## Sessões fixas (Claude Code, repositório casa-live)
| Sessão | Quem usa | Para quê | Pasta no repo | Pasta no Drive |
|---|---|---|---|---|
| 🧠 **Central** | Kaio | Estratégia, decisões, revisar o plano, reunião semanal, coordenar as outras áreas | `areas/central` | 00, 01 |
| 💰 **Financeiro** | Kaio | Lançar custos e aportes, receitas, comissões, cobrança, fechamento do mês | `areas/financeiro` | 05 |
| 🤝 **Comercial e Clientes** | Felipe e Kaio | Leads, qualificação, propostas, acordos, onboarding de cada cliente (E0 a E3, E8 e E9) | `areas/comercial` | 02, 08 |
| 🎬 **Operação** | Kaio, Duda, hosts | Agenda, fichas de produto, roteiros, registro de lives, relatórios (E4 a E7) | `areas/operacao` | 03, 04 |
| ⚙️ **Automação** | Kaio | n8n, Apps Script, APIs, integrações. O código fica no repo | `areas/automacao` | 06 |

**Dica:** não abra uma sessão por cliente. Os clientes vivem na sessão "Comercial e Clientes" e nas pastas `08 Clientes/<Marca>`. Uma sessão longa demais fica lenta. Quando isso acontecer, encerre e abra outra com o mesmo prompt inicial: o contexto está nos arquivos.

## Prompt inicial de cada sessão (copiar e colar)
```
Você é o responsável pela área <ÁREA> da Casa Live.
Leia CLAUDE.md, docs/00-plano-mestre.md e areas/<pasta>/README.md antes de qualquer coisa.
Trabalhe só dentro do escopo dessa área. Decisões vão para docs/decisoes.md.
Ao terminar cada tarefa: atualize os arquivos e as planilhas, faça commit e push no branch combinado.
```

## Felipe no claude.ai (chat)
Para o Felipe tirar dúvidas e consultar números sem mexer em arquivos, crie no claude.ai um **Projeto "Casa Live"** com o GitHub (este repositório) e o Google Drive conectados. Ele faz perguntas com o contexto completo, e o que for decisão volta para a sessão Central.
