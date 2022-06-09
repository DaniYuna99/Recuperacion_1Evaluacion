'''
Created on 4 jun 2022

@author: Daniel
'''
"""14.- Realizar un método que reciba una cadena de caracteres y devuelva su valor entero
correspondiente sin utilizar los métodos disponibles propios del lenguaje, es decir, recorriendo la
cadena y calculando su valor."""

numeroRecibido = str(input("Dime un número. Te devolveré su valor en una forma poco convencional: "))

suma = 0
contador = 0
ceros = ""
#370

for cifra in reversed (numeroRecibido) :
    numero = cifra
    
    if (contador > 0) :
        ceros += "0"
    
    numero += ceros
    suma += int(numero)
        
    contador += 1

print (suma)