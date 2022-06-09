'''
Created on 4 jun 2022

@author: Daniel
'''
"""5.- Escribir un programa que pregunte cuántas decimales (máximo 4 decimales) queremos en el
número pi, y muestre el número pi con los decimales adecuados. Para calcular el número pi se
puede utilizar la siguiente fórmula pi = 4* (1 -1/3 + 1/5 -1/7 ….)
"""

def calcularPi () :
    pi = 4 
    producto = 0
    par = 0
    
    for i in range (1, 99999, 2):
        if (par % 2 == 0) :
            producto += (1/i)
        else :
            producto -= (1/i)
        par += 1
    
    return (pi * producto)


###-------    MAIN    -------###
eleccion = int(input("¿Cuántos decimales quieres en el número Pi? (Máximo 4 decimales) "))

piOmega = 0

if (eleccion == 0) :
    piOmega = round(calcularPi(), 0)
    print (int(piOmega))
elif (eleccion == 1) :
    piOmega = round(calcularPi(), 1)
    print (piOmega)
elif (eleccion == 2) :
    piOmega = round(calcularPi(), 2)
    print (piOmega)
elif (eleccion == 3) :
    piOmega = round(calcularPi(), 3)
    print (piOmega)
elif (eleccion == 4) :
    piOmega = round(calcularPi(), 4) 
    print (piOmega)
else :
    print ("El número que has introducido no está permitido, o has puesto un caracter.")



