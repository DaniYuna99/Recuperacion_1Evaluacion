'''
Created on 6 jun 2022

@author: Daniel
'''

"""
23.- Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga
cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar un vector. Para simplificarlo
vamos a suponer que febrero tiene 28 días.
"""

diasMeses = [["Enero", 31], ["Febrero", 28], ["Marzo", 31], ["Abril", 30], ["Mayo", 31], ["Junio", 30], 
             ["Julio", 31], ["Agosto", 31], ["Septiembre", 30], ["Octubre", 31], ["Noviembre", 30], 
             ["Diciembre", 31]]

mes = int(input("¿De cuál mes quieres saber el número de días que tiene? (Dime el número del mes): "))
mes -= 1

if (mes > 12) :
    print ("No hay más de 12 meses. Prueba de nuevo.")
elif (mes <= 0) :
    print ("No existen meses negativos.")
else :
    print (f"El mes {diasMeses[mes][0]} tiene {diasMeses[mes][1]} días.")

    