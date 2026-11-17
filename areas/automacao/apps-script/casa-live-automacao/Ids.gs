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
