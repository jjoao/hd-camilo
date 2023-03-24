from jjcli import *

html_1 = ""
html_2 = open("obras.html", "w")

obras = glob("Obra/*.txt")

for obra in obras:
    print(obra)
    html_1 = html_1 + "<p>" + obra + "</p>\n"

html_2.write(html_1)