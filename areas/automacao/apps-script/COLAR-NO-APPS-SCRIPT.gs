/**
 * CASA LIVE — AUTOMAÇÕES (arquivo único para colar no Apps Script)
 * Gerado por scripts/juntar-apps-script.sh. NÃO editar aqui: edite os arquivos em casa-live-automacao/ e rode o script de novo.
 */

// ===================== Config =====================

/**
 * Casa Live — configuração compartilhada.
 *
 * IDs de planilhas e pastas: aba Config da planilha "Casa Live — Automação (Config e Log)".
 * E-mails e qualquer segredo: Propriedades do script (Configurações do projeto > Propriedades do script).
 * Nunca colocar token, senha ou e-mail neste arquivo.
 */

var AUTOMACAO_ID = '1qgjsBVpLnkB_weRbK6DngA_Ron0-tSntiv5WhufS4Eo';
var FUSO = 'America/Sao_Paulo';

/** Lê a aba Config (Chave | Valor) e devolve um objeto. */
function lerConfig() {
  var aba = SpreadsheetApp.openById(AUTOMACAO_ID).getSheetByName('Config');
  var linhas = aba.getRange(2, 1, Math.max(aba.getLastRow() - 1, 1), 2).getValues();
  var cfg = {};
  linhas.forEach(function (l) {
    if (l[0]) cfg[String(l[0]).trim()] = String(l[1]).trim();
  });
  return cfg;
}

/** Grava um valor na aba Config (cria a chave se não existir). */
function gravarConfig(chave, valor) {
  var aba = SpreadsheetApp.openById(AUTOMACAO_ID).getSheetByName('Config');
  var chaves = aba.getRange(1, 1, aba.getLastRow(), 1).getValues();
  for (var i = 0; i < chaves.length; i++) {
    if (String(chaves[i][0]).trim() === chave) {
      aba.getRange(i + 1, 2).setValue(valor);
      return;
    }
  }
  aba.appendRow([chave, valor, '']);
}

/** Lê uma Propriedade do script. Se obrigatoria e vazia, lança erro claro. */
function propriedade(nome, obrigatoria) {
  var v = PropertiesService.getScriptProperties().getProperty(nome);
  if (obrigatoria && !v) {
    throw new Error('Falta a Propriedade do script "' + nome + '". Veja areas/automacao/instalacao.md.');
  }
  return v || '';
}

/**
 * Mapa "nome do cabeçalho" -> número da coluna (1 = A).
 * As automações acham as colunas pelo nome, então a ordem pode mudar sem quebrar nada.
 */
function mapaCabecalho(aba) {
  var cab = aba.getRange(1, 1, 1, aba.getLastColumn()).getValues()[0];
  var mapa = {};
  cab.forEach(function (nome, i) {
    if (nome) mapa[String(nome).trim()] = i + 1;
  });
  return mapa;
}

/** Garante que os cabeçalhos exigidos existem; senão, erro com a lista do que falta. */
function exigirColunas(mapa, nomes, nomeAba) {
  var faltando = nomes.filter(function (n) { return !mapa[n]; });
  if (faltando.length) {
    throw new Error('Na aba ' + nomeAba + ' faltam as colunas: ' + faltando.join(', '));
  }
}

// ===================== Log =====================

/**
 * Casa Live — log das automações.
 * Toda automação grava uma linha na aba Log: data, automação, gatilho, referência, resultado e detalhe.
 * Resultado: OK, ERRO ou TESTE.
 */
function registrarLog(automacao, gatilho, referencia, resultado, detalhe) {
  try {
    var aba = SpreadsheetApp.openById(AUTOMACAO_ID).getSheetByName('Log');
    aba.appendRow([new Date(), automacao, gatilho, referencia || '', resultado, String(detalhe || '').slice(0, 1000)]);
  } catch (err) {
    // Se nem o log funcionar, ao menos aparece em Execuções no Apps Script.
    console.error('Falha ao gravar log: ' + err + ' | ' + automacao + ' ' + resultado + ' ' + detalhe);
  }
}

