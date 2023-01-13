import spacy
from collections import Counter

# modelo de linguagem para português
mod = spacy.load('pt_core_news_md')

ficheiro = input("Nome do ficheiro: ")
# Obra/Camilo-A_mulher_fatal.txt
abrir_ficheiro = mod(open(ficheiro).read())

verbos = [
    palavra.text
    for palavra in abrir_ficheiro
    if palavra.pos_ == 'VERB' and palavra.is_punct == False]

print(Counter(verbos).most_common())
