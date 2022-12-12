import re, sys, doctest

def tagReplacer(text, tag='', repl='', self_closing=False):

	"""
	Given a text, replace/strip tag
	_defaults to stripping all tags

	:param text: str
	:param tag:  str
	:param repl: str
	:param self_closing: boolean
	:return: str

	>>> tagReplacer('O gato <b>preto</b> cruzou a estrada<br />')
	'O gato preto cruzou a estrada'
	>>> tagReplacer('O gato <b>preto</b> cruzou a estrada<br />','b')
	'O gato preto cruzou a estrada<br />'
	>>> tagReplacer('O gato <b>preto</b> cruzou a estrada<br />','b','emph')
	'O gato <emph>preto</emph> cruzou a estrada<br />'
	>>> tagReplacer("O gato <b>preto</b> cruzou a estrada<br />","b","emph rend='bold'")
	"O gato <emph rend='bold'>preto</emph> cruzou a estrada<br />"
	>>> tagReplacer('O gato <b>preto</b> cruzou a estrada<br />','br',self_closing=True)
	'O gato <b>preto</b> cruzou a estrada'
	>>> tagReplacer('O gato <b>preto</b> cruzou a estrada<br />','br','lb', True)
	'O gato <b>preto</b> cruzou a estrada<lb />'
	>>> tagReplacer('O gato <b>preto</b> cruzou a estrada<br />','br','lb class="dummy"', True)
	'O gato <b>preto</b> cruzou a estrada<lb class="dummy" />'

	>>> tagReplacer('<span class="fr">Le chat est monté sur le toit.</span>','span class="fr"')
	'Le chat est monté sur le toit.'
	"""

	t_closer = (r'</'+re.sub(r'(^\w+)(?:.*)', r'\1', tag )+'>' 				if tag  != '' else '')  if not self_closing else ''
	pattern  = ('<'+tag+r'(?:(?: ?>)|(?: +[^\w]+[^/>]*?>))(.*?)'+t_closer)  if not self_closing else r'<'+tag+r' ?[^\\]*?>'
	r_opener = (r'<'+repl+r'>'  if not self_closing else r'<'+repl+r' />') 	if repl != '' else ''
	r_closer = (r'</'+re.sub(r'(^\w+)(?:.*)', r'\1', repl)+'>' 				if not self_closing else '') if repl != '' else ''
	replace  = (r_opener+r'\1'+r_closer            							if not self_closing else r'<'+repl+r' />') if repl != '' else ''

	# print(f'tag={tag}\n{t_closer}')
	# print(f'repl={repl}\n{r_opener}\n{r_closer}')
	# print(f'pattern={pattern}\nreplace={replace}')

	if tag == '':
		strip_all_tags = re.sub(r'<[^>]*?>', r'', text)
		output = strip_all_tags
	elif repl == '':
		strip_select_tag = re.sub(pattern, r'\1', text) if not self_closing else re.sub(pattern, '', text)
		output = strip_select_tag
	else:
		replace_select_tag = re.sub(pattern, replace, text)
		output = replace_select_tag

	return output

doctest.testmod()

if __name__ == '__main__':

	"""
	if run not as a module, either get argvs
	_or stdin to output something

	"""

	if sys.stdin.isatty():
		n_args = len(sys.argv[1:])
		if n_args   <  1: print("nothing in stdin nor arguments given")
		elif n_args == 1: print(tagReplacer(sys.argv[1]))
		elif n_args == 2: print(tagReplacer(sys.argv[1],sys.argv[2]))
		elif n_args == 3: print(tagReplacer(sys.argv[1],sys.argv[2],sys.argv[3]))
		else			: print("too many arguments")
	else: print(tagReplacer(sys.stdin.read()))