/** Envia e-mail de erro para o Kaio (se EMAIL_KAIO estiver configurado). */
function avisarErro(automacao, err) {
  var email = propriedade('EMAIL_KAIO', false);
  if (!email) return;
  MailApp.sendEmail(email, '[Casa Live] Erro na automação ' + automacao,
    'A automação ' + automacao + ' falhou.\n\nErro: ' + err + '\n\n' +
    'Veja a aba Log: https://docs.google.com/spreadsheets/d/' + AUTOMACAO_ID + '/edit');
}

// ===================== Ids =====================

/**
 * Casa Live — IDs padronizados (docs/50, seção 3).
 * LEAD-001, CLI-001, CST-001; live: CL-2026-001.
 */

/**
 * Próximo ID com prefixo (ex.: 'LEAD') olhando a coluna de IDs da aba.
 * Ignora o 000 (linha de exemplo) e qualquer valor fora do padrão.
 */
function proximoId(aba, colunaId, prefixo) {
  var ultima = aba.getLastRow();
  var maior = 0;
  if (ultima >= 2) {
    var valores = aba.getRange(2, colunaId, ultima - 1, 1).getValues();
    var re = new RegExp('^' + prefixo + '-(\\d+)$');
    valores.forEach(function (v) {
      var m = String(v[0]).trim().match(re);
      if (m) maior = Math.max(maior, parseInt(m[1], 10));
    });
  }
  return prefixo + '-' + ('00' + (maior + 1)).slice(-Math.max(3, String(maior + 1).length));
}

/** Primeira linha (a partir da 2) com a coluna de ID vazia. Não confia em getLastRow por causa das fórmulas automáticas. */
function primeiraLinhaVazia(aba, colunaId) {
  var total = aba.getMaxRows();
  var valores = aba.getRange(2, colunaId, total - 1, 1).getValues();
  for (var i = 0; i < valores.length; i++) {
    if (String(valores[i][0]).trim() === '') return i + 2;
  }
  aba.insertRowAfter(total);
  return total + 1;
}

// ===================== A1_Lead =====================

/**
 * A1 — Formulário "Quero live" -> lead no CRM (E0) -> aviso ao Felipe.
 *
 * Instalação (uma vez, pelo Kaio): rodar instalarA1(). Ele cria o formulário na pasta 06,
 * grava o ID e o link na aba Config e cria o gatilho de envio.
 * Fase 0: aviso por e-mail. Fase 2: trocar por WhatsApp (Cloud API) via n8n.
 */

var A1_PERGUNTAS = {
  marca: 'Nome da marca',
  contato: 'Seu nome',
  whatsapp: 'WhatsApp com DDD',
  tiktok: '@ da marca no TikTok',
  loja: 'Link da loja (TikTok Shop ou outra)',
  categoria: 'Categoria dos produtos',
  temShop: 'A marca já vende no TikTok Shop?',
  mensagem: 'Quer contar algo mais? (produtos, metas, dúvidas)'
};

var A1_CATEGORIAS = ['Cosméticos e beleza', 'Moda e acessórios', 'Casa e decoração', 'Alimentos e bebidas',
  'Eletrônicos e games', 'Saúde e bem-estar', 'Infantil', 'Pet', 'Outro'];

function instalarA1() {
  var cfg = lerConfig();
  if (cfg.FORM_QUERO_LIVE_ID) {
    throw new Error('O formulário já existe (FORM_QUERO_LIVE_ID na aba Config). Apague o valor só se quiser criar outro.');
  }

  var form = FormApp.create('Quero live na Casa Live');
  form.setDescription('Conte um pouco da sua marca. A gente responde no WhatsApp em até 1 dia útil.');
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  form.setConfirmationMessage('Recebemos! Em breve a equipe da Casa Live chama você no WhatsApp.');

  form.addTextItem().setTitle(A1_PERGUNTAS.marca).setRequired(true);
  form.addTextItem().setTitle(A1_PERGUNTAS.contato).setRequired(true);
  form.addTextItem().setTitle(A1_PERGUNTAS.whatsapp).setHelpText('Ex.: 11 91234-5678').setRequired(true);
  form.addTextItem().setTitle(A1_PERGUNTAS.tiktok).setHelpText('Ex.: @suamarca').setRequired(true);
  form.addTextItem().setTitle(A1_PERGUNTAS.loja).setRequired(false);
  form.addListItem().setTitle(A1_PERGUNTAS.categoria).setChoiceValues(A1_CATEGORIAS).setRequired(true);
  form.addMultipleChoiceItem().setTitle(A1_PERGUNTAS.temShop).setChoiceValues(['Sim', 'Não', 'Não sei']).setRequired(true);
  form.addParagraphTextItem().setTitle(A1_PERGUNTAS.mensagem).setRequired(false);

  // Move o formulário para a pasta 06 Automação.
  DriveApp.getFileById(form.getId()).moveTo(DriveApp.getFolderById(cfg.PASTA_AUTOMACAO));

  ScriptApp.newTrigger('aoEnviarQueroLive').forForm(form).onFormSubmit().create();

  gravarConfig('FORM_QUERO_LIVE_ID', form.getId());
  gravarConfig('FORM_QUERO_LIVE_URL', form.getPublishedUrl());
  registrarLog('A1', 'instalação', form.getId(), 'OK', 'Formulário criado: ' + form.getPublishedUrl());
  console.log('Formulário criado. Link público: ' + form.getPublishedUrl());
}

