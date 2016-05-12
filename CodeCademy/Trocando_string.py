#!/usr/bin/python
# *-* coding:latin1 *-*

pyg = 'ay'

original = raw_input('Entre com uma palavra: ')
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:]

# Checando se o usuário colocou a palavra - isalpha falso caso o usuario digite numero
if len(original) > 0 and original.isalpha() :
	print new_word
else :
	print 'empty'

