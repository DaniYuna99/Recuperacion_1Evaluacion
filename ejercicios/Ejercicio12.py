'''
Created on 5 jun 2022

@author: Daniel
'''

"""
12.- Escribir un programa que tenga un método que permita cifrar cadenas de caracteres usando
el algoritmo de cifrado simple consistente en asignar a cada carácter aquel que resulte de sumar
un valor a su código ASCII. El método deberá tener como argumento la cadena a cifrar y el
número a sumar (ambos valores deberán pedirse por teclado antes de llamar a la función). El
método debe pasar la cadena a mayúsculas y devolver la clave cifrada.

Nota. El valor de la Z es 90, por lo que si algún valor da por ejemplo 91 se debe asignar la A que
es el 65.
"""

cadena = str(input("Dime una cadena y lo cifraré modificando los valores ASCII de cada caracter individualmente: "))
cadena = cadena.upper()
valor = int(input("Dame un valor para que esto arranque y cifre según él: "))
cadenaCifrada = ""
letraAscii = 0

for letra in (cadena) :
    letraAscii = ord(letra) + valor
    while (letraAscii > 90) :
        letraAscii = 65 + (letraAscii - 90)
        
    cadenaCifrada += chr(letraAscii)
    
print (cadenaCifrada)