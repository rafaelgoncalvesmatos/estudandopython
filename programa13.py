#!/usr/bin/python
# -*- coding: latin1 -*-

import string

print 'Cria uma string template'
st = string.Template('$aviso aconteceu em $quando')

print 'Preenche o modelo com um dicionario\n'
s = st.substitute({
'aviso':'Falta de eletricidade',
'quando':'03 de abril de 2002'})

a = st.substitute({
'aviso':'Falta de agua',
'quando':'03 de agosto 2011'
})

print s , '\n e \n', a
