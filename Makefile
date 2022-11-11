

SHELL=/bin/bash

G=~/googledrive/Camilo/

up:
	rsync  -turv  $G/recortes/ ./recortes/
	rsync  -turv  $G/Obra/ ./Obra/

