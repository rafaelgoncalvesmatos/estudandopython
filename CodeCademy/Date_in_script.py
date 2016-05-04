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

print str(now.day) + '/' + str(now.month) + '/' + str(now.year)

data = now.day
print data
