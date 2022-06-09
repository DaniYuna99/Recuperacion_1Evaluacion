'''
Created on 4 jun 2022

@author: Daniel
'''

"""8.- Se desea realizar un programa para validar el código de identificación de 
la seguridad social. El número siempre está formado por 2 partes que llamaremos 
parte A y parte B. El separador de las partes es un guión ‘-’. La parte A está 
formada por caracteres alfabéticos en mayúsculas (al menos dos). La parte B 
está formada sólo por caracteres numéricos (al menos 2).
Las dos partes son intercambiables, es decir, tanto la parte A como la parte B 
pueden ser la primera. Se pide realizar un programa que solicite la  
identificación de la seguridad social e informe de si es o no válida.

Ejemplos de ejecución:

Introduzca la identificación de la SS: AB-345
Es correcta
Introduzca la identificación de la SS: 345-AB
Es correcta
Introduzca la identificación de la SS: 3A45-AB
Es incorrecta
Introduzca la identificación de la SS: 3-45-AB
Es incorrecta"""

def detectarCaracteresIncorrectos (cadena):
    sonLetras = False
    sonNumeros = False
    vistoBueno = False
    
    for chara in (cadena) :
        if (chara.isalpha()) :
            sonLetras = True
        elif (chara.isnumeric()) :
            sonNumeros = True
        
        if (chara.isalpha() and sonLetras == True) :
            vistoBueno = True
    
        if (chara.isnumeric() and sonLetras == True) :
            vistoBueno = False
            break
        
        if (chara.isnumeric() and sonNumeros == True) :
            vistoBueno = True
        
        if (chara.isalpha() and sonNumeros == True) :
            vistoBueno = False 
            break
        
    return (vistoBueno)


# ====== MAIN ====== #     
codigo = str(input("Dime el código de identificación: "))
primeraParte = ""
segundaParte = ""
contGuiones = 0
cambioParte = False

for caracter in (codigo) :
    if (caracter == "-") :
        contGuiones += 1
        cambioParte = True
        if (contGuiones > 1) :
            break

    if (cambioParte == False and caracter != "-") :
        primeraParte += caracter
    elif (cambioParte == True and caracter != "-") :
        segundaParte += caracter

longitudBuena = False

if (len(primeraParte) > 1) and (len(segundaParte) > 1) :
    longitudBuena = True
    
verificacionP1 = detectarCaracteresIncorrectos(primeraParte)
verificacionP2 = detectarCaracteresIncorrectos(segundaParte)


if (verificacionP1 == True and verificacionP2 == True and longitudBuena == True) :
    print ("Está bien.")
elif (verificacionP1 == False or verificacionP2 == False or longitudBuena == False) :
    print ("NO ESTA BIEN.")

# =================================================== #


#HICE SIN QUERER ALGO QUE SEPARA NUMEROS Y LETRAS DE 
#UNA CADENA AUNQUE CONTENGA GUIONES EN DOS VARIABLES
"""for caracter in (codigo) :
    if (caracter == "-") :
        contGuiones += 1
        if (contGuiones > 1) :
            break
        
    if (caracter.isalpha() and parteAlfabetica == False):
        parteAlfabetica = True
    if (caracter.isnumeric() and parteNumerica == False) :
        parteNumerica = True
    if (caracter.isnumeric() and parteAlfabetica == True) :
        parteAlfabetica = False 
    if (caracter.isalpha() and parteNumerica == True) :
        parteNumerica = False

    if (parteAlfabetica == True and caracter != "-") :
        letras += caracter
    elif (parteNumerica == True and caracter != "-") :
        numeros += caracter
 
print (letras)
print (numeros)"""
        
        
        
    







