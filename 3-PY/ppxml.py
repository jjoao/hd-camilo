import sys, io
from lxml import etree;

parser = etree.XMLParser(remove_blank_text=True)

def ppXML(xml: str):

    parsed = etree.XML(xml,parser)
    pretty = etree.tostring(parsed,pretty_print = True)
    
    return pretty.decode("utf-8")

def ppXML_argv(xml: str):

    parsed = etree.XML(xml,parser)
    pretty = etree.tostring(parsed,pretty_print = True)
    
    return pretty.decode("utf-8")

if __name__ == '__main__':
	if sys.stdin.isatty():
		if len(sys.argv[1:]) == 1 :
			try:
				xml = open(sys.argv[1]).read()
				print(ppXML(xml))
			except: print("throw error opening file")
		else: print("throw error due to too few/much arguments")
        
	else: print(ppXML(sys.stdin.read()))
	#else: print(etree.tostring(etree.parse(io.StringIO(sys.stdin.read()),etree.XMLParser(remove_blank_text = True)), pretty_print = True).decode("utf-8"))