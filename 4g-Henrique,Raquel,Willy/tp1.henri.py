# -*- coding: utf-8 -*-
import os, re, sys
from operator import itemgetter
import pydoc
import spacy
try:
	nlp = spacy.load("pt_core_news_md")
except:
	print("install spacy's 'pt_core_news_md' portuguese package"
		  "\npython -m spacy download pt_core_news_md")
	exit()

nlp=spacy.load('pt_core_news_md')

interactive = False if len(sys.argv[1:]) == 0 else True
if interactive: from pick import pick

markdown = '''
~~~
title: Trabalho Prático 1
author: Henrique
~~~

# Resolução dos [Enunciados](https://github.com/jjoao/hd-camilo/blob/main/Doc/TP/tp1.md) propostos

## 1. Lista das obras de camilo.
Listar as obras de Camilo existentes na pasta `Obra/` do nosso repositório.
Ou seja apresentar a lista dos ficheiros de texto existentes nessa pasta.

'''

def spacyTagTxt(paragraphs,ents):
	tagChars = 0
	for w, beg, end, typ in ents:
		beg += tagChars
		end += tagChars
		if typ == 'PER':
			typ = 'persName'
		elif typ == 'LOC':
			typ = 'placeName'
		tagged = "<"+typ+">"+w+"</"+typ+">"
		paragraphs = paragraphs[0:beg]+tagged+paragraphs[end:]
		tagChars+=len(tagged)-len(w)
	return paragraphs

class Book:
	def __init__(self,filepath):
		self.filename = filepath[8:]
		baseurl = 'https://raw.githubusercontent.com/'
		repo = 'jjoao/hd-camilo'
		branch = '/main'
		folder = '/Obra/'
		self.url= baseurl+repo+branch+folder+self.filename
		self.title = re.sub('_',' ',filepath[7:-4])[8:]
		self.author = filepath.split('-')[0][8:]
	
	def stats(self, action=''):
		book = '../Obra/' + self.filename
		with open(book, 'r') as file:  content = file.read()
		doc = nlp(content)
		self.ents = [(e.text, e.label_, e.start_char, e.end_char) for e in doc.ents]

		def sentences():
			self.sents, l_sent_str, l_sent_words = [],[],[]
			for sent in doc.sents:
				sentence = sent.text.strip()
				words = sentence.split()
				self.sents.append(sent.text.strip())
				l_sent_str.append(len(sentence))
				l_sent_words.append(len(words))

			mean_len_s = round(sum(l_sent_str)/len(l_sent_str),1)
			mean_len_words = round(sum(l_sent_words)/len(l_sent_words),1)

			return (len(self.sents),mean_len_s, mean_len_words)

		def verbs(action=''):
			verbs,verbs_dict = [],{}
			for n_tokens,token in enumerate(doc): 
				if token.pos_ == 'VERB':
					verbs.append((token.lemma_,token.text))
					if token.lemma_ not in verbs_dict:
						verbs_dict[token.lemma_] = [0]
					verbs_dict[token.lemma_].append(token.text.lower())
					verbs_dict[token.lemma_][0] += 1 
					verbs_dict[token.lemma_][1:] = list(set(verbs_dict[token.lemma_][1:]))
			d_verbs = dict(sorted(verbs_dict.items(), key = itemgetter(1), reverse = True))
			
			self.n_tokens = n_tokens
			self.all_verbs, self.d_verbs = verbs, d_verbs
			self.n_all_verbs, self.n_verbs = len(verbs),len(verbs_dict.keys())
			

			def list_verbs():
				output = ''
				for k in verbs_dict:
					verbs_dict[k].sort()
					values = "\n\t".join(verbs_dict[k])
					output += f'{k:<12} {len(values):>4} itens\n\t{values}\n'
				pydoc.pager(output)

			if action == 'list': list_verbs()

		def entities():
			d_per,d_loc = {},{}
			for ent in self.ents: 
				if   ent[1] == 'PER':
					if ent[0].replace('\n',' ') in d_per: d_per[ent[0].replace('\n',' ')] += 1
					else: d_per[ent[0].replace('\n',' ')] = 1
				elif ent[1] == 'LOC':
					if ent[0].replace('\n',' ') in d_loc: d_loc[ent[0].replace('\n',' ')] += 1
					else: d_loc[ent[0].replace('\n',' ')] = 1
			self.per= dict(sorted(d_per.items(), key = itemgetter(1), reverse = True))
			self.loc= dict(sorted(d_loc.items(), key = itemgetter(1), reverse = True))

		self.sentences = sentences()
		self.verbs = verbs(action)
		entities()
	
