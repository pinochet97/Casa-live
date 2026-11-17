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
