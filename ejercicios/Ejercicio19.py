'''
Created on 5 jun 2022

@author: Daniel
'''
"""
19.- Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector con datos leídos
por el teclado. Copia los elementos del vector en otro vector pero en orden inverso, y muéstralo
por la pantalla.
"""

caracteres = []

for i in range (5) :
    cadena = str(input("Inserta cadena: "))
    caracteres.append(cadena)

caracteresInversos = []

for chara in reversed (caracteres) :
    caracteresInversos.append(chara)
    
print (f"Caracteres insertados, pero en orden invertido: {caracteresInversos}")
    