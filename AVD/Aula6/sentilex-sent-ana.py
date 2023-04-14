#!/usr/bin/python3
import re
POL = {}

def carrega_sentilex():
    with open("sentilexjj.txt") as f:
        for linha in f:
            linha = re.sub(r"ANOT=.*", "", linha)
            lista = re.split(r";",linha)
            if len(lista) == 5:
                pallemapos, flex, assina, pol, lixo = lista
                pal = re.split(r",",pallemapos)[0]
                pol = int( re.sub(r"POL:N[01]=", "", pol) )
                POL[pal] = pol
            elif len(lista) == 6:
                pallemapos, flex, assina, pol1, pol2, lixo = lista
                pal = re.split(r",",pallemapos)[0]
                pol1 = int( re.sub(r"POL:N[01]=", "", pol1) )
                pol2 = int( re.sub(r"POL:N[01]=", "", pol2) )
                POL[pal] = (pol1+pol2)/2 
            else:
                print(lista)
                exit()

def sentimento(frase):
    lp = re.findall(r"\w+", frase)    #  era...lp = frase.split()
    ptotal = 0
    
    for p in lp:
        if p in POL:
            ptotal += POL[p] 

    return (ptotal, len(lp)) 

carrega_sentilex()

txt = open("harry_potter_pedra_filosofal.txt").read()
listacap = re.split(r"#", txt)
for cap in listacap:
    print( len(cap), sentimento(cap))
