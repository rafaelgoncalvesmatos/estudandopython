#!/usr/bin/python
# -*- coding: latin1 -*-

s = 'Rafael '
a = 'Linux '

# Concatenacao
print 'concatenação'
print 'The' + s + 'run away!'

# Interpolação
print '\ninterpolação'
print 'tamanho de %s => %d' % (s,len(s))

# String tratada como sequencia
print '\nString tratada como sequencia'
for ch in s: print ch

# Strings sao objetos
print 'Strings sao objetos'
if s.startswith('R'): print s.upper()

if a.startswith('Ot'):
    print '\nValor da variavel a = ', a, a.upper()
    print 'Otario comeca com O entao - Voce é um otario'

# O q acontecera
print '\nO que acontecera? '
print 3 * s

# 3 * s é consistente com s + s + s Q

# Vamos continuar com a mesma linha de racicinio
print '\nContinuando com a mesma linha de raciocinio'
print '\b\b\b', 10 * ( s + a )