/** Gatilho: cada envio do formulário. */
function aoEnviarQueroLive(e) {
  var respostas = {};
  e.response.getItemResponses().forEach(function (ir) {
    respostas[ir.getItem().getTitle()] = ir.getResponse();
  });
  criarLeadA1(respostas, e.response.getTimestamp(), false);
}

/**
 * Grava o lead no CRM. Separada do gatilho para poder testar.
 * @param {Object} respostas título da pergunta -> resposta
 * @param {Date} quando
 * @param {boolean} teste se true, não grava no CRM nem manda e-mail; só registra no Log o que faria
 */
function criarLeadA1(respostas, quando, teste) {
  var lock = LockService.getScriptLock();
  lock.waitLock(30000);
  var idLead = '';
  try {
    var cfg = lerConfig();
    var aba = SpreadsheetApp.openById(cfg.CRM_ID).getSheetByName('Leads');
    var col = mapaCabecalho(aba);
    exigirColunas(col, ['ID', 'Data de entrada', 'Marca', 'Contato (nome)', 'WhatsApp', '@ TikTok',
      'Link da loja', 'Categoria', 'Origem', 'Quem trouxe', 'Etapa', 'Tem TikTok Shop?',
      'Próxima ação', 'Prazo da próxima ação', 'Responsável', 'Observações'], 'Leads');

    idLead = proximoId(aba, col['ID'], 'LEAD');
    var hoje = new Date(quando.getFullYear(), quando.getMonth(), quando.getDate());
    var r = function (chave) { return String(respostas[A1_PERGUNTAS[chave]] || '').trim(); };
    var tiktok = r('tiktok');
    if (tiktok && tiktok.charAt(0) !== '@' && tiktok.indexOf('http') !== 0) tiktok = '@' + tiktok;

    // Só as colunas de digitação. As colunas (auto) do CRM são fórmulas e não são tocadas.
    var valores = {};
    valores['ID'] = idLead;
    valores['Data de entrada'] = hoje;
    valores['Marca'] = r('marca');
    valores['Contato (nome)'] = r('contato');
    valores['WhatsApp'] = r('whatsapp');
    valores['@ TikTok'] = tiktok;
    valores['Link da loja'] = r('loja');
    valores['Categoria'] = r('categoria');
    valores['Origem'] = 'Formulário Quero live';
    valores['Quem trouxe'] = 'Formulário';
    valores['Etapa'] = 'E0 Lead';
    valores['Tem TikTok Shop?'] = r('temShop') || 'Não sei';
    valores['Próxima ação'] = 'Mandar M1 (primeiro contato)';
    valores['Prazo da próxima ação'] = hoje;
    valores['Responsável'] = 'Felipe';
    valores['Observações'] = r('mensagem') ? 'Mensagem no formulário: ' + r('mensagem') : '';

    if (teste) {
      registrarLog('A1', 'teste', idLead, 'TESTE', 'Gravaria: ' + JSON.stringify(valores));
      return idLead;
    }

    var linha = primeiraLinhaVazia(aba, col['ID']);
    Object.keys(valores).forEach(function (nome) {
      aba.getRange(linha, col[nome]).setValue(valores[nome]);
    });
    SpreadsheetApp.flush();

    avisarFelipeA1(idLead, valores, cfg);
    registrarLog('A1', 'formulário enviado', idLead, 'OK', valores['Marca'] + ' (linha ' + linha + ' do CRM)');
    return idLead;
  } catch (err) {
    registrarLog('A1', 'formulário enviado', idLead, 'ERRO', err);
    avisarErro('A1', err);
    throw err;
  } finally {
    lock.releaseLock();
  }
}

