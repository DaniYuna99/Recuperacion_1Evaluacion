'''
Created on 5 jun 2022

@author: Daniel
'''

"""11.- Escribir un programa que solicite un número de segundos y muestre por pantalla dicha
cantidad de tiempo en horas, minutos y segundos."""

segundosRecibidos = int(input("Dime los segundos, y los transformo en horas y minutos: "))

minutos = int((segundosRecibidos / 60))
segundosReales = int((segundosRecibidos % 60))
horas = 0

while (minutos >= 60) :
    horas += 1
    minutos -= 60

print (f"{segundosRecibidos} segundos son {horas} hora(s), {minutos} minuto(s), {segundosReales} segundo(s).")

