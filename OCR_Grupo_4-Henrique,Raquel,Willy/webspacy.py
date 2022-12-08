# -*- coding: utf-8 -*-
import os, sys, itertools, re
import requests, html, json
from bs4 import BeautifulSoup as bs
from lxml import etree
import xml.etree.cElementTree as ET
from json2xml import json2xml
from json2xml.utils import readfromjson #, readfromurl, readfromstring
from xml.dom import minidom
import spacy
from spacy import displacy, tokenizer
from spacy.language import Language

try:
	nlp = spacy.load("pt_core_news_lg")
except:
	print("install spacy's 'pt_core_news_lg' portuguese package"
		  "\npython -m spacy download pt_core_news_lg")

try:
	with open('./sources', 'r', encoding='utf8') as folder:
			folder.read()
except FileNotFoundError: os.mkdir('sources')
except IsADirectoryError: pass
except: print('ERRO: diretório "sources" não existe, nem pôde ser criado')

lineUp = '\033[1A'
lineClear = '\x1b[2K'
spinner = itertools.cycle(['|', '/', '-', '\\'])

def cmdNiceties():
	print(lineClear, end ='\r')
	sys.stdout.write(next(spinner))   # write the next character
	sys.stdout.flush()                # flush stdout buffer (actual character display)
	sys.stdout.write('\b')		       # erase the last written char

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

"""Functions for text handling"""

dictSubst = {

#Normalizing white spaces, later <head> will have '\n\n'
' {1,}'                 : ' ',
'\n.{1,}' 			: '\n', # dealt in body of functioon
r'\
</p>'				: '</p>',

#Normalize some superscript
'ª'						: '<sup>a</sup>',

#HTML tags
'<i>'					: '<emph rend="italic">',
'</i>|</u>'				: '</emph>',
'<u>'					: '<emph rend="underscore">',
'<br />'				: '<lb />',
'<head>'				: r'\n\n<head>',
'</head>'				: r'</head>\n'
}

def substDict(text):
	regex = re.compile("|".join(map(repr, dictSubst.keys())))
	return regex.sub(lambda match: dictSubst[match.group(0)], text)

def decodeHandler(text):
	return html.unescape(
			etree.tostring(text, pretty_print=True).decode("utf-8"))

def refsHandler(text):
	t0	= textHandler(text)
	t1	= re.sub(r'\n',r'',t0)
	t2	= re.sub(r'<ol [^>]*>(.*?)<\/ol>', 
				 r'<note><list type="ordered">\1</list></note>\n\n\n', t1)
	t3	= re.sub(r'<li [^>]*>(.*?)<\/li>', r'<item>\1</item>', t2)
	return t3

def titleHandler(text):
	return str("<head>" + text + "</head>\n")

def textHandler(text):
	t0	= decodeHandler(text)
	t1	= span_pagenumToPb(t0)
	t2	= quotationToquote(t1)
	t3	= iToEmph(t2)
	t4	= stripSpan(t3)
	t5	= newLine(t4)
	t6	= substDict(t5)
	t7	= ref(t6)
	t99 = stripA(t7)
	return t99

def newLine(text):
	add = re.sub(r'(?!\<\/p>)(.+)\n', r'\1<lb />\n', text)
	trimBack = re.sub(r'(</?\w+[^>]*> *)<lb />\n', r'\1\n', add)
	normalize = re.sub(r'<lb />\n?</p>?', r'</p>', trimBack)
	normalize = re.sub(r'(<pb [^>]*>)\n{0,2}</p>', r'</p>\1', normalize)
	return normalize

'''USE this'''
# def normNewLine(text):
# 	return re.sub(r'\n{1,}', r'\n', text)

def stripSpan(text):
	t0	= re.sub(r'<span[^>]*>(.*?)<\/span>', r'\1', text)
	t99	= re.sub(r'<span[^>]*>|<\/span>', r'', t0)
	return t99

def stripA(text):
	t0	= re.sub(r'<a [^>]*>(.*?)<\/a>', r'\1', text)
	t1	= re.sub(r'<a [^>]*>|<\/a>', r'', t0)
	return t1

def span_pagenumToPb(text):
	return re.sub(
r'(?i)<span><span class="pagenum ws-pagenum" id="([0-9]{1,3}|(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?)".*\/><\/span>', 
r'<pb n="\1" />', text)

def quotationToquote(text):
	return re.sub(r'«(.*?)»', r'<quote>\1</quote>', text)

def iToEmph(text):
	t0	= re.sub(r'<i[^>]*>(.*?)</i>', r'<emph rend="italic">\1</emph>', text)
	t1	= re.sub(r'<i>', r'<emph rend="italic">', t0)
	t99	= re.sub(r'</i>', r'</emph>', t1)
	return t99

def ref(text):
	t0 = re.sub(r'<sup class="reference" [^>]*><a [^>]*>\[(\d+)\]</a></sup>', 
				r'<ref><sup>\1</sup></ref>', text)
	return t0

#root & stem of a XML into which data will be plugged-in
root = ET.Element("TEI.2"); 
if True:
	tH	= ET.SubElement(root,"teiHeader")
	txt	= ET.SubElement(root,"text")
	frt	= 	ET.SubElement(txt,"front")
	d1f	= 		[ET.SubElement(frt,"div1") for i in range(1)]
	bod	= 	ET.SubElement(txt,"body")
	d1b	= 		[ET.SubElement(bod,"div1") for i in range(2)]
	
	stemTree = ET.ElementTree(root)
	stemTree.write("./sources/stemTree.xml")

#mockup of book as dictionary/json structure
book = {
	"meta": {},
	"front": [],
	"chapters": [],
	"back": []
}

