#!/usr/bin/env python3

from jjcli import *
from collections import Counter

cl = clfilter("")
oco = Counter()

for linha in cl.input():
    if "NP" in linha:
        word, lema, pos = linha.split()
        oco[word] = oco[word]+1
        ### oco[word] += 1

for  w,n  in  oco.most_common(30):
    print( f"{w},{n}")

#print(oco.most_common(30),"\n")
