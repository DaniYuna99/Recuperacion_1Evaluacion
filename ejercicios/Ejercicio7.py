'''
Created on 4 jun 2022

@author: Daniel
'''
"""7.- Escribir un programa que pida un número entero y escriba el número en binario."""

numeroRecibido = int(input("Dime un número: "))
numDividido = numeroRecibido
numBinario = ""
numBiReves = ""

while (numDividido != 1) :
    numBinario = str(numBinario) + str(numDividido % 2)
    numDividido = int(numDividido / 2)
    
    if (numDividido == 1) :
        numBinario += str(1)
    
for i in reversed (numBinario) :
    numBiReves += i
 
print (f"El número {numeroRecibido} en binario es: {numBiReves}")