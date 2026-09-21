# 1. Modules
# Files .py which can live separate of the main code
# examples calculadora.py and main.py

# import a whole module (.py)
import calculadora

print(calculadora.sumar(10, 5))
print(calculadora.restar(10, 5))

# import just one function
from calculadora import sumar

print(sumar(10, 12))

# import severals functions
from calculadora import restar, sumar

print(sumar(12, 3))
print(restar(12, 3))

# import with as
# you can give a different name to the module
import calculadora as calc

print(calc.sumar(10, 5))
# This is very common when large names


# from .. import *
from calculadora import *

sumar(10, 4)

# python includes a lot of modules already!
import math

print(math.sqrt(25))
print(math.pi)

# important as well
import random

numero = random.randint(1, 10)
print(numero)

# Packages
"""
mi_proyecto/
│
├── main.py
│
└── calculos/
    ├── __init__.py
    ├── matematicas.py
    └── estadisticas.py
    
inside matematicas.py
def sumar(a, b):
    return a + b
    
inside main.py
from calculos.matematicas import sumar
print(sumar(10, 20)) # -> 30
    
    
"""

# Exercise 2. users module
from users import crear_usuario

print(crear_usuario("Cesario", 27))

import random

numeros = [random.randint(1, 101) for x in range(1, 6)]

print(numeros)

mayor = max(numeros)
menor = min(numeros)
avg = sum(numeros) / len(numeros)
print(mayor, menor, avg)

# Excersise 5. Package
from utils.numbers import es_par
from utils.users import crear_usuario

print(es_par(12))
print(crear_usuario("Cesario"))
