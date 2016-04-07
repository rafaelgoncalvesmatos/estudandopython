#!/usr/bin/python
# -*- coding: latin1 -*-

# String unicode
u = u'Hüsker Dü'
# Convertendo para str
s = u.encode('latin1')
print s, '=>', type(s)
# String str
s = 'Hüsker Dü'
u = s.decode('latin1')
print repr(u), '=>', type(u)
