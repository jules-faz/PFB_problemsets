#!/usr/bin/env python3
from Bio import SeqIO
with open('Python_06.fasta', 'r') as fasta_file:
	for seq_record in SeqIO.parse(fasta_file, 'fasta'):
		print('ID', seq_record.id)
		print('Sequence', seq_record.seq)
		print('Length', len(seq_record))
