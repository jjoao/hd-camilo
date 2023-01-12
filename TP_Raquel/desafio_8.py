import spacy
from collections import Counter

# modelo de linguagem para português
mod = spacy.load('pt_core_news_md')

lista = []

ficheiro = input("Nome do ficheiro: ")
# Obra/Camilo-A_mulher_fatal.txt
abrir_ficheiro = mod(open(ficheiro).read())

for palavra in abrir_ficheiro.ents:
    if palavra.label_ == "LOC" or palavra.label_ == "ORG" or palavra.label_ == "PER":
        lista.append(palavra)

print(Counter(lista).most_common())
