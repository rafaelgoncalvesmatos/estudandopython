#!/usr/bin/python

# Curiosidade

valor = int(raw_input('Entre com o valor: '))

if valor >= 100 :
	print "Valor e maior ou igual a 100 "
elif valor <= 100 :
	print "Valor e menor ou igual a 100 "
else :
	print "Valor nao encontrado."


resp = int(raw_input('Gostaria de realizar uma tabuada [1-sim/2-nao]'))
if resp == 1 :
	tabuada = int(raw_input("Qual tabuada:"))
	range = range(1,11)
	for range in range :
		print tabuada, " * ", range," = ",tabuada * range