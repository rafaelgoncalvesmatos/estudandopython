#!/usr/bin/python
# -*- coding: latin1 -*-

import string

# Importando modulo string
print 'Importando modulo string - import string.'

print 'O alfabeto'
a = string.ascii_letters

print '\nConteudo da variavel a - a = string.ascii_letters'
print a

print '\nRodando o alfabeto um caractere para a esquerda.'
b = a[1:]+a[0]

tab = string.maketrans(a,b)

msg = "'Esse texto será traduzido..Vai ficar bem estranho.'"

print string.translate(msg,tab)
