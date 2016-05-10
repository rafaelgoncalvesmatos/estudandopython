#!/usr/bin/python
# *-* coding:latin1 *-*

print "Comecando com o funcoes"

def funcao_principal(answer) : 
	if answer > 5 :
		return 1
	elif answer < 5 : 
		return -1
	else : 
		return 0 

# Chamando a funcao com o valores definidos para a variavel "answer"
print funcao_principal(4)
print funcao_principal(5)
print funcao_principal(6)

