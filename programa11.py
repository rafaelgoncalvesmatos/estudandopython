#!/usr/bin/python
# -*- coding: latin1 -*-

print 'Outro tipo de interpolação ao inves de % - após versão 2.6'


musicos = [('Page','guitarrista','Led Zeppelin','Otimo'),
('Fripp','guitarrista','King Crimson','Agradavel'),
('Core','baterista','Ramones','Otimo')]

# Parametros identificados pela ordem
print 'Parametros identificados pela ordem'
msg = '{0} é {1} do {2} e o nivel é {3}'

for nome,funcao,banda,nivel in musicos:
    print '\n',(msg.format(nome,funcao,banda,nivel))
    maiusculo = (msg.format(nome,funcao,banda,nivel))
    print maiusculo.upper()

# Parametro identificados pelo nome
print '\nParametro identificados pelo nome'
msg = '{saudacao}, são {hora:02d}:{minuto:02d}'
print msg.format(saudacao='Bom dia',hora=7,minuto=30)

# Funcao bulrin format()
print '\nFuncao bulrin format()'
print 'Pi =', format(3.14159,'.3e')
