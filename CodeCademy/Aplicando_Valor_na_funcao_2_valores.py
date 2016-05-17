#!/usr/bin/bash
# *-* coding:latin1 *-*

# Declaracao da funcao onde q o base = 37 e exponent = 4
def power(base, exponent) : 
	result = base ** exponent
	print "%d elevado a %d e %d." % (base, exponent, result)

# Chamando a funcao adicionando dois valores
power(37, 4)