# loading data on where to find book
try:
	with  open("./sources/AmorDePerdição.json", 'r') as f:
		d = json.load(f)
except FileNotFoundError:  
	print('Warning: specification file for book retrieval',
		'not found, using default')
	d = {"URL": "https://pt.wikisource.org/wiki/Amor_de_Perdição", 
		 "pages" : ["Dedicatória", "Prefacio",
				"I", "II", "III", "IV", "V", "VI", "VII", "VIII", 
				"IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", 
				"XVII", "XVIII", "XIX", "XX"],
		"XPath": "//*[@id=\'mw-content-text\']"}
	pass
except: print('ERRO: diretório "sources" não existe, nem pôde ser criado')

# http fetch file by feeding url and feeding nested lists
htmlSections = []; xmlSections = []; html_text = ""; pg = 0
for page in d['pages']:
	cmdNiceties()
	# print(lineClear, end ='\r')
	# sys.stdout.write(next(spinner))   # write the next character
	# sys.stdout.flush()                # flush stdout buffer (actual character display)
	# sys.stdout.write('\b')		       # erase the last written char
	print("\tparsing:", page)
	print(lineUp,end=lineClear)

	q = str( d['URL'] + "/" + page)
	r = requests.get(q)
	if r.status_code == 200:
		soup 	= bs(r.content, 'lxml')
		dom 	= etree.HTML(str(soup))
		content = dom.xpath('//*[@id="mw-content-text"]/div[1]')[0]
		refs 	= content.xpath('//*[@class="references"]')
		title 	= content.xpath(
							'./div//span[@class="mw-headline"]/text()')
		if len(title) > 1: title = title[0] 
		text 	= content.xpath('./div/p')

		"""HTML list [h2, p, ol] -> [<head>, <p>, <note>]"""
		htmlSections.append([
					"".join([titleHandler(t) for t in title]),
					"".join([textHandler(p ) for p in text]),
					"".join([refsHandler(r ) for r in refs])])
		
		"""XML list <div2>[<head>, <p>, <note>]"""
		ch = pg-1; 
		div2child = "".join([htmlSections[-1][0],htmlSections[-1][1],
							 htmlSections[-1][2]])
		if   pg == 0: 
			xmlSections.append(ET.XML("".join([
								"<div2 type='Dedicatória'>", 
									htmlSections[-1][0],
									htmlSections[-1][1],
									htmlSections[-1][2], 
								"</div2>"
								])))
			d1f[0].set("type", "Prefácio")
			d1f[0].append(xmlSections[-1])
		elif pg == 1:
			xmlSections.append(
				ET.XML("<div2 type='Prefácio'>"+div2child+"</div2>"))
			d1f[0].append(xmlSections[-1])
		elif pg < 11: 
			xmlSections.append(
				ET.XML("<div2 chapter='"+str(ch)+"'>"+div2child+"</div2>"))
			d1b[0].set("type", "Parte 1")
			d1b[0].append(xmlSections[-1])
		else: 
			xmlSections.append(
				ET.XML("<div2 chapter='"+str(ch)+"'>"+div2child+"</div2>"))
			d1b[1].set("type", "Parte 2")
			d1b[1].append(xmlSections[-1])

		"""Dict variable for JSON export"""
		if 		pg == 0: 
			book["front"].append({"div2 chapter='Dedicatória'" :div2child})
		elif 	pg == 1: 
			book["front"].append({"div2 chapter='Prefácio'" 	:div2child})
		else:		 
			book[ "chapters"].append({"div2 chapter='"+str(ch)+"'":div2child})
		
		html_text += htmlSections[-1][0]+htmlSections[-1][1]+htmlSections[-1][2]

		pg+=1

#HTML output
with open("./sources/CASTELO-BRANCO,Camilo-AmorDePerdição.html",'w') as htmlF:
	output = ""
	for section in htmlSections: output+="\n".join(section)
	htmlF.write(output)

#XML output
tree = ET.ElementTree(root)
tree.write("tTree.xml", encoding="utf-8", xml_declaration=True)
with open("tTree.xml", "r") as read:
	xml = read.read()
	with open("tTree.xml", "w") as file:
		file.write(minidom.parseString(xml).toprettyxml(indent="	"))

#JSON output & convert to XML
with open('./sources/CASTELO-BRANCO,Camilo-AmorDePerdição.json','w') as jsonf:
	jsonf.write(json.dumps(book, ensure_ascii=False)) 
	with open('./sources/json2xm.xml', 'w') as xmlf:
		data = readfromjson(
					'./sources/CASTELO-BRANCO,Camilo-AmorDePerdição.json')
		xmlf.write(html.unescape(json2xml.Json2xml(data).to_xml()))

untagged = re.sub(r'<[^>]*?>', r'', html_text)
with open('./sources/CASTELO-BRANCO,Camilo-AmorDePerdição.txt', 'w') as txt:
	txt.write(untagged) 

text = html_text # untagged

doc = nlp(text)

sentences = list(doc.sents)
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]

def spacyTagTxt(paragraphs,ents):
	
	tagChars = 0
	for w, beg, end, typ in ents:
		beg += tagChars
		end += tagChars
		typ = "name" # persName, placeName later on mapped to PER, LOC
		tagged = "<"+typ+">"+w+"</"+typ+">"
		paragraphs = paragraphs[0:beg]+tagged+paragraphs[end:]
		tagChars+=len(tagged)-len(w)
	return paragraphs


output = spacyTagTxt(html_text,ents)
with open('./sources/CASTELO-BRANCO,Camilo-AmorDePerdição.xml', 'w') as out:
	out.write(output) 