function avisarFelipeA1(idLead, v, cfg) {
  var email = propriedade('EMAIL_FELIPE', true);
  var corpo = [
    'Novo lead pelo formulário "Quero live". Prazo do primeiro contato (M1): hoje.',
    '',
    'ID: ' + idLead,
    'Marca: ' + v['Marca'],
    'Contato: ' + v['Contato (nome)'],
    'WhatsApp: ' + v['WhatsApp'] + '  ->  https://wa.me/55' + String(v['WhatsApp']).replace(/\D/g, '').replace(/^55/, ''),
    'TikTok: ' + v['@ TikTok'],
    'Loja: ' + (v['Link da loja'] || 'não informou'),
    'Categoria: ' + v['Categoria'],
    'Já vende no TikTok Shop: ' + v['Tem TikTok Shop?'],
    v['Observações'] ? v['Observações'] : '',
    '',
    'CRM: https://docs.google.com/spreadsheets/d/' + cfg.CRM_ID + '/edit',
    'Próximo passo (Playbook E0): olhar a loja e mandar a mensagem M1.'
  ].join('\n');
  MailApp.sendEmail(email, '[Casa Live] Novo lead: ' + v['Marca'] + ' (' + idLead + ')', corpo);
}

/** Teste seguro: simula um envio e só grava no Log o que faria. Não mexe no CRM. */
function testarA1() {
  var fake = {};
  fake[A1_PERGUNTAS.marca] = 'Marca Teste';
  fake[A1_PERGUNTAS.contato] = 'Fulano';
  fake[A1_PERGUNTAS.whatsapp] = '11 91234-5678';
  fake[A1_PERGUNTAS.tiktok] = 'marcateste';
  fake[A1_PERGUNTAS.categoria] = 'Outro';
  fake[A1_PERGUNTAS.temShop] = 'Sim';
  var id = criarLeadA1(fake, new Date(), true);
  console.log('Teste ok. Veja a aba Log: o próximo ID seria ' + id);
}

// ===================== A2_PastaCliente =====================

/**
 * A2 — Lead chega em "E3 Onboarding" (acordo assinado) -> cria a pasta do cliente em 08 Clientes.
 *
 * Roda a cada 15 minutos (gatilho de tempo), procura no CRM as linhas em E3 ou depois
 * que ainda não têm pasta e cria: 08 Clientes/<Marca>/ com Acordo, Fichas, Relatórios e Mídia.
 * Registra na aba "Pastas de clientes" da planilha de automação, para nunca duplicar,
 * e avisa a Duda por e-mail com o link.
 */

var A2_SUBPASTAS = ['Acordo', 'Fichas', 'Relatórios', 'Mídia'];
var A2_ETAPAS_COM_PASTA = ['E3 Onboarding', 'E4 Planejamento', 'E5 Live', 'E6 Relatório', 'E7 Cobrança',
  'E8 Conversão', 'E9 Ativo'];

function instalarA2() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'verificarPastasA2') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('verificarPastasA2').timeBased().everyMinutes(15).create();
  registrarLog('A2', 'instalação', '', 'OK', 'Gatilho a cada 15 minutos criado');
  verificarPastasA2();
}

