#!/usr/bin/python
# *-* coding: latin1 *-*

# Criando estrutura de lacos com o for

# Realizando some de forma simples.
s = 0

for x in range(1,100):
    s = s + x

    # Utilizando o break caso o resultado seja igual a dois.
    if s == 2:
        break

# Depois de terminar o laco ele manda escreve.
else:
    print 'Terminou ?'

# Mostrando o total.
print s
