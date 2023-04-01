#!/usr/bin/python3
'''
NAME
   onesentpl - convert text into one-sentence-per-line format

Usage:
   onesentpl -l file.txt > nova.txt

Options:
   -l   convert utf8 '—' in ascii '-' (for linguakit)
'''
__version__ = "0.0.2"

from jjcli import * 

def main():
    cl=clfilter(opt="l", doc=__doc__) 
    abrev = r'((Sr|Sra|Exm[oa]?|Ilm[oa]|Dr|Dra|Fr)\.)\n'
    
    for par in cl.paragraph():      ## process paragrafo de cada vez
        if match(r'---\s*\n',par):  ## não processa as linhas "---" metadados
            print(par, "\n")
            continue
        par = re.sub(r'(#.*)', r'\1§', par)                 ## titulos markdown
        par = re.sub(r'(\w)-\n *([a-zç-])',  r'\1\2', par); ## translineações
        par = re.sub(r'\n', r' ', par)
        par = re.sub(r'([a-zãáéíúó0-9][.?!]+) ([A-ZÁÉÍÓÚ\-])', r'\1\n\2', par)
        par = re.sub(r'([a-zãáéíúó0-9][.?!]+) (— *[A-ZÁÉÍÓÚ])', r'\1\n\2', par)
        par = re.sub(r' +', r' ', par) 
        par = re.sub(abrev, r'\1 ', par,flags=re.I)         ## abreviaturas
        par = re.sub(r'(#.*)§', r'\n\1\n', par)
        if "-l" in cl.opt:
            par = re.sub(r'—', r'-', par)
    
        print (par, "\n")

if __name__ == "__main__":
    main()
