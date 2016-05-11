#!/usr/bin/python
# *-* coding:latin1 *-*

from __future__ import print_function

print("Work to Loop. for Rafael G. de Matos")

# raw_input("Digit number: ")

num = 60

for test in range(2,num) :

	if num % test == 0 and num != test : 
		print(num, 'equals', test, '*', num/test)
		print(num,'is not a prime number')
		break
else :
	print(num,'is a prime number!')