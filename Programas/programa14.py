#!/usr/bin/python
# -*- coding: latin1 -*-

import UserString

print 'É possível usar strings mutáveis no Python, através do módulo UserString,\
que define o tipo MutableString:'

print 'Basicamente ele realiza uma substituicao de caractere'

a = UserString.MutableString('RAFAEL')
a[2:] = 'RAFA'

s = UserString.MutableString('Python')
s[0] = 'p'

print '\nDepois da funcao'
print a
print s
