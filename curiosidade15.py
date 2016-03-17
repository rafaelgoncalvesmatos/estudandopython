#!/usr/bin/python
# -*- coding: latin1 -*-

print "Mesclando conhecimento - Legal\n"

# Primeira opcao
def option1() :
    produtos = [
    ('Caderno','Italacs','12x2','R$12,00'),
    ('Lapis','Faber','30cm','R$4,00'),
    ('Livro','Matematica','14x14','R$56,00'),
    ]

    resp = int(raw_input('1 - Produtos. \
\n2 - Valores. \
\n3 - Tamanho \
\n0 - Voltar. \
\nDigite valor desejado: '))

# $msg tem dois valores de posicao dentro da variavel
#   0 e 1 são ordem das variaveis dentro do msg.format
# esses valores serao usados pelo msg.format
#   - pegando tipo e marca ou b e d no outro exemplo
# por fim, print msg.format utilizara a chamada das 4 variaveis
# dentro da variavel de array produtos
# O nomeclatura foi atribuida por voce, lembrando que tem que possuir
# a merma quantidade de valores por linha no array


    if resp == 1 :
        msg = 'Tipo: {0} - Marca: {1}\n'
        print '\n###################################\n'
        for tipo,marca,tamanho,valor in produtos :
            print msg.format(tipo,marca)
        print '\n###################################\n'
        raw_input('')

    elif resp == 2 :
        print '\n###################################\n'
        msg = 'Marca: {0} {1} - Valor: {2}'
        for a,b,c,d in produtos :
            print msg.format(a,b,d)
        print '\n###################################\n'
        raw_input('')

    elif resp == 3 :
        print '\n###################################\n'
        msg = 'Marca: {0} {1} - Tamanho: {2}'
        for a,b,c,d in produtos :
            print msg.format(a,b,c)
        print '\n###################################\n'
        raw_input('')

    elif resp == 0 :
        print principal()

    else :
        return 'valor não encontrado'

    print option1()

# Segunda funcao
def option2() :
    def otario(x) :
        print '\n########################################'
        print 'Numero selecionado ', x

        for a in range(1,11) :
            print x, ' * ', a , ' = ', x * a

        print 'Ele mesmo ', x , ' * ' , x , ' = ', x * x
        print '\n########################################'

    multiplicacao = int(raw_input('\nDigite um numero: '))
    print otario(multiplicacao)
    print option2()

# Funcao principal
def principal() :
    princ = int(raw_input('\nEscolha opcao: \
\n1 - Produtos \
\n2 - Tabuada \
\n0 - Sair \
\nEscolha opcao: '))

    if princ == 1 :
        print option1()

    elif princ == 2 :
        print option2()

    elif princ == 0 :
        return 'bye'


print principal()
