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
print 'Exibindo com o operador fica mais facil de trabalhar - segue: %s-%s-%s' % (now.day,now.month,now.year), 'Tudo com %s'

print 'Trabalhando com hora: %s:%s:%s' % (now.hour, now.minute, now.second)

# FIM

