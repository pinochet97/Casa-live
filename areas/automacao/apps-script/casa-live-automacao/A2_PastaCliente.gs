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
