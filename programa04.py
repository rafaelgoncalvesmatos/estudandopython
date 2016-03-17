#!/usr/bin/python

# Trabalhando com condicao, recebendo valores de usuario

# recebendo variavel

temp = int(raw_input('Entre com a temperatura: '))

print temp

if temp < 0 :
	print 'Congelado...'
elif 0 <= temp <= 20 :
	print 'Frio...'
elif 21 <= temp <= 25 :
	print 'Normal...'
elif 26 <= temp <= 35 :
	print 'Quente...'
else 
:	print 'Muito quente!'
