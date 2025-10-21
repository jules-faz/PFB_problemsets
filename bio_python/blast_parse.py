#!/usr/bin/env python3
from Bio.Blast import NCBIXML

result_handle = open("result.xml")
blast_records = NCBIXML.parse(result_handle)

for blast_record in blast_records:
   query_id = blast_record.query_id
   for alignment in blast_record.alignments:
     for hsp in alignment.hsps:
        if hsp.expect < 1e-10:
           print(f'qid: {query_id} hit_id: {alignment.title} E: {hsp.expect}' )
           # print(query_id, alignment.title, hsp.expect, sep="\t" ) # print tab delimited results table
