'''
Created on 4 jun 2022

@author: Daniel
'''
"""4.- Escribir un programa que calcule el mínimo, el máximo y la media de una lista de números
enteros positivos introducidos por el usuario. La lista debe finalizar cuando se produzca un número
negativo."""

numeroRecibido = int(input("Dime un número: "))
numeroMin = numeroRecibido
numeroMax = numeroRecibido
contadorNum = 0;
suma = 0;

if (numeroRecibido == 0) :
    print ("No has iniciado el programa al introducir un número negativo.")

while (numeroRecibido >= 0) :
    contadorNum+= 1
    suma += numeroRecibido
    
    if (numeroRecibido < numeroMin) :
        numeroMin = numeroRecibido
    
    elif (numeroRecibido > numeroMax) :
        numeroMax = numeroRecibido

    numeroRecibido = int(input("Dime un número: "))
    
if (suma != 0) :       
    print ("Te has salido del programa.")
    print (f"El número más pequeño introducido ha sido {numeroMin}, " , 
            f"el número más grande ha sido {numeroMax}, ",
            f"y la media de todos ellos es {suma / contadorNum}.")