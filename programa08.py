#!/usr/bin/python
# -*- coding: latin1 -*-

print 'Convertendo de real para inteiro'
print 'int(3.14) = ',int(3.14)

print 'Convertendo de inteiro para real'
print 'float(5) = ', 5.0 / 2 + 3

print 'Inteiros em outra base'
print "int('20',8) = ",int('20',8) # base 8
print "int('20',16) = ",int('20',16) # base 16

print 'Operações com números complexos'
c = 3 + 4j
print 'c =',c
print 'Parte real: ',c.real
print 'Parte imaginário: ',c.imag
print 'Conjugado: ',c.conjugate()
