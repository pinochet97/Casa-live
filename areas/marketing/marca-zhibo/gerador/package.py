"""Builds the upload tree (curated files + zips) mirroring the Drive structure, and upload_manifest.json."""
import os, glob, shutil, zipfile, json
from pypdf import PdfWriter
from brand import DIST, B, FRONTS, PALETTE, rgb, cmyk
UP = f'{B}/up/Zhibo_Marca_e_Comercial'
shutil.rmtree(f'{B}/up', ignore_errors=True)
items = []   # dict(path=<drive path rel to root>, src=<local>, kind=<pptx|docx|xlsx|html_doc|file>)
def put(rel, src, kind='file'):
    dst = f'{UP}/{rel}'; os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy(src, dst); items.append(dict(path=rel, src=dst, kind=kind))
def zipit(rel, files, arc_base=None):
    dst = f'{UP}/{rel}'; os.makedirs(os.path.dirname(dst), exist_ok=True)
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(files): z.write(f, os.path.relpath(f, arc_base) if arc_base else os.path.basename(f))
    items.append(dict(path=rel, src=dst, kind='file'))
def merge(rel, pdfs):
    dst = f'{UP}/{rel}'; os.makedirs(os.path.dirname(dst), exist_ok=True); w = PdfWriter()
    for p in pdfs: w.append(p)
    w.write(dst); items.append(dict(path=rel, src=dst, kind='file'))
D = DIST; I = '01_Identidade_Visual'
# ---------- 01 logos
for fr in ('Zhibo_Institucional', 'Zhibo_Agencia', 'Zhibo_Shop'):
    L = f'{D}/{I}/Logos/{fr}'; R = f'{I}/Logos/{fr}'
    zipit(f'{R}/Editaveis/{fr}_Logos_SVG_v01.zip', glob.glob(f'{L}/Editaveis/*.svg'))
    zipit(f'{R}/Finais_Digitais/{fr}_Logos_PNG_v01.zip', glob.glob(f'{L}/Finais_Digitais/*.png'))
    zipit(f'{R}/Impressao/{fr}_Logos_PDF_Vetorial_v01.zip', glob.glob(f'{L}/Impressao/*.pdf'))
    for cw in ('Colorida', 'Negativa', 'Branca'): put(f'{R}/Finais_Digitais/{fr}_Logo_Horizontal_{cw}_v01.png', f'{L}/Finais_Digitais/{fr}_Logo_Horizontal_{cw}_v01.png')
    put(f'{R}/Finais_Digitais/{fr}_Logo_Vertical_Colorida_v01.png', f'{L}/Finais_Digitais/{fr}_Logo_Vertical_Colorida_v01.png')
    put(f'{R}/Editaveis/{fr}_Logo_Horizontal_Colorida_v01.svg', f'{L}/Editaveis/{fr}_Logo_Horizontal_Colorida_v01.svg')
    put(f'{R}/Impressao/{fr}_Logo_Horizontal_Colorida_v01.pdf', f'{L}/Impressao/{fr}_Logo_Horizontal_Colorida_v01.pdf')
S = f'{D}/{I}/Logos/Zhibo_Simbolo'
put(f'{I}/Logos/Zhibo_Simbolo/Editaveis/Zhibo_Simbolo_Vermelho_v01.svg', f'{S}/Editaveis/Zhibo_Simbolo_Vermelho_v01.svg')
put(f'{I}/Logos/Zhibo_Simbolo/Finais_Digitais/Zhibo_Simbolo_Vermelho_v01.png', f'{S}/Finais_Digitais/Zhibo_Simbolo_Vermelho_v01.png')
put(f'{I}/Logos/Zhibo_Simbolo/Impressao/Zhibo_Simbolo_Vermelho_v01.pdf', f'{S}/Impressao/Zhibo_Simbolo_Vermelho_v01.pdf')
zipit(f'{I}/Logos/Zhibo_Simbolo/Zhibo_Simbolo_Todas_as_Cores_v01.zip', glob.glob(f'{S}/*/*.*'), S)
MD = f'{D}/{I}/Logos/Marca_dAgua'
for fr in ('Zhibo_Institucional', 'Zhibo_Agencia', 'Zhibo_Shop'):
    put(f'{I}/Logos/Marca_dAgua/Finais_Digitais/{fr}_Marca_dAgua_Branca_v01.png', f'{MD}/Finais_Digitais/{fr}_Marca_dAgua_Branca_v01.png')