def locationByChapter(b: Book):
	filepath = '../Obra/' + b.filename
	with open(filepath, 'r', encoding='utf8') as book: content = book.readlines()
	query = '^ {0,70}[A-Z\u00c0-\u00dc]{1,}[^a-z\.]+$'
	chHeader_TitleCase = ['A enjeitada','A filha do Acerdiago', 
		'A filha do doutor negro', 'A mulher fatal', 'A neta do arcediago',
		'Anatema 1', 'Aventuras de Basilio Fernandes', 'Carlota Angela',
		'Cenas da Foz', 'Gracejos que matam', 'Misterios de Fafe',
		'O Judeu', 'O que fazem mulheres', 'O regicida','Um homem de brios']
	chHeader_Roman = ['A Gratidao','A Infanta Capelista', 
		'A Morgada de Romariz', 'A queda de um Anjo-Grafia actualizada', 
		'Amor de Salvacao', 'Eusebio Macario','Memorias de Guilherme do Amaral',
		'Misterios de Lisboa 1','Misterios de Lisboa 2','Misterios de Lisboa 3',
		'Novelas do Minho 1','Novelas do Minho 2','O carrasco de Vitor Hugo',
		'Coracao cabeca e estomago', 'Doze casamentos felizes',
		'Duas Horas de Leitura','Eusebio Macario', 'Novelas do Minho 1', 
		'Novelas do Minho 2','O esqueleto-v2',
		'O retrato de Ricardina-v1', 'Onde esta a felicidade', 'Um livro']
	if b.title in chHeader_TitleCase : 
		query = '^(( )*(?:Capítulo .{1,18})|( )*(?:Introdução)|( )*(?:Conclusão)$)'
	if b.title in chHeader_Roman : 
		query = '^(( )*[^ \n]((XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?)[^\f]$)'

	ch_header = [l for l,line in enumerate(content) if re.search(query,line) is not None]
	if ch_header == []: return '\n##### Capítulos não encontrados.\n\n'
	#print('\n',str(book).replace('_',' ')[40:-31],' ',len(ch_header),'\n\t',ch_header, sep='')
	ch_end = ch_header[1:]; ch_end.append(len(content))
	ch_marks = [(b,e) for b,e in zip(ch_header,ch_end)]
	#print(ch_marks)
	chapters = [content[b:e] for b,e in ch_marks]
	preface = content[0:ch_header[0]]

	non_locs_A_Brasileira_de_Prazins = ['Srª','Majestade', 'Marco']
	if b.title == 'A Brasileira de Prazins': 
		"""As it gets the book title as a chapter, strip it"""
		chapters = chapters[1:]


	all_locs = []
	for ch in chapters:
		chapter = " ".join([line.strip() for line in ch[1:]])
		doc = nlp(chapter)
		locs = [e.text for e in doc.ents if e.label_ == 'LOC']
		all_locs.append(locs)

	non_locs_Amor_de_Perdicao = ['A5','Abençoado','Abram-me',
	'Abria','Aconteceu', 'Ajuntava','Albuquerque','Alcobaça','aleive',
	'Almacave','Amanhã','Animava-a','Arranjou','Atira','bela fugitiva!',
	'Bela','Bemposta','Bendito seja Deus!','bigorna','boa moça!','Brito',
	'cabo da rua','cabo dum punhal','Chamou','Claro','Coma','Conhece-a',
	'Conta-me','Cuide','Dai-me','Decerto','Deixa','desditosa menina!',
	'Dezoito','Digo','Dionisia','Disse-mo','Donde','Eis-me','Estará','Estou',
	'esturrínho','Estás','Fala-lhe','Fale','Farei','fidalguinha','Fr',
	'Ignorava','Imaginara','Importa','insólito','Iremos',
	'Juiz de fora de','juiz de fora.','Juiz','Junqueira','lareira',
	'Leia','Mande-me','Mariana','Mariana.','Matasse','Mau','minha',
	'Nossa Senhora','Noutra','Nã','Olhe','Parece-me','Parei','Pasmosa',
	'pedra da lareira','pedra dum agueiro.','Pensará','Peça-lhe',
	'Pinhão','Pintos','planizava','Pobre','Posso amar-te','Procura-a',
	'Promete-me','Que','Queres','Queria','Rodeado','Rodeou','sanhudo',
	'Sansão','Senta-te','Serei','Significa','Simão','Sol','Tenha',
	'Tenho','Terias','terra','tonizar','Vai-te','Vais','Vales','Vamos',
	'Venha','Venho','Vinha','Ânsia','És','Ó']

	non_locs = non_locs_Amor_de_Perdicao + non_locs_A_Brasileira_de_Prazins

	sep, d_loc, d_locs, loc_data = '', {}, [], f'' 
	header = ['Capítulo', 'top 3 Localidades']
	loc_header = f'| {header[0]:<20} | {header[1]:^46} |\n'
	line =       f'|:{     sep:-<20} |:{     sep:-<46} |\n'

	for i,locs in enumerate(all_locs):
		for loc in locs: 
			if loc not in non_locs: d_loc[loc] = d_loc.get(loc, 0) + 1

		d_loc = dict(sorted(d_loc.items(), key = itemgetter(1), reverse = True))
		#d_loc = list(set(d_loc[key]))
		d_locs.append(d_loc)

		loc3 = " ; ".join(list(d_loc)[:3])
		loc_data += f'| {chapters[i][0].strip():<20} | {loc3:^46} |\n'
	
	loc_ch_output = loc_header+line+loc_data+'\n'
	if interactive: print(loc_ch_output)
	else: return loc_ch_output

