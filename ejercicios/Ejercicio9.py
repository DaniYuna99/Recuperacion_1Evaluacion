'''
Created on 4 jun 2022

@author: Daniel
'''
"""9. Realizar un método que reciba una frase e informe de si es “chachi” o no. Se considera “chachi”
si las 4 primeras letras y las 4 últimas son iguales entre sí. Si es “chachi” devolverá true y false en
caso contrario. Si la cadena no tiene 8 caracteres no podrá ser “chachi”.
El valor 4 debe crearse como constante de manera que el programa siga funcionando si se
modifica dicha constante.

Ejemplo de frases “chachis”:
“Manolo juega al balonmano”
“Ponedle más marcarpone”
En el main pedir al menos una frase al usuario y decir utilizando el método si es “chachi” o no.
"""

palabra2 = str(input("Dime una palabra (o frase) chachi: "))
palabra = palabra2.lower()
letrasDelante = ""
letrasDetras = ""
letrasDetrasSin = ""
contador = 0

if (len(palabra) >= 8) :
    for letra in (palabra) :
        letrasDelcaracter+= str(letra)
        contador += 1
        caracter     if (contador == 4) :
            contador = 0
            break;
    
    for letra2 in reversed (palabra) :
        letrasDetrasSin += str(letra2)
        contador += 1
        
        if (contador == 4) :
            contador = 0
            break;
    
    for letra3 in reversed (letrasDetrasSin) :
        letrasDetras += letra3
        
    if (letrasDelante == letrasDetras) :
        print (f"La palabra (o frase) \"{palabra2}\" es chachi.")
    else :
        print (f"La palabra (o frase) \"{palabra2}\" NO es chachi.")

else :
    print (f"La palabra (o frase) \"{palabra}\" no tiene 8 caracteres o más.")
    



