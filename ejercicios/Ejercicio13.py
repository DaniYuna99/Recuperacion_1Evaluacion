'''
Created on 4 jun 2022

@author: Daniel
'''
"""13.- Escribir un programa que tenga una función que determine si una cadena de caracteres es
palíndroma o no (se lee igual de izquierda a derecha que de la derecha a izquierda)."""

palabra = str(input("Introduce una palabra: "))
palabraInvertida = ""

for lecaractern reversed (palabra) :
    palabraInvertida += lecaracter     
if (palabra == palabraInvertida) :
    print (f"La palabra \"{palabra}\" es palíndroma.")
else :
    print (f"La palabra \"{palabra}\" NO es palíndroma.")