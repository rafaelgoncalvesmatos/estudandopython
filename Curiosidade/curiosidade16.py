#!/usr/bin/python
# -*- coding: latin1 -*-

import string

print 'Brincando com string'

b = 'Trabalhando com texto'
a = string.hexdigits

print 'Trabalhando com formatacao de texto'
print '{:^30}'.format(b),'centralizado'
print '{:<30}'.format(b),'30 a esquerda'
print '{:>30}'.format(b),'30 a direita'
print '{:>40}'.format(b),'40 a direita'


print 'Trabalhando com valores como variaveis'
print 'Coordinates: {latitude},{longitude}'.format(latitude='15N',longitude='30W')

print 'Trabalhando com numero'

print 'Porcentagem'
points = 19.5
total = 22
print 'Porcentagem: {:.2%}'.format(points/total)
