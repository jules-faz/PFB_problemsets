#!/usr/bin/env 
import re
with open("Python_07_ApoI.fasta", "r") as ApoI:
    content = ApoI.read()
    found = re.findall(r'([GA][A])[A][T][T][TC]', content)
    print(found)
