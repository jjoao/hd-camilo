#!/usr/bin/python3
from jjcli import * 
import xml.etree.ElementTree as ET

cli=clfilter("do:")     ## option values in c.opt dictionary

xmls = glob("../recortes/**/*.xml", recursive=True)

print(xmls)

for filename in xmls:  

    tree = ET.parse(filename).getroot()
    for fonte in tree.findall("fonte"):
        print(filename,fonte.attrib) 
        print(fonte.attrib["data"]) 

## ele.tag
## ele.text
## ele.attrib
## ele.findall("tag")
## ele.find("tag")
     
