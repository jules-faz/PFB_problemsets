#!/usr/bin/env
with open("Python_06.txt", "r") as py3, open("Python_06_uc.txt","w") as py3_uc:
	for line in py3:
		print(line.upper())
		uc = line.upper()
		py3_uc.write(f' {uc}')
