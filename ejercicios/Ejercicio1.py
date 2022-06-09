'''
Created on 4 jun 2022

@author: Daniel
'''

"""1.- Realizar un programa que lea un número entero por teclado e indique si el número se puede
expresar como el cuadrado de un número entero."""

numeroPedido = int(input("Dime un numero:"));
daCuadrado = False;

for i in range (numeroPedido) :
    if ((i * i) == numeroPedido) :
        num = i;
        daCuadrado = True;

if (daCuadrado == True) :
    print (f"{num}, al elevarse al cuadrado, da {numeroPedido}. ")
else :
    print (f"Ningun numero da {numeroPedido} al elevarse al cuadrado.")
