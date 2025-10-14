#!/usr/bin/env python3
import sys
num = int(sys.argv[1])
if num > 0 and num != 50 and num < 101:
	print("positive")
elif num < 0:
	print("negative")
elif num%2 == 0 and num != 50 and num < 101:
	print ("even")
elif num%2 != 0 and num < 101:
	print("odd")
elif 50 < num < 101:
	print("large number")
elif num < 50:
	print("small number")
elif num%3 == 0 and num < 101:
	print("divisible by 3")
elif num%3 != 0 and num < 101 and num !=50:
	print("not divisible by 3")
else:
	print("number must be 50")

