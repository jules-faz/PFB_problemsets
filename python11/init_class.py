#!/usr/bin/env python3
class dna_seq_info(object):
    def __init__(self, sequence, gene_name, organism):
       self.sequence = sequence.upper()
       self.gene_name = gene_name
       self.organism = organism

    #sequence length method:
    def seq_length(self):
        seq_l = len(self.sequence)
        return seq_l
    
    #nucleotide count + GC content methods:
    def nt_count(self):
        a_count = self.sequence.count('A')
        t_count = self.sequence.count('T')
        g_count = self.sequence.count('G')
        c_count = self.sequence.count('C')
        GC_content = (g_count + c_count)/len(self.sequence)
        return a_count, t_count, g_count, c_count
        
    #FASTA formatter method
    def fasta_formatter(self):
            fasta_header = "> seq#" + "\n"
            for line in self.sequence:
                 seq_fasta = self.sequence[0] + fasta_header + self.sequence
            return seq_fasta
                 

#create objects
dna_object_1 = dna_seq_info('GATTACA', 'ABCD', 'Homo Sapiens')
dna_object_2 = dna_seq_info('TAAGACGC', 'TNAA', 'Fusobacterium nucleatum')

for i in [dna_object_1, dna_object_2]:
    print('name:', i.gene_name, 'sequence:' , i.sequence, 'sequence_length:', 
    i.seq_length(), 'nt count:', i.nt_count(), 'fasta:', i.fasta_formatter())