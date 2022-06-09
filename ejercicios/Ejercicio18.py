'''
Created on 5 jun 2022

@author: Daniel
'''
import random

"""
18.- Realizar un programa que defina un vector llamado “vector_numeros” de 10 enteros, a
continuación lo inicialice con valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla
cada elemento del vector junto con su cuadrado y su cubo.
"""

numeros = []

for i in range (10) :
    numero = random.randint(1,10)
    numeros.append(numero)

print (numeros)

for numero in (numeros) :
    print("-----------------------")
    print (numero)
    print(f"Cuadrado: {numero * numero}")
    print(f"Cubo: {numero * numero * numero}")

