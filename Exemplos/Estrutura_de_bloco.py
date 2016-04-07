#!/usr/bin/python
# *-* coding: latin1 *-*
# By: Rafael Gonçalves de Matos

# Estrutura simples de blocos.

print "Dado a lista de numeros, iremos verificar se é dividido por 3  \
Irá mostrar apenas o numero que sao divididos. \
Segue a lista: \
234,654,378,798,20 "

for i in [234,654,378,798]:

    # Se resto dividindo por 3 for igual a zero:
    if i % 3 == 0:

        # Imprime
        print i, ' / 3 =', i/3

print "Não mostrou o 20, porque 20 não é dividido por 3. :-) "

# ---------------------------------------------------------------

print "Vamos prolongar nosso programa. \
Iremos agora verificar os resultado com numeros 'PAR' dividindo por 2 \
Terá que mostra apenas numero que são divididos por 2 e a lista será um range"

# Range de 1 a 100
for i in range(1,101):

    # Se o resto for zero ele é dividido por 2.
    if i % 2 == 0:

        # Mostre para mim os numero que são divididos por 2.
        print i, ' / 2 =', i/2

print "Repare que só possui numeros par, FIM ;-)"
