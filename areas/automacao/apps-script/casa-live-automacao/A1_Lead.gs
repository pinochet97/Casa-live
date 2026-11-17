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
