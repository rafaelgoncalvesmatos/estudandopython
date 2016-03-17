#!/usr/bin/python

# Trabalhando com loop
s = 0

for x in range(1,100) :
    s = s + x
    print s
    if s >= 3000 :
        print 'Brecou'
        break
    else : 
        print 'Continuando'
        continue
else :
    print 'Fui para o else dentro do for'


