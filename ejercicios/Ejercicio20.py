'''
Created on 5 jun 2022

@author: Daniel
'''

"""
20.- Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno
(comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota
más alta que ha sacado y la menor.
"""
contador = 1
suma = 0

nota = int(input("Introduce una nota: "))
numMin = nota 
numMax = nota
suma += nota

while (contador <= 4 and 10 >= nota >= 0) :
    nota = int(input("Introduce una nota: "))
    
    if (10 >= nota >= 0) :
        
        suma += nota
        
        if (nota < numMin) :
            numMin = nota 
        elif (nota > numMax) :
            numMax = nota
            
        contador += 1
    
    else :
        break

if (nota < 0 or nota > 10) :
    print ("Has insertado un número menor que 0, o más alto que 10.") 
else :
    print (f"La media de las notas es: {suma / contador}, la nota más baja ha sido {numMin} y la nota más alta ha sido {numMax}.")
    
    
    
    
    
    
    
    
    