def md(b: Book, level=0):
	sep = ''

	h0 = ['Autor', 'Título', 'Ficheiro']
	b_header = f'| { h0[0]:>7} | {  h0[1]:^25} | {     h0[2]:<36} |\n'
	line =  f'| {     sep:-<7}:|:{   sep:-<25}:|:{      sep:-<36} |\n'
	b_data = f'| {b.author:>7} | {b.title:^25} | {b.filename:<36} |\n'

	first_sentence  = b.sents[0].strip().replace('\n','\n>')
	second_sentence = b.sents[1].strip().replace('\n','\n>')
	b_head = '#### Primeiras duas frases detectadas pelo spaCy [ref. enunciado nº 2]'+"\n> "+"\n> ".join([first_sentence,second_sentence])

	hv = ['freq','lemma', 'ex. não ordenado de flexões']
	hv_header = f'| { hv[0]:>4} | { hv[1]:>10} | {  hv[2]:<50} |\n'
	line2 =     f'| {  sep:->4}:| {  sep:->10}:|:{   sep:-<50} |\n'
	
	hv_data = f''
	top_v = list(b.d_verbs.items())[:5]
	for lma in top_v:
		hv_data +=   f'| {  str(lma[1][0]):>4} | {  lma[0]:>10} | {   "; ".join(lma[1][1:6]):<50} |\n'
	
	t0_book_meta = '#### metadata\n\n'+b_header+line+b_data+'\n'+b_head+'\n\n'
	tv_verb_data = '#### listagem dos verbos mais frequentes [ref. enunciados nº 3 e 4]\n\n'+hv_header+line2+hv_data+'\n\n'
	
	t1_book_stat, t2_book_top, t3 = '','',''
	if level>0:
		h1 = ['nº tokens','nº verbos','nº frases','tamanho de frases','nº ents']
		stat_header = f'| {h1[0]:>10} | {h1[1]:^10} | {h1[2]:<10} | {h1[3]:<18} | {h1[4]:<10} |\n'
		line =       f'| {      sep:-<10} | {     sep:-<10} | {          sep:-<10} | {            sep:-<18} | {                sep:-<10} |\n'
		stat_data =  f'| {b.n_tokens:>10} | {b.n_verbs:^10} | {b.sentences[0]:>10} |   ~{b.sentences[2]:>6} palavras | {len(b.ents):<10} |\n'
	
		t1_book_stat = '#### Estatísticas do spaCy [ref. enunciados nº 3, 5, 6 e posto que iterando sobre todos os livros 7]\n\n'+ stat_header+line+stat_data+'\n'
	
	if level>1:
		h2 = ['top 5 Personagens', 'top 5 Localidades']
		ents_header = f'| {h2[0]:^26} | {h2[1]:^25} |\n'
		line =        f'|:{ sep:-<26} |:{ sep:-<25} |\n'
		
		pl = zip(list(b.per.items())[:5],
				 list(b.loc.items())[:5])

		ents_data = f'' 
		for i in list(pl): 
			ents_data += f'| {i[0][0]:<21}{i[0][1]:>5} | {i[1][0]:20}{i[1][1]:>5} |\n'
		
		t2_book_top = '#### [ref. enunciado nº 9, necessitando internamente nº 8, e fornecendo 10 já que iterando sobre todos os livros]\n\n' + ents_header+line+ents_data+'\n'
	
	if level>2: t3 = locationByChapter(b) + '\n\n'
	
	return t0_book_meta+t1_book_stat+tv_verb_data+t2_book_top+'#### Lugares mais falados por capítulo, quando possível, [ref enunciado nº 11]\n\n'+t3




