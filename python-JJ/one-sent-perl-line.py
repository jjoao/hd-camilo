#!/usr/bin/python3
'''
NAME
   one-sent-per-line -  

Usage:
  one-sent-per-line  file.txt > nova.txt

Description '''

from jjcli import * 
cl=clfilter(opt="do:", doc=__doc__) 

for par in cl.paragraph():    ## process one line at the time
    if match(r'---\s*\n',par):
        print(par, "\n")
        continue
    par = re.sub(r'(#.*)', r'\1§', par)
    par = re.sub(r'(\w)-\n *([a-zç])',  r'\1\2', par);  ## translineações
    par = re.sub(r'\n', r' ', par)
    par = re.sub(r'([a-zãáéíúó0-9][.?!]+) ([A-ZÁÉÍÓÚ\-—])', r'\1\n\2', par)
    par = re.sub(r' +', r' ', par) 
    par = re.sub(r'((Sr|Sra|Exm[oa]?|Ilm[oa])\.)\n', r'\1 ', par) ## abreviaturas
    par = re.sub(r'(#.*)§', r'\n\1\n', par)

    print (par, "\n")

