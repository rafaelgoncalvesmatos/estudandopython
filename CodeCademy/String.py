#!/usr/bin/python
# *-* coding:latin1 *-*

# String

print "Método de string: Permitem a realização de tarefas especificas em strings ( textos )"

# Frase trabalhada
frase = "Agua de São Frascisco"
print "A frase que iremos trabalhar é: ", frase

print 'Contando letras com len'
print len(frase)

print "Caixa baixa com lower"
print frase.lower()

print "Caixa alta com upper"
print frase.upper()

print "Exemplo de conversao utilizando str()"
print "O valor de pi e' de cerca de " + str(3.14)

print "Formatacao de string com %"
name = "Rafael Goncalves"
print "Olá %s " % (name)

print "Utilizando varias %s (string)"
name2 = "Amanda Veras"
print "Eu %s tenho 4 anos de namoro com %s." % (name,name2)

print "Sem utilizacao de variavel"
print "Eu %s conclui o ensino superior em %s." % ("Rafael","2014")
