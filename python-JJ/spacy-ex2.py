
from jjcli import *
obras_camilo = glob("../Obra/**/*txt", recursive=True)
print(obras_camilo)

l5 = obras_camilo[5]             ## nome do quinto livro
txt = open(l5).read()            ## conteudo do quinto livro

import spacy
apt = spacy.load('pt_core_news_md')

txtanal = apt(txt)

cont = 0
for w in txtanal:
#    print(w, w.pos_, w.lemma_ )
    if w.pos_ == "VERB":
        print(w, w.lemma_ )
        cont = cont + 1

print("Numero de verbos",cont)
        
       

