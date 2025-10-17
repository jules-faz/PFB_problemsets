#!/usr/bin/env python3
import re

#problem3
with open("Python_07.fasta", "r") as fasta:
	for line in fasta:
		for head_line in re.findall(">+", line):
			print(line)
		
	
