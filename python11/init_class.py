#!/usr/bin/env python3
class dna_seq_info(object):
    def __init__(self, sequence, gene_name, organism):
       self.sequence = sequence.upper()
       self.gene_name = gene_name
       self.organism = organism

#create objects
dna_object_1 = dna_seq_info('GATTACA', 'ABCD', 'Homo Sapiens')
dna_object_2 = dna_seq_info('TAAGACGC', 'TNAA', 'Fusobacterium nucleatum')

for i in [dna_object_1, dna_object_2]:
    print('name:', i.gene_name, 'sequence:' , i.sequence)