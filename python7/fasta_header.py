#!/usr/bin/env python3
import re

#problem3
with open("Python_07.fasta", "r") as fasta:
	info = {}
	for line in fasta:
		for head_line in re.finditer(r"^>+(\w*)\|\S+\s(.*)", line):
			id = head_line.group(1)
			desc = head_line.group(2)
			print(f'id:{id}')
			print(f'desc:{desc}')
				
#problem4		
	
