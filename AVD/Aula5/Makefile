N=40

p0:
## limpeza geral AP; uma frase por linha
	onesentpl -l Camilo-Amor_de_Perdicao.txt > AP.txt

p1:
## tagging + entidades
	linguakit tagger pt -nec AP.txt > AP.tag

p2:
## Calcular entidades; selecionar as 20 mais oco
	python getNP-oco.py -n $N AP.tag > AP20.csv
