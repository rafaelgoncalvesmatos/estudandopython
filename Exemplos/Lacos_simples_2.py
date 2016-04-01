#!/usr/bin/python
# *-* coding: latin1 *-*

# Criando estrutura de lacos com o while
# Soma de 0 a 99

# Desclaracao de variavel
s = int(raw_input("Digite o numero de começo: "))
x = 1

while x < 100 :
    s = s + x
    x = x + 1
print s
