import re, sys
# python3 mgrep in.txt "\n<p>\n(^.*$)\n</p>" "\n<h2>\1</h2>'" out.txt
# needs scapping: | \

def multiLine_grep(f_i, r_i, r_o):
	"""
	Given a text, replace patter for replace in multiple lines
	_saves to file if given enough argumennts

	utf-8 capabilities, multi-line by default

	echo "<täg>item</tag>" | python3 mgrep.py '<\w+' '<tag'
	echo "<täg>item</tag>" | python3 mgrep.py '</?\w+>'


	"""

	return re.sub(r_i, r_o, f_i, flags=re.M)

if __name__ == '__main__':
	arg_len = len(sys.argv[1:])
	print(arg_len)
	if sys.stdin.isatty():
		""""when nothing in stdin consider arg as the followinng
            [input.file , pattern, replacement, output.file]"""

		if 1 < arg_len <= 4:

			try: f_i = open(sys.argv[1], "r").read()
			except FileNotFoundError: 
				raise Exception("input.file couldn't be opened")

			r_i = r'{}'.format(sys.argv[2])
			r_o = '' if arg_len == 2 else r'{}'.format(sys.argv[3])

			if arg_len == 4:
				with open(sys.argv[4], 'w') as f_o:
					f_o.write(multiLine_grep(f_i, r_i, r_o))
			else:       print(multiLine_grep(f_i, r_i, r_o))
		else: raise Exception(
			"try: python3 mgrep input.file pattern replacement output.file ")
	else: 
		""""when data in stdin consider arg as the followinng
			[pattern, replacement, output.file]"""
		f_i = sys.stdin.read()
		arg_len = len(sys.argv[1:])
		if 0 < arg_len <= 3:
			r_i = r'{}'.format(sys.argv[1])
			r_o = '' if arg_len == 1 else r'{}'.format(sys.argv[2])
			if arg_len == 3:
				with open(sys.argv[3], 'w') as f_o:
					f_o.write(multiLine_grep(f_i, r_i, r_o))
			else:       print(multiLine_grep(f_i, r_i, r_o))
		else: raise Exception("try: echo 'some text' | python3 mgrep pattern replacement output.file ")
