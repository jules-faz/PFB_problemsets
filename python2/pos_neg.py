#!/usr/bin/env python3
num = 25 
if 50 > num > 0 and num != 50:
	print("positive")
elif num < 0:
	print("negative")
elif num < 50 and num%2 != 0:
	print("small number")
elif num%2 == 0 and num !=50:
	print("even steven")
elif num < 50 and num%2 == 0:
	print("it is an even number that is smaller than 50")
elif num > 50 and num%3 != 0:
	print("large number")
elif num%3 == 0 and num < 50:
	print("divisible by 3")
elif num > 50 and num%3 == 0:
	print("it is larger than 50 and divisible by 3")
elif num == 50:
	print("nifty fifty!")
else:
	print("number must be 0")
