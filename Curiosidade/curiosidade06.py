#!/usr/bin/python

# Fucando em condicoes dentro de variaveis

x = range(1,11)
x1 = 1

for x in x :
	print "Valor de x agora e ",x
	print "Valor de x1 e ",x1
	x1 = x1 + 1
	for x1 in x1 :
		print x1,' * ', " = ",x1 * x 
