#/usr/bin/python
# *-* coding:latin1 *-*

for i in range(1,100) :
    for a in range (1,5):
        print i , a 
        print 'Tudo certo'

# Declaração de módulos
import string

# Começo
print "Trabalhando com o módulo string"

# String template
st = string.Template('$aviso aconteceu em $quando. Estatus: $status')

# Preenche o modelo com um dicionáRealizando
s = st.substitute({'aviso':'Falta de Eletricidade','quando':'03 de Março de 2016','status':'Não Paga'})

# Mostrando valor
print s
