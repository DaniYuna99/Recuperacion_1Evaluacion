'''
Created on 4 jun 2022

@author: Daniel
'''
"""15.- Realizar un método que reciba como argumento una cadena y un carácter y nos devuelva el
número de caracteres que hay entre la primera y la última aparición de un carácter concreto."""

palabraRecibida = str(input("Palabra, poner: "))
letraRecibida = str(input("¿Qué letra?: "))
pistoletazo = False
contador = 0
yaPuedoSalir = False
coincidencia = 0

for letra in (palabraRecibida) :
    if (letra == letraRecibida) :
        pistoletazo = True
        coincidencia += 1
    
    if (letra == letraRecibida and pistoletazo == True and yaPuedoSalir == True) :
        coincidencia += 1
        break
        
    if (letra != letraRecibida and pistoletazo == True) :
        contador += 1
    
    if (pistoletazo == True) :
        yaPuedoSalir = True
        

if (pistoletazo == False) :
    print (f"No se ha encontrado la letra {letraRecibida} en la frase.")
elif (coincidencia < 2) :
    print (f"No se ha encontrado una segunda {letraRecibida}.")
else :
    print (f"La distancia entre el primer caracter {letraRecibida} y la segunda es de {contador} letra(s).")