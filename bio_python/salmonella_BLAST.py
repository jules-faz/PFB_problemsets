#!/usr/bin/env python3
from Bio import SeqIO
import sys

species_search = 'OS=Salmonella paratyphi B'
with open('uniprot_sprot.fasta', 'r') as uniprot:
	for seq_record in SeqIO.parse(uniprot, 'fasta'):
		if species_search in seq_record.description:
			SeqIO.write(seq_record, sys.stdout, 'fasta')
	

