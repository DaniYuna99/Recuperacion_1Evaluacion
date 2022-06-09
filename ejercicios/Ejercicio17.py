'''
Created on 5 jun 2022

@author: Daniel
'''

"""17.- Los preprocesadores de los lenguajes de programación como Java o C eliminan del código
fuente los comentarios (/* ….*/) antes de compilarlo. Diseña un método que reciba una sentencia
en Java y devuelva una cadena eliminando los comentarios."""

frase = str(input("Pon una frase con comentarios, y te la devolveré sin ellos: "))

fraseSinComentario = ""
indice = 0
esComentario = False

for letra icaracterase) :
    if (indice + 1 == len(frase)) :
        break
 
    if (letra =caracter and frase[indice + 1] == "*"):
        esComentario = True
        
    elif (letra =caracter and frase[indice - 1] == "*" and esComentario == True) :
        esComentario = False
    
    elif (esComentario == False) :
        fraseSinComentario += letra
caracter
    indice += 1
    
print (fraseSinComentario)
        

