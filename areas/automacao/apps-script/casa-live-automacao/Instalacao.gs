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
