'''
Created on 4 jun 2022

@author: Daniel
'''
"""2.- Realizar un programa que lea números enteros hasta que se pulse un número negativo y
muestre la suma de la suma de los números introducidos, desde 1 al número que se ha
introducido. Por ejemplo, si se introduce el 3, el 5, el 10 y el -2. Se deberá sumar 1+2+3 +
1+2+3+4+5 + 1+2+3+4+5+6+7+8+9+10"""

numeroRecibido = int(input("Dime un numero:"))

if (numeroRecibido <= 0) :
    print ("Te has salido del programa sin introducir números.")

suma = 0;
    
while (numeroRecibido > 0) :
    for i in range (numeroRecibido + 1) :
        suma += i;
    
    numeroRecibido = int(input("Dime un numero:"))

if (suma != 0) :
    print (f"Te has salido del programa. La suma de la suma de los números introducidos es: {suma}.")