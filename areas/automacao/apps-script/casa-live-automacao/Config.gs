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
