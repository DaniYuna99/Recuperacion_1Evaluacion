'''
Created on 6 jun 2022

@author: Daniel
'''
import random

"""
22.- Hacer un programa que inicialice un vector de números con valores aleatorios, y 
posterior ordene los elementos de menor a mayor.
"""

lista = []

for i in range (10) :
    numero = random.randint(1,100)
    lista.append(numero)

print (f"Lista de números generada: {lista}")

for i in range (len(lista)) :
    posicionActual = i 
    posicionEncontrada = False 
    
    while (posicionEncontrada == False and posicionActual > 0) :
        if (lista[posicionActual - 1] > lista[posicionActual]) :
            temporal = lista[posicionActual] 
            lista[posicionActual] = lista[posicionActual - 1]
            lista[posicionActual - 1] = temporal
            
            posicionActual -= 1
        
        else :
            posicionEncontrada = True
    
print (f"Lista de números ordenada: {lista}")



