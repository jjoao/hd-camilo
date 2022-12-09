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

    t = arvore.find("titulo")
    if t is not None:
        print(f"<H1>{t.text}</H1>")
        l = l + (f"<H1>{t.text}</H1>")
    for f in arvore.findall("fonte"):  
        print(f.attrib)
        output = f"<ol><li>{f.attrib['nome']}</li><li>{f.attrib['local']}</li><li>{f.attrib['local']}</li></ol>"
        print(output)
        l = l + (output)

h.write(l)