"""1. Lista das obras de camilo.
Listar as obras de Camilo existentes na pasta `Obra/` do nosso repositório.
Ou seja apresentar a lista dos ficheiros de texto existentes nessa pasta."""

try: 
	with open('../Obra', 'r') as folder: folder.read()
except IsADirectoryError: 
	obras = os.listdir('../Obra'); obras.sort(); 
	pass
except: print('ERRO: diretório "Obra" não achado')
finally: 
	if interactive:
		print('TP1.1:\n\t',end='')#,"\n\t".join(obras),sep='')
		inp = input('pressione qualquer tecla para continuar, '
		+'na listagem aperte q para sair')
		pydoc.pager("\n".join(obras))
	
	else: 
		markdown += '''
#### Código

```python
obras = os.listdir('../Obra'); obras.sort();
```

### Listagem de obras
<details id="list_books">
	<summary>expanda lista</summary>
	
1. ''' + '\n1. '.join(obras) + '\n</details>\n\n'


"""2. Tílulo e autor de um livro
Dado um livro (ficheiro de texto, ex: `Amor_de_predição.txt`) 
mostrar as duas primeiras frases.
"""

if interactive:
	books = [book[7:-4].replace('_',' ') for book in obras]
	inp = input('TP1.2\n\tpressione qualquer tecla para continuar,'+
				' depois escolha uma obra')
	title = 'Selecione um título de livro de Camilo Castelo Branco'
	options = books
	option, i = pick(options, title)
	book_path = '../Obra/' + obras[i]
	book = Book(book_path)
	book.stats()
	print('# TP1\n\n## primeira iteração: \n')
	print(md(book,2))

	if book.title == 'Amor de Perdicao':
		print('Vê-se erros do Spacy:',
		'\t* em citar mais de uma vez o mesmo Simão (Botelho);',
		'\t* em pensar que Mariana seria uma localidade.',
		'Para além, vê se que "\\n" se intermeiam nas entidades',
		'> Assim como outros sinais de pontuação como, hyphen'
		'\nAlterando essas entidades, temos a 2ª iteração:\n', sep='\n')

		book.per['Mariana'] = book.loc['Mariana']
		del book.loc['Mariana']
		del book.loc['Estou']
		del book.loc['Albuquerque']
		del book.loc['Olhe']
		del book.loc['Vamos']
		del book.loc['Que']

		personagens = [('Baltasar Coutinho',"Balta"),('Simão Botelho',"Simão"),
					('Tadeu de Albuquerque', "Tadeu"), ('Teresa de Albuquerque',"Tere")]
		for k in book.per.keys():
			for p,query in personagens:
				if k != p:
					if k.find(query) > -1:
						book.per[p] += book.per[k]
						book.per[k] = 0

		book.per= dict(sorted(book.per.items(), key = itemgetter(1), reverse = True))
		book.loc= dict(sorted(book.loc.items(), key = itemgetter(1), reverse = True))
		print(md(book,2))
		book.verbs('list')

else:
	markdown += '''

## 2. Estatísticas sobre as obras de Camilo

Instancio uma classe de _Books_ aonde, usando o **spaCy**, carrego estatísticas (método _stats_) sobre cada obra:
  * As entidades _ents_ separados em:
    - personagens
    - localidades
  * As frases e seu tamanho médio em carácteres e em palavras
  * Os verbos e seus lemmas, compilados em dicionário de frequencias

Então imprimo tabelas e as 2 frases iniciais com tais informações (função _md_)

#### Código

```python
for obra in obras:
	book_path = '../Obra/' + obra
	book = Book(book_path)
	book.stats()
	markdown += md(book)
```

### Listagem de obras

	
'''
	for obra in obras:
		book_path = '../Obra/' + obra 
		book = Book(book_path)
		markdown += str('### ' + book.title 
				 + '\n<details id="'+ obra +'">'
				  +'\n\t<summary>expanda para detalhes</summary>\n\n')
		book.stats()
		markdown += md(book,3) + '</details>\n\n'
	


