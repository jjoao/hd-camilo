import spacy
from collections import Counter

# modelo de linguagem para português
mod = spacy.load('pt_core_news_md')

lista_personagens = []
lista_locais = []

ficheiro = input("Nome do ficheiro: ")
# Obra/Camilo-A_mulher_fatal.txt
abrir_ficheiro = mod(open(ficheiro).read())

for palavra in abrir_ficheiro.ents:
    if palavra.label_ == "LOC":
        lista_locais.append(palavra)
    elif palavra.label_ == "PER":
        lista_personagens.append(palavra)

print(
    f"Personagens com maior frequência no livro: {Counter(lista_personagens).most_common(5)}")
print(
    f"Lugares com maior frequência no livro: {Counter(lista_locais).most_common(5)}")
