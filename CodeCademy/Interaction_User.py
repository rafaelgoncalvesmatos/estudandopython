#!/usr/bin/python
# *-* coding:latin1 *-*

print "Bem-vindo ao tradutor!"

# Perguntando palavra
original = raw_input("Enter a word: ")

# Verificando se a varialvel tem caractere AND verificando string
if len(original) > 0 and original.isalpha() :
	print original 
else :
	print "Empty"

# CONTINUA