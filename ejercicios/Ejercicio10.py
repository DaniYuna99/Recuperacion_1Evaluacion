'''
Created on 4 jun 2022

@author: Daniel
'''
"""10. Se desea realizar un programa para codificar una cadena formada sólo por números. Para
codificar necesitamos una clave de codificación que será a su vez otra cadena de longitud 10 en la
que no podemos repetir los números.

Veamos cómo se codifica con los siguientes ejemplos. Supongamos que la clave de codificación
es “3651829470”

0 1 2 3 4 5 6 7 8 9    --> Posiciones
3 6 5 1 8 2 9 4 7 0    --> Clave encriptadora

2380 --> 5173

Si deseamos codificar “2380”. La cadena codificada es “5173”. Como vemos, cada número se
sustituye por el que ocupa su posición en la clave de codificación.

Realizar los siguientes métodos:
- Un método llamado codificar que reciba la cadena a codificar y la clave de codificación y
devuelva un String con la cadena codificada.
- Un método llamado decodificar que reciba la cadena codificada y la clave de
codificación y devuelva un String con la cadena decodificada.

Ejemplos de codificación con la clave anterior

Cadena a codificar     Cadena codificada
       129                     650
       4614                   8968"""

#APARTADO A (MÉTODO CODIFICAR)
def codificar (codigo, clave):      
    
    codigoEncriptado = ""
    
    for cifra in (codigo) :
        codigoEncriptado += clave[int(cifra)]
    
    return (f"El código encriptado es: {codigoEncriptado}. No pierdas la clave que has usado.") 


#APARTADO B (MÉTODO DECODIFICAR)
def decodificar (codigoCodificado, clave) :
    
    codigoDesencriptado = ""
   
    for cifra in (codigoCodificado) :
        for clave2 in (clave) :
            if (cifra == clave2) :
                codigoDesencriptado += str(clave.index(cifra))
    
    return (f"El código desencriptado es: {codigoDesencriptado}. Que no te lo roben.") 


#EJEMPLOS QUE VENÍAN JUNTO CON EL ENUNCIADO
print (codificar ("2380", "3651829470"))
print (decodificar ("5173", "3651829470"))
print (codificar ("129", "3651829470"))
print (decodificar ("650", "3651829470"))
















