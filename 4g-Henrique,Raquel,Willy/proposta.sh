#!/bin/bash

# Regex replacements needed

## strip pagenumbers but retain <0x0c> form feed \f
python3 mgrep.py \
../Obra/Camilo-Amor_de_Perdicao.txt \
'(?:\n{1,})(?: {11,})(?:[0-9]{1,3})\n(\x0c)(?: {11,})?(?:www.nead.unama.br)?(?:\n{2,})?' \
'\1\n' \
../Obra/Camilo-Amor_de_Perdicao.txt


## change hyphen, ndash, mdash to m-dash like \u2015 for dialogue citation

python3 mgrep.py \
../Obra/Camilo-Amor_de_Perdicao.txt \
'^ {6,12}(?:[‒–—―] )' \
'        ― ' \
../Obra/Camilo-Amor_de_Perdicao.txt

## normalize paragraph beginning to 10 spaces
python3 mgrep.py \
../Obra/Camilo-Amor_de_Perdicao.txt \
'^ {6,12}(["a-zA-Z\u00c0-\u00dc])' \
'        \1' \
../Obra/Camilo-Amor_de_Perdicao.txt

python3 substDict.py \
 ../Obra/Camilo-Amor_de_Perdicao.txt \
./src/Amor_de_Perdicao.dict.json \
> ../Obra/Camilo-Amor_de_Perdicao.tmp.txt

mv ../Obra/Camilo-Amor_de_Perdicao.tmp.txt ../Obra/Camilo-Amor_de_Perdicao.txt
