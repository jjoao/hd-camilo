import spacy
# importação da biblioteca do "spacy"

apt = spacy.load('pt_core_news_md')
# a variável "apt" traz para o script o modelo português de linguagem do "spacy"

obra = input("Obra Camillo: ")
# a variável "obra" recebe o caminho de um ficheiro (Obra/Camilo-A_Brasileira_de_Prazins.txt)

livro = open(obra).read()
"""a variável "livro" abre e faz uma leitura do respectivo ficheiro 
tendo em conta o modelo português da biblioteca"""

frases = 0
for sent in livro.sents:
	frases = frases + 1

""" a variável "frases" é criada para contar o número de ocorrências em que uma pontuação utilizada
para encerrar uma frase, ou seja, uma frase """

print("Tokens:" + {len(apt(livro))}) 

print("Frases:" + {frases})

#Obra/Camilo-O_que_fazem_mulheres.txt