function verificarPastasA2() {
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(10000)) return;
  try {
    var cfg = lerConfig();
    var crm = SpreadsheetApp.openById(cfg.CRM_ID).getSheetByName('Leads');
    var col = mapaCabecalho(crm);
    exigirColunas(col, ['ID', 'Marca', 'Etapa'], 'Leads');

    var registro = SpreadsheetApp.openById(AUTOMACAO_ID).getSheetByName('Pastas de clientes');
    var jaTem = {};
    if (registro.getLastRow() >= 2) {
      registro.getRange(2, 1, registro.getLastRow() - 1, 1).getValues().forEach(function (l) {
        if (l[0]) jaTem[String(l[0]).trim()] = true;
      });
    }

    var n = crm.getLastRow() - 1;
    if (n < 1) return;
    var dados = crm.getRange(2, 1, n, crm.getLastColumn()).getValues();
    dados.forEach(function (l) {
      var id = String(l[col['ID'] - 1]).trim();
      var marca = String(l[col['Marca'] - 1]).trim();
      var etapa = String(l[col['Etapa'] - 1]).trim();
      if (!id || id === 'LEAD-000' || !marca || jaTem[id]) return;
      if (A2_ETAPAS_COM_PASTA.indexOf(etapa) === -1) return;
      try {
        var pasta = criarPastaCliente(marca, cfg.PASTA_CLIENTES);
        registro.appendRow([id, marca, pasta.getUrl(), new Date()]);
        jaTem[id] = true;
        avisarDudaA2(id, marca, pasta.getUrl());
        registrarLog('A2', 'CRM em ' + etapa, id, 'OK', 'Pasta criada: ' + pasta.getUrl());
      } catch (err) {
        registrarLog('A2', 'CRM em ' + etapa, id, 'ERRO', err);
        avisarErro('A2', err);
      }
    });
  } catch (err) {
    registrarLog('A2', 'verificação', '', 'ERRO', err);
    avisarErro('A2', err);
  } finally {
    lock.releaseLock();
  }
}

/** Cria (ou reaproveita, se já existir com o mesmo nome) a pasta da marca e as subpastas. */
function criarPastaCliente(marca, pastaClientesId) {
  var raiz = DriveApp.getFolderById(pastaClientesId);
  var existentes = raiz.getFoldersByName(marca);
  var pasta = existentes.hasNext() ? existentes.next() : raiz.createFolder(marca);
  A2_SUBPASTAS.forEach(function (nome) {
    if (!pasta.getFoldersByName(nome).hasNext()) pasta.createFolder(nome);
  });
  return pasta;
}

function avisarDudaA2(id, marca, url) {
  var email = propriedade('EMAIL_DUDA', false);
  if (!email) return;
  MailApp.sendEmail(email, '[Casa Live] Pasta criada: ' + marca,
    'O cliente ' + marca + ' (' + id + ') entrou em onboarding.\n\n' +
    'A pasta dele já está pronta, com as subpastas Acordo, Fichas, Relatórios e Mídia:\n' + url + '\n\n' +
    'Próximos passos (Playbook E3):\n' +
    '1. Salvar o acordo assinado na subpasta Acordo.\n' +
    '2. Mandar o formulário de onboarding para o cliente.\n' +
    '3. Abrir o CRM, aba Onboarding, e ir marcando os itens.');
}

// ===================== Instalacao =====================

/**
 * Verificação geral: confere acesso às planilhas, pastas, colunas e Propriedades do script.
 * Não altera nada além de gravar o resultado no Log.
 */
function verificarInstalacao() {
  var problemas = [];
  var cfg = {};
  try { cfg = lerConfig(); } catch (e) { problemas.push('Não abri a planilha de automação: ' + e); }

  try {
    var leads = SpreadsheetApp.openById(cfg.CRM_ID).getSheetByName('Leads');
    if (!leads) problemas.push('CRM sem a aba Leads');
    else exigirColunas(mapaCabecalho(leads), ['ID', 'Marca', 'Etapa', 'Origem'], 'Leads');
  } catch (e) { problemas.push('CRM: ' + e); }

  ['PASTA_CLIENTES', 'PASTA_AUTOMACAO'].forEach(function (k) {
    try { DriveApp.getFolderById(cfg[k]).getName(); } catch (e) { problemas.push(k + ': ' + e); }
  });

  ['EMAIL_FELIPE', 'EMAIL_DUDA', 'EMAIL_KAIO'].forEach(function (k) {
    if (!propriedade(k, false)) problemas.push('Falta a Propriedade do script ' + k);
  });

  var resultado = problemas.length ? 'ERRO' : 'OK';
  registrarLog('Instalação', 'verificarInstalacao', '', resultado, problemas.join(' | ') || 'Tudo certo');
  console.log(resultado + ': ' + (problemas.join('\n') || 'Tudo certo'));
}
