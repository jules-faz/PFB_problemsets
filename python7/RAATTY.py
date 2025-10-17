#!/usr/bin/env python3
import re

with open("Python_07_ApoI.fasta", "r") as ApoI:
	content = ApoI.read()
	found = re.findall(r'[GA]AATT[GC]', content)
	print(found)
