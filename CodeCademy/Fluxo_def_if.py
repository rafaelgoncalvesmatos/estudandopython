#!/usr/bin/python
# *-* coding:latin1 *-*

# Declarando função chamada clinic
def clinic():
    print "Você entrou na clinica!"
    print "Entra pela porta esquerda (left) ou a direita (right) ?"

    # Perguntando a opcao desejada
    answer = raw_input("Digite left ou right e pressione enter: ").lower()

    # Se resposta for left
    if answer == 'left' or answer == 'l' :
            print "Está e a sala de massagem!"

    # Se resposta for right
    elif answer == 'right' or answer == 'r' :
        print "É claro que esta e a sala de discussoes."

    # Se nao seleciona nenhuma
    else :
        print "Você nao escolheu nenhuma das opcoes citadas."
        clinic()

# Aqui a função é chamada
clinic()
