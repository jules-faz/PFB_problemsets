#!/usr/bin/env python3
with open ("Python_06.fasta", "r") as seq_read:
	fastaDict = {}
	for line in seq_read:
		line =line.rstrip()
		if line.startswith(">"):		
			seq_num = line.rstrip()
			fastaDict[seq_num]= ""
			print(fastaDict)
			#print(seq_num)
			#for key, value in fastaDict:
				#fastaDict = seq_num
		else:
			seq = line.rstrip()
			fastaDict[seq_num] += seq
			print(fastaDict)
			#print(line)
			#for key, value in fastaDict:
				#fastaDict[seq_num] = seq


print(fastaDict)
		

		
