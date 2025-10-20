#!/usr/bin/env python3
from Bio import SeqIO
total_a = 0
total_t = 0
total_g = 0
total_c = 0
sequence_lengths = []

with open('Python_06.fasta', 'r') as fasta_file:
	for seq_record in SeqIO.parse(fasta_file, 'fasta'):
		print('ID', seq_record.id)
		print('Sequence', seq_record.seq)
		print('Length', len(seq_record))
		sequence_lengths.append(len(seq_record))
		
	#total nts
		total_a += seq_record.seq.count('A')
		total_t += seq_record.count('T')
		total_g += seq_record.count('G')
		total_c += seq_record.count('C')
	
	all_nts = total_a + total_t + total_g + total_c
	print(f'total_number_of_nucleotides: {all_nts}')
		

	avg_seq_len = (sum(sequence_lengths))/4
	print(f'average sequence length: {avg_seq_len}')
	shortest_seq_len = min(sequence_lengths)
	print(f'shortest sequence: {shortest_seq_len}')
	longest_seq_len = max(sequence_lengths)
	print(f'longest sequence:{longest_seq_len}')
		
#question 2 here
#total number sequences
with open('Python_06.fasta', 'r') as fasta_file:
	seq_count = 0
	for line in fasta_file:
		if line.startswith(">"):
			seq_count += 1
		
	print(f'sequence count:{seq_count}')

		
