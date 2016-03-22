#!/usr/bin/python
# *-* coding: latin1 *-*
# By: Rafael Gonçalves de Matos

# Ilustra a utilizacao de fluxo.

# Coletando informacoes do usuario - Tipo inteiro
temp = int(raw_input('Entre com a temperatura: '))

if temp < 0 :
    print "Muito frio, vai congelar."
elif 0 <= temp <= 20 :
    print "Está frio."
elif 21 <= temp <= 25 :
    print "Temperatura está ambiente."
elif 26 <= temp <= 35 :
    print "Muito quente, vai para praia"
else :
    print "Quente demais, vai para casa!"
