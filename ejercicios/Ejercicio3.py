'''
Created on 4 jun 2022

@author: Daniel
'''
"""3. Realiza un programa que calcule el precio de unas entradas de cine en función del número de
personas y del día de la semana. El precio general de una entrada son 8 euros. El miércoles (día
del espectador), el precio es de 5 euros. Los jueves es el día de la pareja, por lo que la entrada
para dos cuesta 11 euros.
Por ejemplo, si un jueves, un grupo de 6 personas compran entradas, el precio total sería de 33
euros ya que son 3 parejas; pero si es un grupo de 7, pagarán 3 entradas de pareja más 1
individual que son 41 euros (33 + 8).
Además si dispone de la tarjeta CineJacaranda se obtiene un 10% de descuento.

Ejemplo 1:
Número de entradas: 4
Día de la semana (L,M,X,J,V,S,D): L
¿Tienes tarjeta CineJacaranda(S/N)?:
N
El precio de su compra es 32 euros

IMPORTANTE: Para este ejercicio puedes suponer que los datos que se introducen son
todos correctos.
"""

precioEntradaDefault = 8;

numeroEntradas = int(input("¿Cuál es el número de entradas que quieres comprar?: "))
diaSemana = str(input("¿Qué día de semana es?:"))

total = 0;

if (diaSemana == "L" or diaSemana == "M" or diaSemana == "V" or diaSemana == "S" or diaSemana == "D") :
    total = precioEntradaDefault * numeroEntradas;
    
elif (diaSemana == "X") :
    precioEntradaDefault = 5
    total = precioEntradaDefault * numeroEntradas

elif (diaSemana == "J") :
    precioEntradaDefault = 11
 
    if (numeroEntradas % 2 == 0) :
        total = precioEntradaDefault * (numeroEntradas / 2)
        
    else :
        total = (precioEntradaDefault * ((numeroEntradas - 1) / 2) + 8)
    
    
tarjeta = str(input("¿Tienes tarjeta CineJacaranda? (S/N)"))

if (tarjeta == "S") :
    total = total * 0.90
    

print (f"El precio de tu compra es {total} euros.")  




    