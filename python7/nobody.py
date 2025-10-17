#!/usr/bin/env python3
import re

#problem1
#with open("Python_07_nobody.txt", "r") as nobody_poem:
	#content = nobody_poem.read()
	#print(content)
	#nobody = re.findall(r"Nobody", content)
	#for match in re.finditer(r"Nobody", content):
		#print(f"{match.span()}")
#print(nobody)

#problem2
with open("Python_07_nobody.txt", "r") as nobody_poem:
	content = nobody_poem.read()
	nobody = re.sub(r'Nobody', 'ur mom', content)
print(nobody)

