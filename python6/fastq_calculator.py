#!/usr/bin/env
with open ("Python_06.fastq", "r") as py6_fastq:
	#create variables
	amt_lines = 0
	amt_IDs = 0
	amt_char = 0
	amt_nt = 0
	len_sums = []
	len_seq_sum = []
		
	for line in py6_fastq:	
		#count total number of lines
		amt_lines += 1
		
		#count total number of sequence IDs
		if line.startswith("@"):
			amt_IDs += 1
		#count total number of characters
		for char in line:
			amt_char += 1

		#count total number of nucleotides
		line = line.rstrip()
		for char in line:
			amt_nt += 1
		
		#calculate average length of all the lines
		len_sums.append(len(line))

		#calculate the average line length of sequences
		if line[0] == "A" or line[0]=="T" or line[0]=="G" or line[0]=="C":
			line = line.rstrip()
			len_seq_sum.append(len(line))


len_avg = (sum(len_sums))/120
len_seq_avg =(sum(len_seq_sum))/30

#print final outputs
print(f'amount of lines: {amt_lines}')
print(f'amount of IDs: {amt_IDs}')
print(f'amount of characters: {amt_char}')
print(f'amount of nucleotides: {amt_nt}')
print(f'average line lenght: {len_avg}')
print(f'average sequence length: {len_seq_avg}')
