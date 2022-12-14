import sys, io
from lxml import etree;

parser = etree.XMLParser(remove_blank_text=True)

def ppXML(xml: str):
    parsed = etree.XML(xml,parser)
    pretty = etree.tostring(parsed,pretty_print = True, encoding="UTF-8")
    
    return pretty.decode("utf-8")

if __name__ == '__main__':
	if sys.stdin.isatty():
		if len(sys.argv[1:]) == 1 :
			try:
				xml = open(sys.argv[1]).read()
				print(ppXML(xml))
			except FileNotFoundError: 
				xml = sys.argv[1]
				print(ppXML(xml))
		else: raise Exception("Too few/much arguments")
        
	else: print(ppXML(sys.stdin.read()))

