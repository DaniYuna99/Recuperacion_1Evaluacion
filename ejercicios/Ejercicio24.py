'''
Created on 6 jun 2022

@author: Daniel
'''

"""
24.- Programa que declare tres vectores ‘vector1’, ‘vector2’ y ‘vector3’ de cinco enteros cada uno,
pida valores para ‘vector1’ y ‘vector2’ y calcule vector3=vector1+vector2.
"""

lista1 = []
for i in range (5) :
    numero = int(input("Número entero para la 1º lista: "))
    lista1.append(numero)
    

lista2 = []    
for i in range (5) :
    numero = int(input("Número entero para la 2º lista: "))
    lista2.append(numero)

lista3 = []

for i in range (len(lista1)) :
    lista3.append(lista1[i] + lista2[i])

print ("La lista resultante de la suma entre los elementos correspondientes de las dos declaradas es: ")
print (lista3)

    