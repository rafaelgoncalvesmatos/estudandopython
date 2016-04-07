#!/usr/bin/python

# Interagindo com usuarios atraves de um loop

resp = int(raw_input('Digite o intervalo que voce deseja: '))

if resp <= 1 : print 'Coloque o valor acima de 1...'

for x in range(0,101,resp) :
    print 'Intervalo que voce desejou: ',x

