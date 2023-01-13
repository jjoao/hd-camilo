import spacy

apt = spacy.load('pt_core_news_md')

obra = input("Obra Camillo: ")
livro = apt(open(obra).read())

verbos = 0
for palavra in livro:
	if palavra.pos_ == "VERB":
		print(palavra, palavra.lemma_)
		verbos = verbos + 1
		
print("Verbos:", verbos)

#C:\Users\Utilizador\Desktop\Trabalho PI\Obra\Camilo-O_que_fazem_mulheres.txt