zipit(f'{I}/Logos/Marca_dAgua/Zhibo_Marcas_dAgua_Todas_v01.zip', glob.glob(f'{MD}/*/*.*'), MD)
AV = f'{D}/{I}/Avatares'
for fr in ('Zhibo_Institucional', 'Zhibo_Agencia', 'Zhibo_Shop'): put(f'{I}/Avatares/Finais_Digitais/{fr}_Avatar_v01.png', f'{AV}/Finais_Digitais/{fr}_Avatar_v01.png')
zipit(f'{I}/Avatares/Editaveis/Zhibo_Avatares_SVG_v01.zip', glob.glob(f'{AV}/Editaveis/*.svg'))
CF = f'{D}/{I}/Cores_e_Fontes'
put(f'{I}/Cores_e_Fontes/Finais_Digitais/Zhibo_Paleta_de_Cores_v01.png', f'{CF}/Finais_Digitais/Zhibo_Paleta_de_Cores_v01.png')
put(f'{I}/Cores_e_Fontes/Impressao/Zhibo_Paleta_de_Cores_v01.pdf', f'{CF}/Impressao/Zhibo_Paleta_de_Cores_v01.pdf')
put(f'{I}/Cores_e_Fontes/Editaveis/Zhibo_Guia_Cores_e_Fontes_v01.html', f'{CF}/Editaveis/Zhibo_Guia_Cores_e_Fontes_v01.html', 'html_doc')
put(f'{I}/Cores_e_Fontes/Editaveis/Zhibo_Fontes_Unbounded_Inter_v01.zip', f'{CF}/Editaveis/Zhibo_Fontes_Unbounded_Inter_v01.zip')
EG = f'{D}/{I}/Elementos_Graficos'
zipit(f'{I}/Elementos_Graficos/Icones/Zhibo_Icones_SVG_PNG_v01.zip', glob.glob(f'{EG}/Icones/*/*.*'), f'{EG}/Icones')
zipit(f'{I}/Elementos_Graficos/Padroes/Zhibo_Padroes_SVG_PNG_v01.zip', glob.glob(f'{EG}/Padroes/*/*.*'), f'{EG}/Padroes')
put(f'{I}/Elementos_Graficos/Icones/Zhibo_Icones_Visao_Geral_v01.png', f'{B}/figs/icones.png')
for fr in ('Zhibo_Institucional', 'Zhibo_Agencia', 'Zhibo_Shop'):
    zipit(f'{I}/Elementos_Graficos/Fundos/{fr}_Fundos_PNG_v01.zip', glob.glob(f'{EG}/Fundos/Finais_Digitais/{fr}_*.png'))
zipit(f'{I}/Elementos_Graficos/Fundos/Zhibo_Fundos_SVG_Editaveis_v01.zip', glob.glob(f'{EG}/Fundos/Editaveis/*.svg'))
put(f'{I}/Elementos_Graficos/Fundos/Zhibo_Shop_Fundo_Apresentacao_16x9_Escuro_v01.png', f'{EG}/Fundos/Finais_Digitais/Zhibo_Shop_Fundo_Apresentacao_16x9_Escuro_v01.png')
MM = f'{D}/{I}/Manual_da_Marca'
put(f'{I}/Manual_da_Marca/Editaveis/Zhibo_Manual_da_Marca_v01.pptx', f'{MM}/Editaveis/Zhibo_Manual_da_Marca_v01.pptx', 'pptx')
put(f'{I}/Manual_da_Marca/Finais_Digitais/Zhibo_Manual_da_Marca_v01.pdf', f'{MM}/Finais_Digitais/Zhibo_Manual_da_Marca_v01.pdf')
# ---------- 02 mídia kit
MK = f'{D}/02_Midia_Kit'
for f in sorted(glob.glob(f'{MK}/0[123]_*/Editaveis/*.pptx')): put(os.path.relpath(f, D), f, 'pptx')
for f in sorted(glob.glob(f'{MK}/0[123]_*/Finais_Digitais/*.pdf')): put(os.path.relpath(f, D), f)
for f in sorted(glob.glob(f'{MK}/04_Resumos_Comerciais/Editaveis/*.pptx')): put(os.path.relpath(f, D), f, 'pptx')
for f in sorted(glob.glob(f'{MK}/04_Resumos_Comerciais/Finais_Digitais/*')):
    if f.endswith('-1.png'): put(os.path.relpath(f, D).replace('-1.png', '.png'), f)
    elif f.endswith('.pdf'): put(os.path.relpath(f, D), f)
