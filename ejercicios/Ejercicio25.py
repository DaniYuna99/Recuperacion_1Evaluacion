'''
Created on 6 jun 2022

@author: Daniel
'''
"""
25.- Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un
programa que introduzca el nombre y la edad de cada alumno. El proceso de lectura de datos
terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrarán los
siguientes datos:

● Todos los alumnos mayores de edad.
"""

listaAlumnos = []
alumno = []

nombre = str(input("Introduce el nombre del alumno: ")) 

while (nombre != "*") :
    edad = int(input("Introduce la edad del alumno: "))
    alumno.append(nombre)
    alumno.append(edad)
    listaAlumnos.append(alumno)
    alumno = []
    nombre = str(input("Introduce el nombre del alumno: ")) 

#alumnos = [["Daniel", 22],["Fernando", 35],["Alejandro", 13],["Paula", 46],["Cintia", 17]]
alumnosMayores = []

for elemento in (listaAlumnos) :
    if (elemento[1] >= 18) :
        alumnosMayores.append(elemento)
        
print (f"De entre los alumnos declarados, los que son mayores de edad son: {alumnosMayores}")


