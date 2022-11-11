#!/usr/bin/python3
from jjcli import * 
import xml.etree.ElementTree as ET

cli=clfilter("do:")     ## option values in c.opt dictionary

xmls = glob("../recortes/**/*.xml", recursive=True)

print(xmls)

for filename in xmls:  
    print(f"### {filename}")
    try:
        tree = ET.parse(filename).getroot()
    except Exception as e:
        print(f"   ---> error: {str(e)}")
        continue

    fonte = tree.find("fonte")
    if fonte is not None:
        print(fonte.attrib) 
    else:
        print("???")

## ele.tag
## ele.text
## ele.attrib
## ele.findall("tag")
## ele.find("tag")
     
