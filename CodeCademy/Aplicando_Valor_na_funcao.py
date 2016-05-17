#!/usr/bin/python
# *-* coding:latin1 *-*

""" Declaracao da funcao """

def square(n) : 
	""" Retorno o quadrado de um numero """
	squared = n ** 2
	print "%d squared is %d." % (n, squared)
	return squared

""" Chamando a funcao """
square(10)
