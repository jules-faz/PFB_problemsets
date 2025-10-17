#!/usr/bin/env python3
import re

with open ("Python_06.fasta", "r") as seq_read:
	fastaDict = {}
	for line in seq_read:
		if line.startswith('>'):
			line =line.rstrip()
			for found in re.finditer(r'^>.*', line):		
				seq_num = line.rstrip()
				fastaDict[seq_num]= ""
		else:			
			for found in re.finditer(r'[^>seq\d]', line):
				seq = line.rstrip()
				fastaDict[seq_num] += seq
	
print(fastaDict)
		

		
