import spacy
from jjcli import *

# modelo de linguagem para português
mod = spacy.load('pt_core_news_md')

lista = glob("Obra/*.txt")

for obra in lista:
    print(obra)
