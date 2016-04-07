#!/usr/bin/python
# -*- coding: latin1 -*-

s = 'Camel'

print 'The ' + s + ' run away!'
print 'Tamanho de %s => %d, Isso utilizando a operacao (s,len(s))' % (s,len(s))
print 'Contando o numero de letras.'

print 'String tratada como sequencia'
for ch in s :
    print ch
print 'Imprimindo com o for em cada linha.'

if s.startswith('C') :
    print s.upper()
    print 'Utilizando o s.upper - podemos deixar a variavel em caixa alta.'

print "Utilizando 'print 3 * s', ele repetira o valor. Que e considerado s+s+s."
print 3 * s

test = 132.1
print "Para converter float para inteiro 'print Agora %d % test ' valor de test = 132.1"
print "Agora %d " % test
