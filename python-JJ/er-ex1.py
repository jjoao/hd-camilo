from jjcli import *

with open("Camilo-Amor_de_Perdicao.txt",encoding="utf8") as f:
    livro = f.read()

caps =  re.split(r'CAPÍTULO', livro)

num=0
for c in caps:
#    print(num, len(c))
    anos = re.findall(r'\d{4}', c)
    print("Capítulo",num, anos)
    num = num +1

#anos = re.findall(r'\d{4}', livro)

