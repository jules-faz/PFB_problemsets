#!/usr/bin/env python3!
#open files & assign to vairables
with open("ferret_transcriptionFactors.tsv", "r") as tf_genes, open("ferret_stemcellproliferation_genes.tsv", "r") as scp_genes:

	#gene sets
	tf_genes_set = set(tf_genes)
	scp_genes_set = set(scp_genes)

#shared genes
shared_genes = tf_genes_set | scp_genes_set
print(f'Ferret genes involved in both transcription factor regulation and stem cell proliferation are: {shared_genes}')
