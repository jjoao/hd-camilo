#!/usr/bin/env python3

from jjcli import *

cl = clfilter("")

for linha in cl.input():
    if "NP" in linha:
        print(linha)

