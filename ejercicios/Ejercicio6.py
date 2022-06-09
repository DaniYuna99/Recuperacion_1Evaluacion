'''
Created on 4 jun 2022

@author: Daniel
'''
"""6.- Escribir un programa que lea un número entero y lo descomponga en factores primos. Por
ejemplo 18 = 2 * 3 * 3
"""

def detectorNumPrimo (numero) :
    contadorDivisores = 0
    esPrimo = False;
    
    for i in range (numero + 1) :
        if (numero % (i + 1) == 0) :
            contadorDivisores += 1
        
    if (contadorDivisores == 2) :
        esPrimo = True
        
    return esPrimo;


numeroRecibido = int(input("Dime un número: "))
numDividido = numeroRecibido
listaMultiplos = []

while (numDividido != 1) :
    for i in range (numeroRecibido + 1) :
        if ((detectorNumPrimo(i) == True) and (numDividido % i == 0)) :
            numDividido = numDividido / i
            listaMultiplos.append(i);
            break;

print (f"Los factores primos del número {numeroRecibido} son: {listaMultiplos}")