import xml.etree.ElementTree as ET
from jjcli import *

lista=glob("xmls/*.xml", recursive=True)
print(len(lista))
print(lista)

h = open("rendx.html", "w")
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
        output = f"<ul><li>{f.attrib['nome']}</li><li>{f.attrib['revista']}</li><li>{f.attrib['numero']}</li><li>{f.attrib['data']}</li><li>{f.attrib['local']}</li></ul>"
        print(output)
        l = l + (output)

h.write(l)