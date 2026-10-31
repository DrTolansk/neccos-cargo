#!/usr/bin/env python3
"""Restaura as sete imagens publicas do site e gera PDF institucional."""
from pathlib import Path
from urllib.request import Request, urlopen
from hashlib import sha256
from shutil import copyfile
ROOT=Path(__file__).resolve().parent.parent
SITE="https://neccos-cargo.joasmaciel588.workers.dev"
HASHES={
"favicon.png":"80507f99fa0a4fcebd57da6c7a59342074517d869fd51f5c10340dfbbf4fb100",
"operacao-logistica.webp":"f643b43ff7257e32344e68090db770300e00855b3b9df33211e1f2773103e37a",
"compartilhamento.jpg":"adadf35b7b22eb30330994c915c7ee277849f3319239a683798fc5680278ad9e",
"logo-horizontal.webp":"02179fff94ec68d9eeffdee8e7c417668bf86ff980bf9e7a612cecf49c632743",
"marca-completa.webp":"4aabbe67a735a1c1a8e5b76c3b44ed7b92c52fe36237541b43b04f8f5803cf43",
"frete-e-cargas.webp":"fca303ebd377481e402b635486af529d3192ef05956b49a83dccc0eda117b203",
"banner-neccos.webp":"e6fa92be603ce9b295a5a77369c533f643bc7e70020281ce722357706d2d939d"}
folder=ROOT/"website/assets"
folder.mkdir(parents=True,exist_ok=True)
for name,expected in HASHES.items():
    path=folder/name
    if not path.exists() or sha256(path.read_bytes()).hexdigest()!=expected:
        with urlopen(Request(SITE+"/assets/"+name,headers={"User-Agent":"Mozilla/5.0"}),timeout=35) as r:
            data=r.read(1500000)
        if sha256(data).hexdigest()!=expected:
            raise RuntimeError("Arquivo inesperado: "+name)
        path.write_bytes(data)
    print("OK",name)
(ROOT/"assets").mkdir(exist_ok=True)
for name in ("banner-neccos.webp","logo-horizontal.webp"):
    copyfile(folder/name,ROOT/"assets"/name)
html=ROOT/"website/index.html"
html.write_text(html.read_text().replace(SITE+"/assets/","assets/"))
readme=ROOT/"README.md"
readme.write_text(readme.read_text().replace(SITE+"/assets/banner-neccos.webp","assets/banner-neccos.webp"))
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
pdfmetrics.registerFont(TTFont("DVS","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVS-Bold","/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
W,H=A4
c=canvas.Canvas(str(ROOT/"APRESENTACAO-PARCEIROS.pdf"),pagesize=A4)
c.setTitle("NECCOS Cargo - Apresentacao para parceiros")
def lines(block,x=48,y=630,leading=19,maxlen=88):
    import textwrap
    c.setFont("DVS",9)
    for item in block:
        for line in textwrap.wrap(item,width=maxlen):
            c.drawString(x,y,line)
            y-=leading
        y-=12
    return y
def title(s):
    c.setFillColorRGB(.09,.2,.11);c.setFont("DVS-Bold",20)
    c.drawString(48,755,s);c.setFillColorRGB(0,0,0)
logo=Image.open(folder/"logo-horizontal.webp").convert("RGB")
tmp=folder/"_temp_logo.jpg";logo.save(tmp)
c.drawImage(str(tmp),48,655,width=180,height=180*logo.height/logo.width,mask='auto')
title("NECCOS Cargo")
lines(["Conectando cargas. Movendo negocios.","Agenciamento de Cargas e Gestao de Fretes | Osasco - SP","Visao: conectar demandas de transporte a parceiros aptos, organizando","programacao, documentacao e acompanhamento operacional.","Situacao: marca e site publicados; formalizacao empresarial e dominio pendentes.","Servicos em planejamento: agenciamento, gestao de fretes, cadastro de","parceiros, suporte documental e acompanhamento."])
c.setFont("DVS",8);c.drawString(48,80,SITE)
c.showPage()
title("Crescimento e parcerias")
lines(["NECCOS HUB: projeto de um sistema proprio para demandas, alocacao,","cadastros restritos, acompanhamento e indicadores. Nao esta em producao.","Etapas: formalizacao, validacao comercial, pilotos medidos, processos","padronizados, MVP tecnologico e escala sustentavel.","Parcerias: clientes, transportadores, tecnologia e dialogo com potenciais","investidores mediante orcamento, requisitos e diligencia.","Dados a comprovar: custos, capital de giro, comissoes, fluxo de caixa,","demanda contratada, riscos, indicadores e governanca.","Documento exploratorio; nao e oferta de investimento nem promessa de retorno."])
c.save()
tmp.unlink(missing_ok=True)
print("Concluido: imagens locais e apresentacao PDF")
