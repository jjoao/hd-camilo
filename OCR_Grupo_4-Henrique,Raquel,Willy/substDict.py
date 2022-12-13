import json, re
import doctest

# loading data on where to find book
try:
	with  open("./sources/dictSubst.json", 'r') as f:
		dictSubst = json.load(f)
except FileNotFoundError:  
	dictSubst = {
#Normalizing white spaces to a single
 ' {1,}'                 	 : ' ',
#Annotating abbreviations, starting from the ones w/ superscript
 'ª'				 : '<sup>a</sup>',
r'\.\^([a-z]{1,3})'		 :r'.<sup>\1</sup>',
 '([V|v]\. [E|e]x\.<sup>a</sup>)': '<abbr expan="Vossa Excelência">V. Ex.<sup>a</sup></abbr>',
 '([V|v]\. [S|s]\.<sup>a</sup>)' : '<abbr expan="Vossa Senhoria">V. S.<sup>a</sup></abbr>',
 '(vm.<sup>ce</sup>)'		 : '<orig reg="você"><abbr expan="vossa mercê">vm.<sup>ce</sup></abbr></orig>',
 'Ill.<sup>mo</sup>'		 : '<abbr expan="Ilustríssimo">Ill.<sup>mo</sup></abbr>',
 '(D.<sup>or</sup>)'		 : '<abbr expan="Doutor">D.<sup>or</sup></abbr>',
 '(Snr.)'			 : '<abbr expan="Senhor">Snr.</abbr>',
#HTML tags into XML tags
 '<b>'				 : '<emph rend="bold">',
 '<i>'				 : '<emph rend="italic">',
 '<u>'				 : '<emph rend="underscore">',
 '</b>|</i>|</u>'		 : '</emph>',
 '<br />'			 : '<lb />',
}
	pass
except: print('ERRO: dicionário "dictSubst" não existe, nem pôde ser criado')


def substDict(text,dictSubst):

	"""
	Given a text, do regex substitutions
   	_based on a dictionary

	:param text: str
	:param dictSubst:  dict
	:return: str

	>>> substDict("O gato <b>preto</b> cruzou   a   estrada<br />",dictSubst)
	'O gato <emph rend="bold">preto</emph> cruzou a estrada<lb />'
	>>> substDict("Que o Ill.^mo tem romances na sua bibliotheca",dictSubst)
	'Que o <abbr expan="Ilustríssimo">Ill.<sup>mo</sup></abbr> tem romances na sua bibliotheca'
	>>> substDict("— E vm.^ce não acceitou a incumbencia",dictSubst)
	'— E <orig reg="você"><abbr expan="vossa mercê">vm.<sup>ce</sup></abbr></orig> não acceitou a incumbencia'
	>>> substDict("Ill.^mo Snr. D.<sup>or</sup> Domingos",dictSubst)
	'<abbr expan="Ilustríssimo">Ill.<sup>mo</sup></abbr> <abbr expan="Senhor">Snr.</abbr> <abbr expan="Doutor">D.<sup>or</sup></abbr> Domingos'
	"""

	for key, value in dictSubst.items():
		text = re.sub(key,value, text)
	return text

doctest.testmod()

if __name__ == '__main__':

	"""
	if run not as a module, either get argvs
	_or stdin to output something

	"""
	if sys.stdin.isatty():
		n_args = len(sys.argv[1:])
		if n_args   <  1: raise Exception("nothing in stdin nor arguments given")
		try:
			txt =  open(sys.argv[1]).read()
		except FileNotFoundError: 
			txt =  sys.argv[1]
		if   n_args == 1: print(substDict(txt))
		elif n_args == 2: 
			try:
				dct = open(sys.argv[2]).read()
			except FileNotFoundError: 
				dct = sys.argv[2]
			print(substDict(txt,dct))
		else : print("too many arguments")
	else: print(substDict(sys.stdin.read()))
