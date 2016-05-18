#!/usr/bin/python

# Esse import é para usar com math.sqrt
import math
# Esse import é para pegar funcoes em outros arquivos
import fun
# Esse é um import de uma funcao especifica
from math import sqrt
# Ou importacao universal 
# from math import *

# Chamando funcao salario do arquivo fun.py
fun.salario(10)

# Podendo usar das duas formas, dessa
print sqrt(25)

# Ou dessa
print math.sqrt(25)

