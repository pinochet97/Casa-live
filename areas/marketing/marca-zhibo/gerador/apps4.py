"""06: cartão digital (pptx 1080x1920 -> PDF), assinatura de e-mail (HTML + preview), papel timbrado (docx)."""
from deck import *
import json, shutil
from docx import Document
from docx.shared import Pt as DPt, Cm, RGBColor as DRGB
AP = f'{DIST}/03_Aplicacoes_da_Marca/06_Cartoes_e_Assinaturas'
F = lambda fr: FRONTS[fr]['file']
PX = 11.25 / 1080; px = lambda v: v * PX
html_jobs = []
for fr in ('Institucional', 'Agencia', 'Shop'):
    d = f'{AP}/{F(fr)}'
    # digital card
    p = new_deck('story'); w, h = SIZES['story']
    bgc = {'Institucional': INK, 'Agencia': INK, 'Shop': RED}[fr]
    s = slide(p, bgc); image(s, bg_image(fr, 'Escuro', 'Stories_9x16'), 0, 0, w, h)
    image_fit(s, logo(fr, 'Vertical', 'Branca' if bgc == RED else 'Negativa'), px(240), px(220), px(600), px(420), align='center')
    text(s, px(80), px(760), w - px(160), px(100), '[Nome Sobrenome]', size=44, bold=True, font=HEAD, color=PAPER, align='center')
    text(s, px(80), px(880), w - px(160), px(60), '[Cargo]', size=26, color=GOLD if bgc == INK else PAPER, align='center', bold=True)
    for i, (k, v) in enumerate([('WhatsApp', '[+55 00 00000-0000]'), ('E-mail', '[nome]@[dominio]'), ('Instagram', '@[perfil]'), ('TikTok', '@[perfil]'), ('Site', '[site]')]):
        y = px(1020) + i * px(140)
        box(s, px(120), y, w - px(240), px(115), fill=PAPER, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3)
        text(s, px(160), y, px(260), px(115), k, size=20, bold=True, color=GREY, anchor='middle')
        t = text(s, px(420), y, w - px(580), px(115), v, size=22, bold=True, color=INK, anchor='middle')
    notes(s, 'Para os contatos ficarem clicáveis: selecione cada texto, Inserir > Link, e use https://wa.me/55DDDNUMERO, mailto:email, https://instagram.com/perfil, https://tiktok.com/@perfil.')
    export(p, f'{d}/Cartao_Digital/Editaveis/{F(fr)}_Cartao_Digital_v01.pptx', f'{d}/Cartao_Digital/Finais_Digitais', f'{d}/Cartao_Digital/Finais_Digitais', 1080)
    # e-mail signature (HTML table, logo from a public URL to be set)
    os.makedirs(f'{d}/Assinatura_Email/Editaveis', exist_ok=True); os.makedirs(f'{d}/Assinatura_Email/Finais_Digitais', exist_ok=True)
    sig = f'''<!-- Assinatura de e-mail {FRONTS[fr]["name"]} v01. Troque LOGO_URL por um link público do PNG do logo (ex.: imagem do site). -->
<table cellpadding="0" cellspacing="0" style="font-family:Arial,Helvetica,sans-serif;color:#141010;font-size:13px;line-height:1.45">
<tr><td style="padding-right:16px;border-right:3px solid {RED}"><img src="LOGO_URL" alt="{FRONTS[fr]["name"]}" width="170" style="display:block"></td>
<td style="padding-left:16px"><b style="font-size:15px">[Nome Sobrenome]</b><br><span style="color:#5C504A">[Cargo] · {FRONTS[fr]["name"]}</span><br>
<a href="https://wa.me/55[DDDNUMERO]" style="color:#141010;text-decoration:none">WhatsApp [+55 00 00000-0000]</a><br>
<a href="mailto:[nome]@[dominio]" style="color:#141010;text-decoration:none">[nome]@[dominio]</a> · <a href="https://[site]" style="color:{RED};text-decoration:none">[site]</a></td></tr></table>'''
    open(f'{d}/Assinatura_Email/Editaveis/{F(fr)}_Assinatura_Email_v01.html', 'w').write(sig)
    prev = sig.replace('LOGO_URL', 'file://' + logo(fr, 'Horizontal', 'Colorida', 'svg'))
    html_jobs.append(dict(html=f'<html><body style="margin:0;padding:30px;background:#fff">{prev}</body></html>', w=700, h=170, out=f'{d}/Assinatura_Email/Finais_Digitais/{F(fr)}_Assinatura_Email_preview_v01.png', scale=2))
    # letterhead docx
    doc = Document(); sec = doc.sections[0]; sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.2); sec.top_margin = Cm(3); sec.bottom_margin = Cm(2.4)
    doc.styles['Normal'].font.name = 'Inter'; doc.styles['Normal'].font.size = DPt(11)
    sec.header.paragraphs[0].add_run().add_picture(logo(fr, 'Horizontal', 'Colorida'), height=Cm(1.0))
    fp = sec.footer.paragraphs[0]; r = fp.add_run(f'{FRONTS[fr]["name"]} · [Razão social] · CNPJ [__] · [endereço] · WhatsApp [__] · [e-mail] · [site]')
    r.font.size = DPt(8); r.font.color.rgb = DRGB(0x5C, 0x50, 0x4A)
    for line in ['[Cidade], [dia] de [mês] de [ano]', '', 'A/C [Nome]', '[Empresa]', '', 'Assunto: [assunto]', '', '[Texto do documento.]', '', 'Atenciosamente,', '', '[Nome]', '[Cargo]']:
        doc.add_paragraph(line)
    os.makedirs(f'{d}/Papel_Timbrado/Editaveis', exist_ok=True)
    doc.save(f'{d}/Papel_Timbrado/Editaveis/{F(fr)}_Papel_Timbrado_v01.docx')
json.dump(html_jobs, open(f'{B}/jobs_apps4.json', 'w'))
print('ok')
