#!/usr/bin/python
# *-* coding: latin1 *-*

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
