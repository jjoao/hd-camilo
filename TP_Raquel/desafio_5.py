import spacy

# modelo de linguagem para português
mod = spacy.load('pt_core_news_md')

pontuacoes = ["?", "...", ".",  "!"]

ficheiro = input("Nome do ficheiro: ")
# Obra/Camilo-A_mulher_fatal.txt
abrir_ficheiro = open(ficheiro).read()

cont = 0
for frase in abrir_ficheiro:
    if frase in pontuacoes:
        cont = cont + 1

print(f"Número de tokens: {len(mod(abrir_ficheiro))}")
print(f"Número de frases: {cont}")
