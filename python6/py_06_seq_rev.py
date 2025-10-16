#!/usr/bin/env
with open("Python_06.seq.txt", "r") as py6_seq:
	for line in py6_seq:
		line = line.rstrip()
		print(line[::-1])
print("Sequence name: [name here]\nNote: this is the reverse complement\n")
