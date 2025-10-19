#!/usr/bin/env python3


def GC_calculator(dna):
	g_count = dna.count('G')
	c_count = dna.count('C')
	dna_len = len(dna)
	gc_content = (g_count + c_count) / dna_len
	return gc_content


