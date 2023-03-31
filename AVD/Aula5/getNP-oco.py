#!/usr/bin/env python3

from jjcli import *
from collections import Counter

cl = clfilter("n:")
oco = Counter()
q = int(cl.opt["-n"]) if "-n" in cl.opt else 20

for linha in cl.input():
    if "NP" in linha:
        word, lema, pos = linha.split()
        oco[word] = oco[word]+1
        ### oco[word] += 1

for  w,n  in  oco.most_common(q):
    print( f"{w},{n}")

#print(oco.most_common(30),"\n")
