from brand import *
import json, shutil, zipfile
CF=f'{DIST}/01_Identidade_Visual/Cores_e_Fontes'
for d in ('Editaveis','Finais_Digitais','Impressao'): os.makedirs(f'{CF}/{d}',exist_ok=True)
shutil.copy(f'{B}/figs/paleta.png', f'{CF}/Finais_Digitais/Zhibo_Paleta_de_Cores_v01.png')
# palette PDF (print reference)
html=open(f'{B}/jobs_html.json').read(); jobs=[j for j in json.loads(html) if j['out'].endswith('paleta.png')]
jobs[0]['pdf']=f'{CF}/Impressao/Zhibo_Paleta_de_Cores_v01.pdf'; jobs[0]['out']=f'{B}/figs/paleta_tmp.png'
json.dump(jobs,open(f'{B}/j_pal.json','w'))
# fonts zip (SIL Open Font License allows redistribution)
with zipfile.ZipFile(f'{CF}/Editaveis/Zhibo_Fontes_Unbounded_Inter_v01.zip','w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(os.listdir(f'{B}/fonts')): z.write(f'{B}/fonts/{f}', f)
rows=''.join(f'<tr><td><b>{n}</b></td><td style="background:{h};width:60px"></td><td>{h}</td><td>{", ".join(map(str,rgb(h)))}</td><td>{" ".join(map(str,cmyk(h)))}</td><td>{g}</td><td>{role}</td></tr>' for n,h,role,g in PALETTE)
doc=f'''<html><head><meta charset="utf-8"></head><body style="font-family:Inter,Arial">
<h1>Zhibo — Guia de cores e fontes (v01)</h1>
<p>Fonte da verdade: Manual da Marca (01_Identidade_Visual/Manual_da_Marca). Este guia resume os códigos para quem vai produzir peças.</p>
<h2>Cores</h2>
<table border="1" cellpadding="6" style="border-collapse:collapse"><tr><th>Nome</th><th>Cor</th><th>HEX</th><th>RGB (digital)</th><th>CMYK (impressão)</th><th>Grupo</th><th>Uso</th></tr>{rows}</table>
<p><b>CMYK:</b> valores de referência, convertidos do RGB. Antes de imprimir, peça prova de cor à gráfica. Pantone: [A PREENCHER com a gráfica, se necessário].</p>
<h2>Cor de apoio por frente</h2>
<ul><li><b>Zhibo (institucional):</b> Tinta #141010</li><li><b>Zhibo Agência:</b> Ouro Oferta #FFC42E</li><li><b>Zhibo Shop:</b> Vermelho Live #E5262A</li></ul>
<p>O vermelho do símbolo e a Tinta dos textos são iguais nas três frentes. A cor de apoio só muda fundos, selos, destaques e avatar.</p>
<h2>Fontes</h2>
<table border="1" cellpadding="6" style="border-collapse:collapse"><tr><th>Uso</th><th>Fonte</th><th>Peso</th><th>Link</th></tr>
<tr><td>Títulos</td><td>Unbounded</td><td>Bold (700)</td><td><a href="https://fonts.google.com/specimen/Unbounded">fonts.google.com/specimen/Unbounded</a></td></tr>
<tr><td>Subtítulos e chamadas</td><td>Unbounded</td><td>Medium (500)</td><td><a href="https://fonts.google.com/specimen/Unbounded">fonts.google.com/specimen/Unbounded</a></td></tr>
<tr><td>Textos</td><td>Inter</td><td>Regular (400)</td><td><a href="https://fonts.google.com/specimen/Inter">fonts.google.com/specimen/Inter</a></td></tr>
<tr><td>Destaques e rótulos</td><td>Inter</td><td>SemiBold (600)</td><td><a href="https://fonts.google.com/specimen/Inter">fonts.google.com/specimen/Inter</a></td></tr>
<tr><td>Nome “zhibo” no logo</td><td>Unbounded</td><td>ExtraBold (800), em curvas</td><td>Não redigitar: use os arquivos de logo</td></tr></table>
<p>As duas famílias são gratuitas (licença SIL Open Font License). No Google Slides e no Google Docs, escolha em “Mais fontes”. Os arquivos .ttf estão em Cores_e_Fontes/Editaveis.</p>
<h2>Fotografia: orientação rápida</h2>
<ul><li>Só fotos reais: casa, equipe, lives realizadas e produtos de clientes com autorização.</li>
<li>Luz clara e frontal; cores naturais; contraste leve; sem filtros coloridos.</li>
<li>Logo branco sobre área escura da foto, ou dentro de faixa Tinta, respeitando a área de proteção.</li>
<li>Guardar a autorização de uso de imagem (host, cliente, produto) em 04_Referencias_e_Insumos.</li></ul>
</body></html>'''
open(f'{CF}/Editaveis/Zhibo_Guia_Cores_e_Fontes_v01.html','w').write(doc)
print('ok')