zipit('02_Midia_Kit/05_Imagens_Utilizadas/Zhibo_Midia_Kit_Imagens_v01.zip', glob.glob(f'{EG}/Fundos/Finais_Digitais/*Apresentacao_16x9_Escuro*.png') + glob.glob(f'{EG}/Icones/Finais_Digitais/*Vermelho*.png'))
# ---------- 03 aplicações
AP = f'{D}/03_Aplicacoes_da_Marca'; A = '03_Aplicacoes_da_Marca'
for f in sorted(glob.glob(f'{AP}/0[1234]_*/**/*.*', recursive=True)):
    rel = os.path.relpath(f, D)
    if '/Carrossel_PNG/' in rel: continue
    if f.endswith('.pptx'): put(rel, f, 'pptx')
    elif f.endswith('.docx'): put(rel, f, 'docx')
    elif f.endswith('.xlsx'): put(rel, f, 'xlsx')
    elif f.endswith('.pdf'): put(rel, f)
for fr in ('Zhibo_Agencia', 'Zhibo_Shop'):
    zipit(f'{A}/04_Cases_e_Portfolio/{fr}/Finais_Digitais/{fr}_Case_Carrossel_PNG_v01.zip', glob.glob(f'{AP}/04_Cases_e_Portfolio/{fr}/Finais_Digitais/Carrossel_PNG/*.png'))
    R = f'{AP}/05_Redes_Sociais/{fr}'
    for f in sorted(glob.glob(f'{R}/Editaveis/*.pptx')): put(os.path.relpath(f, D), f, 'pptx')
    for f in sorted(glob.glob(f'{R}/Finais_Digitais/*.pdf')): put(os.path.relpath(f, D), f)
    put(f'{A}/05_Redes_Sociais/{fr}/Finais_Digitais/{fr}_Avatar_v01.png', f'{R}/Finais_Digitais/{fr}_Avatar_v01.png')
    zipit(f'{A}/05_Redes_Sociais/{fr}/Finais_Digitais/{fr}_Feed_PNG_v01.zip', glob.glob(f'{R}/Finais_Digitais/Feed_PNG/*.png'))
    zipit(f'{A}/05_Redes_Sociais/{fr}/Finais_Digitais/{fr}_Stories_PNG_v01.zip', glob.glob(f'{R}/Finais_Digitais/Stories_PNG/*.png'))
    zipit(f'{A}/05_Redes_Sociais/{fr}/Capas_Destaques/{fr}_Capas_Destaques_v01.zip', glob.glob(f'{R}/Capas_Destaques/*/*.*'), f'{R}/Capas_Destaques')
for fr in ('Zhibo_Institucional', 'Zhibo_Agencia', 'Zhibo_Shop'):
    C = f'{AP}/06_Cartoes_e_Assinaturas/{fr}'; Rr = f'{A}/06_Cartoes_e_Assinaturas/{fr}'
    put(f'{Rr}/Cartao_Digital/Editaveis/{fr}_Cartao_Digital_v01.pptx', f'{C}/Cartao_Digital/Editaveis/{fr}_Cartao_Digital_v01.pptx', 'pptx')
    put(f'{Rr}/Cartao_Digital/Finais_Digitais/{fr}_Cartao_Digital_v01.pdf', f'{C}/Cartao_Digital/Finais_Digitais/{fr}_Cartao_Digital_v01.pdf')
    merge(f'{Rr}/Cartao_Impresso/Impressao/{fr}_Cartao_Impresso_90x50_Frente_Verso_v01.pdf', sorted(glob.glob(f'{C}/Cartao_Impresso/Impressao/*.pdf')))
    zipit(f'{Rr}/Cartao_Impresso/Editaveis/{fr}_Cartao_Impresso_SVG_v01.zip', glob.glob(f'{C}/Cartao_Impresso/Editaveis/*.svg'))
    put(f'{Rr}/Cartao_Impresso/Finais_Digitais/{fr}_Cartao_Impresso_Frente_preview_v01.png', glob.glob(f'{C}/Cartao_Impresso/Finais_Digitais/*Frente*.png')[0])
    put(f'{Rr}/Assinatura_Email/Editaveis/{fr}_Assinatura_Email_v01.html', f'{C}/Assinatura_Email/Editaveis/{fr}_Assinatura_Email_v01.html')
    put(f'{Rr}/Assinatura_Email/Finais_Digitais/{fr}_Assinatura_Email_preview_v01.png', f'{C}/Assinatura_Email/Finais_Digitais/{fr}_Assinatura_Email_preview_v01.png')
    put(f'{Rr}/Papel_Timbrado/Editaveis/{fr}_Papel_Timbrado_v01.docx', f'{C}/Papel_Timbrado/Editaveis/{fr}_Papel_Timbrado_v01.docx', 'docx')