markdown += '''\n\n
## Considerações finais

Dada a diferença na padronização da formatação das obras na pasta `./Obra`,
seria interessante o pré-processamento destes para melhorar análises textuais.


Cabe salientar que me detive na qualidade da saída de Amor de Perdição, 
posto que teria algumas sugestões de alteração no texto as quais estão em
`./proposta.sh`. _Outputs_ como a **A Brasileira de Prazin** e **A enjeitada** 
parecem bem formadas, mas outras como _A senhora Rattazzi_ ou _Anatema 1_ falham 
seja por detectarem **ents** que não se encaixam nos conceitos, seja porque os
capítulos são errôneamente atribuídos.

Reforço então a sugestão de padronização de estilo para que análises automáticas
resultem mais refinadas.

## Anexos:

#### listagem não exaustiva dos títulos que não estão em caixa-alta

```python
	chHeader_TitleCase = ['A enjeitada','A filha do Acerdiago', 
		'A filha do doutor negro', 'A mulher fatal', 'A neta do arcediago',
		'Anatema 1', 'Aventuras de Basilio Fernandes', 'Carlota Angela',
		'Cenas da Foz', 'Gracejos que matam', 'Misterios de Fafe',
		'O Judeu', 'O que fazem mulheres', 'O regicida','Um homem de brios']
	chHeader_Roman = ['A Gratidao','A Infanta Capelista', 
		'A Morgada de Romariz', 'A queda de um Anjo-Grafia actualizada', 
		'Amor de Salvacao', 'Eusebio Macario','Memorias de Guilherme do Amaral',
		'Misterios de Lisboa 1','Misterios de Lisboa 2','Misterios de Lisboa 3',
		'Novelas do Minho 1','Novelas do Minho 2','O carrasco de Vitor Hugo',
		'Coracao cabeca e estomago', 'Doze casamentos felizes',
		'Duas Horas de Leitura','Eusebio Macario', 'Novelas do Minho 1', 
		'Novelas do Minho 2','O esqueleto-v2',
		'O retrato de Ricardina-v1', 'Onde esta a felicidade', 'Um livro']
```

#### listagem não exaustiva de falsas localidades levantadas pelo **spaCy**

Mariana, provavelmente pelo tomada como localidade pelo acidente ambiental 
constava em __Amor de Perdição__ como a localidade mais falada, sendo na verdade
uma personagem.

```python
non_locs_A_Brasileira_de_Prazins = ['Srª','Majestade', 'Marco']
non_locs_Amor_de_Perdicao = ['A5','Abençoado','Abram-me',
	'Abria','Aconteceu', 'Ajuntava','Albuquerque','Alcobaça','aleive',
	'Almacave','Amanhã','Animava-a','Arranjou','Atira','bela fugitiva!',
	'Bela','Bemposta','Bendito seja Deus!','bigorna','boa moça!','Brito',
	'cabo da rua','cabo dum punhal','Chamou','Claro','Coma','Conhece-a',
	'Conta-me','Cuide','Dai-me','Decerto','Deixa','desditosa menina!',
	'Dezoito','Digo','Dionisia','Disse-mo','Donde','Eis-me','Estará','Estou',
	'esturrínho','Estás','Fala-lhe','Fale','Farei','fidalguinha','Fr',
	'Ignorava','Imaginara','Importa','insólito','Iremos',
	'Juiz de fora de','juiz de fora.','Juiz','Junqueira','lareira',
	'Leia','Mande-me','Mariana','Mariana.','Matasse','Mau','minha',
	'Nossa Senhora','Noutra','Nã','Olhe','Parece-me','Parei','Pasmosa',
	'pedra da lareira','pedra dum agueiro.','Pensará','Peça-lhe',
	'Pinhão','Pintos','planizava','Pobre','Posso amar-te','Procura-a',
	'Promete-me','Que','Queres','Queria','Rodeado','Rodeou','sanhudo',
	'Sansão','Senta-te','Serei','Significa','Simão','Sol','Tenha',
	'Tenho','Terias','terra','tonizar','Vai-te','Vais','Vales','Vamos',
	'Venha','Venho','Vinha','Ânsia','És','Ó']
```

'''

print(markdown)
