#!/usr/bin/python
# *-* coding:latin1 *-*

""" Demostracao dos operações matematicas em python
Uma breve descrição de cada um """

a = 20
b = 2

print "Valor a = 20 e b = 2"

print 'Trabalhando com soma'
print a + b

print 'Trabalhando com subtracao'
print a - b

print 'Trabalhando com multiplicacao'
print a * b

print 'Trabalhando com divisao'
print a / b

print 'Trabalhando com elevacao'
print a ** b

print 'Trabalhando com resto, se retornar 0 é divisivel'
print a % b

print '------------------------------------------------'
print 'Exemplo: Restaurante.\
Conta: $53,23 \
Imposto: 0.6% \
Gorjeta: 15% \
Veja o código...'

conta = 53.23
imposto = 0.06
gorjeta = 0.15

# Conta + Imposto
conta = conta + conta * imposto
print 'Valor da contas mais imposto: ', conta

# Conta + Imposto + Gorjeta
conta = conta + conta * gorjeta
print 'Valor da conta, mais impostos e mais gorjeta: ', conta

# Terminando
print 'Utilizando duas casas utiliza %.2f. Valor: ', ("%.2f" % conta)
print 'Olhe CÓDIGO!!! :-)'
print '------------------------------------------------'

a = "Sapato"[1-4]

print a
