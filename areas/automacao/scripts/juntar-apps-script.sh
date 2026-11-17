#!/usr/bin/env bash
# Junta todos os .gs do projeto num arquivo só, para colar no Apps Script de uma vez.
# Rodar sempre que mudar algum .gs:  bash areas/automacao/scripts/juntar-apps-script.sh
set -euo pipefail
cd "$(dirname "$0")/../apps-script"
SAIDA=COLAR-NO-APPS-SCRIPT.gs
{
  echo "/**"
  echo " * CASA LIVE — AUTOMAÇÕES (arquivo único para colar no Apps Script)"
  echo " * Gerado por scripts/juntar-apps-script.sh. NÃO editar aqui: edite os arquivos em casa-live-automacao/ e rode o script de novo."
  echo " */"
  for f in Config Log Ids A1_Lead A2_PastaCliente Instalacao; do
    echo ""; echo "// ===================== $f ====================="; echo ""
    cat "casa-live-automacao/$f.gs"
  done
} > "$SAIDA"
echo "Gerado: apps-script/$SAIDA"
