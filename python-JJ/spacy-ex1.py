"""
## Instalação
# spacy   -- nlp

 sudo pip install -U spacy
 python -m spacy download pt
 python -m spacy download  pt_core_news_sm
                           pt_core_news_md
                           pt_core_news_lg
No programa:
 spacy.load('pt_core_news_sm')
"""

txt = """Viva o Pedro Henriques e mais os alunos da Universidade do Minho.
O Rui escreveu um lindo programa.
O gato está a miar.
O cão está a ladrar.
"""

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
        
       

