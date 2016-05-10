#!/usr/bin/python
# *-* coding:latin1 *-*

print "Utilizando função."

def first_function() : 
	print "Primeira funcao."
	print ""

def second_fuction() :
	print "Segunda funcao."
	print ""

def principal() :
 	print "Existe duas opcoes: "
	print "	1	- First"
	print "	2	- Second"
	print "	3 	- Quit"
	resp = raw_input("Qual funcao ? ")

	if resp == "first" or resp == "1" :
		first_function()
		principal()
	elif resp == "second" or resp == "2" :
		second_fuction() 
		principal()
	elif resp == "quit" or resp == "q" : 
		print "Saindo"
	else :
		print "Digite uma das opcoes validas"
		principal()

principal()