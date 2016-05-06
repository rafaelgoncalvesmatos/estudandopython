#!/usr/bin/python
# *-* coding:latin1 *-*

# Funcoes
def saud() :
    print "OI"

def agra() :
    print "obrigado"

def principal() :
    # Script de perguntas
    print "Esse script de interação."
    nome = raw_input("Qual o seu nome ? ")

    print "Escolha uma das opcões abaixo %s : " % (nome)
    print "1 - Saudações."
    print "2 - Agradecimento."
    resp = raw_input("Opção: ")

    if resp == 1 :
        print "Opcao 1"
        saud()
    elif resp == 2 :
        print "Opcao 2"
        agra()
    else :
        saud()

principal()
