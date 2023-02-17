import spacy
from jjcli import *

# modelo de linguagem para português
mod = spacy.load('pt_core_news_md')

lista = glob("Obra/*.txt")

pontuacoes = ["?", "...", ".",  "!"]

frases = 0
total = 0

for obra in lista:
    abrir_ficheiro = open(obra).read()
    for obra in abrir_ficheiro:
        if obra not in pontuacoes:
            frases = frases + 1
        elif obra in pontuacoes:
            total = total + 1


print(
    f"Comprimento médio das frases de todos os livros: {round(frases/ total)}")