for piece in sorted(glob.glob(f'{AP}/07_Folhetos_e_Banners/*/*')) + sorted(glob.glob(f'{AP}/08_Espaco_Fisico/*')):
    rel = os.path.relpath(piece, D); name = os.path.basename(piece)
    pdfs = sorted(glob.glob(f'{piece}/Impressao/*.pdf'), key=lambda p: ('Verso' in p or 'Costas' in p, p))
    base = os.path.basename(pdfs[0]).replace('_Frente_v01', '_v01').replace('_Frente_Peito_v01', '_v01')
    if len(pdfs) > 1: merge(f'{rel}/Impressao/{base.replace("_v01", "_Frente_Verso_v01")}', pdfs)
    else: put(f'{rel}/Impressao/{base}', pdfs[0])
    zipit(f'{rel}/Editaveis/{base.replace("_v01.pdf", "_SVG_v01.zip")}', glob.glob(f'{piece}/Editaveis/*.svg'))
    pv = sorted(glob.glob(f'{piece}/Finais_Digitais/*.png'))
    put(f'{rel}/Finais_Digitais/{os.path.basename(pv[0])}', pv[0])
    for sm in glob.glob(f'{piece}/Simulacoes/*.png'): put(f'{rel}/Simulacoes/{os.path.basename(sm)}', sm)
for fr in ('Zhibo_Shop', 'Zhibo_Agencia'):
    L = f'{AP}/09_Materiais_para_Lives/{fr}'
    put(f'{A}/09_Materiais_para_Lives/{fr}/Editaveis/{fr}_Materiais_para_Lives_Templates_v01.pptx', f'{L}/Editaveis/{fr}_Materiais_para_Lives_Templates_v01.pptx', 'pptx')
    put(f'{A}/09_Materiais_para_Lives/{fr}/Finais_Digitais/{fr}_Materiais_para_Lives_Templates_v01.pdf', f'{L}/Finais_Digitais/{fr}_Materiais_para_Lives_Templates_v01.pdf')
    zipit(f'{A}/09_Materiais_para_Lives/{fr}/Finais_Digitais/{fr}_Materiais_para_Lives_PNG_v01.zip', glob.glob(f'{L}/Finais_Digitais/PNG/*.png'))
CO = f'{AP}/09_Materiais_para_Lives/Coassinatura'
zipit(f'{A}/09_Materiais_para_Lives/Coassinatura/Zhibo_Coassinatura_SVG_PNG_PDF_v01.zip', glob.glob(f'{CO}/*/*.*'), CO)
for f in sorted(glob.glob(f'{CO}/Finais_Digitais/*Colorida*.png')): put(f'{A}/09_Materiais_para_Lives/Coassinatura/{os.path.basename(f)}', f)
json.dump(items, open(f'{B}/upload_manifest.json', 'w'), indent=0)
folders = sorted({os.path.dirname(i['path']) for i in items})
allf = set()
for f in folders:
    parts = f.split('/')
    for k in range(1, len(parts) + 1): allf.add('/'.join(parts[:k]))
for extra in ['04_Referencias_e_Insumos']: allf.add(extra)
print('files', len(items), 'folders', len(allf), 'kinds', {k: sum(1 for i in items if i['kind'] == k) for k in {i['kind'] for i in items}})
