import spacy

# modelo de linguagem para português
mod = spacy.load('pt_core_news_md')

pontuacoes = ["?", "...", ".",  "!"]

ficheiro = input("Nome do ficheiro: ")
# Obra/Camilo-A_mulher_fatal.txt
abrir_ficheiro = open(ficheiro).read()

frases = 0
total = 0

for palavra in abrir_ficheiro:
    if palavra not in pontuacoes:
        frases = frases + 1
    elif palavra in pontuacoes:
        total = total + 1

print(
    f"Comprimento médio das frases do livro: {round(frases / total)}")
