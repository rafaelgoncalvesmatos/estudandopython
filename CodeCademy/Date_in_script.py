#!/usr/bn/python
# *-* coding:latin1 *-*

from datetime import datetime
now = datetime.now()

print 'Para ver todas informações de data ', now, ' \
'
print 'Este ano de ', now.year
print 'Estamos no mês ', now.month
print 'No dia ', now.day

# varialvel

print 'Exibindo com o operador + e atribuindo a cada variavel o tipo string: ',str(now.day) + '/' + str(now.month) + '/' + str(now.year)
print 'Exibindo com o operador % fica mais facil de trabalhar - %s, segue: %s-%s-%s' % (now.day,now.month,now.year)
data = now.day
print data
