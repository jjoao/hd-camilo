import spacy

# modelo de linguagem para português
mod = spacy.load('pt_core_news_md')

ficheiro = input("Nome do ficheiro: ")
# Obra/Camilo-A_mulher_fatal.txt
abrir_ficheiro = mod(open(ficheiro).read())

cont = 0
for palavra in abrir_ficheiro:
    if palavra.pos_ == "VERB":
        print(f'"{palavra}" que é do verbo: "{palavra.lemma_}"')
        cont = cont + 1

print("Número de verbos:", cont)
