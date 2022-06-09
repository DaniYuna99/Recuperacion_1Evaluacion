'''
Created on 6 jun 2022

@author: Daniel
'''
"""
26.- Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que
proporcione la siguiente información:

    ● La temperatura media de cada día.
    ● El día con menor temperatura.
    ● Se lee una temperatura por teclado y se muestran los días cuya temperatura
      máxima coincide con ella. Si no existe ningún día se muestra un mensaje de
      información.
"""
                     
def menu () :
    
    print ("---------------------------------------------------------------------")
    print ("Una vez la lista construida, ¿qué quieres saber ahora?")
    print ("1. La temperatura media de cada día")
    print ("2. El día con menor temperatura")
    print ("3. Mostrar coincidencias dependiendo de la temperatura introducida")
    print ("---------------------------------------------------------------------")
    
    eleccion = int(input("Introducir opción: "))
    
    if (eleccion == 1) :
        tempMedia(listaTemp)
    elif (eleccion == 2) :
        tempMinima(listaTemp)
    elif (eleccion == 3) :
        mostrarCoincidencias(listaTemp)
    else : 
        print ("Has introducido algo que no debes.")
        menu()


#Temperatura media
def tempMedia (listaTemperaturas) :
    for elemento in (listaTemperaturas) :
        print (f"El día {elemento[0]} tiene una temperatura media de {(elemento[1] + elemento[2]) / 2} grados.")


#Dia con menor temperatura
def tempMinima (listaTemperaturas):
    tempMinima = listaTemperaturas[0]
     
    for elemento in (listaTemperaturas) :
        if (elemento[1] < tempMinima[1]) :
            tempMinima = elemento
            
    print (f"El día que tuvo la temperatura más baja fue el día {tempMinima[0]}, con {tempMinima[1]} grados.")


#Temperatura por teclado, y buscar coincidencias
def mostrarCoincidencias (listaTemperaturas):
    tempPorTeclado = int(input("Dime la temperatura. Si encuentro una coincidencia, te lo muestro: "))
    coincidencias = []
    
    for elemento in (listaTemperaturas) :
        if (elemento[1] == tempPorTeclado or elemento[2] == tempPorTeclado) :
            coincidencias.append(elemento)
            
    if (len(coincidencias) != 0) :
        for coincidencia in (coincidencias) :
            print (f"Se han encontrado coincidencias: El día {coincidencia[0]} tuvo como temperatura mínima {coincidencia[1]}, y como máxima {coincidencia[2]}.")
    else :
        print (f"No se encontraron días cuya temperatura mínima o máxima fuera de {tempPorTeclado} grados.")



# ==== ----------- MAIN ----------- ====
listaTemp = []
contador = 0

while (contador <= 5) :
    diaYTemp = []
    
    dia = str(input("Dime la fecha (Formato preferible: Martes, 3 de Enero...): "))
    tempMin = int(input("¿Cuál fue la temperatura mínima de ese día?: "))
    tempMax = int(input("¿Y la temperatura máxima?: "))
    
    diaYTemp.append(dia)
    diaYTemp.append(tempMin)
    diaYTemp.append(tempMax)
    listaTemp.append(diaYTemp)
    
    diaYTemp = []
    
    contador+= 1
    
#Funcion
menu()






