'''
Created on 6 jun 2022

@author: Daniel
'''
"""
21.- Programa que declare un vector de diez elementos enteros y pida números para rellenarlo
hasta que se llene el vector o se introduzca un número negativo. Entonces se debe imprimir el
vector (sólo los elementos introducidos).
"""

lista = []

for i in range (0, 10) :
    numero = int(input("Dime un número positivo: "))
    
    if (numero >= 0) :
        lista.append(numero)
    elif (numero < 0) :
        print ("Has introducido un número negativo.")
        break

if (i == 9) :
    print ("Has rellenado la lista.")

    
print (lista)

