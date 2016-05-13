#!/usr/bin/python
# *-* coding:latin1 *-*

# Declaracao da funcao

def tax(bill) :
	""" Soma 8% em imposto a conta de restaurante. """
	bill *=1.08
	print "Com imposto: %f" % bill
	return bill
def tip() :
	""" Soma uma gorgeta de 15%. """
	bill *= 1.15
	print "com gorjeta de: %f" % bill
	return bill

# Variaveis
meal_cost = raw_input("Qual o valor do consumo: ")
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)


