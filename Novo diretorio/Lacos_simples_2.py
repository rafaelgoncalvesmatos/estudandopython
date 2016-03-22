#!/usr/bin/python
# *-* coding: latin1 *-*

# Criando estrutura de lacos com o while

# Realizando some de forma simples.
s = 0

for x in range(1,100):
    s = s + x

    # Utilizando o break caso o resultado seja igual a dois.
    if s == 2:
        break

else:
    print 'Terminou ?'

print s
