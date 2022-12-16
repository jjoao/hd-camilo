
from jjcli import *

with open("Camilo-Amor_de_Perdicao.txt", encoding="utf8") as f:
     txt = f.read()

import spacy
nlp = spacy.load('pt_core_news_lg')

txtanal = nlp(txt)

cont = 0
for ent in txtanal.ents:
#    print(w, w.pos_, w.lemma_ )
#    if w.pos_ == "VERB":
        print(ent, ent.label_)
        cont = cont + 1

print("Número de ents",cont)
