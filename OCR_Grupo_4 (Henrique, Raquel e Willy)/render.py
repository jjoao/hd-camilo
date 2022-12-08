import xml.etree.ElementTree as ET
from jjcli import *

lista=glob("../recortes/**/*.xml", recursive=True)
print(len(lista))
print(lista)

h = open("rec.html", "w")
l = ""

for filename in lista:
    try:
        arvore = ET.parse(filename).getroot()
    except Exception as erro:
        print("Erro no ficheiro", filename, erro)
        continue
   
    h = open("rec.html", "w")
    t = arvore.find("titulo")
    if t is not None:
        print(f"<H1>{t.text}</H1>")
        l = l + (f"<H1>{t.text}</H1>")
    for f in arvore.findall("fonte"):  
        print(f.attrib)
        print(f"<ol><li>{f.attrib['nome']}</li><li>{f.attrib['data']}</li></ol>")
        l = l + (f"<ol><li>{f.attrib['nome']}</li><li>{f.attrib['data']}</li></ol>")

h.write(l)