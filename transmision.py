#LLAMADA A LAS CLASES DE HUFFMAN Y HAMMING
from hamming import hamming
from codemorse import hoffman 

#INGRESO DEL TEXTO A CODIFICAR
texto= input("Inserte el mensaje aquí:" )
archivo = hoffman(texto)

#SE GENERA LA MATRIZ QUE SE ENVIARA AL PY-SERIAL
envio = []
for i in archivo:
    mensaje_codificado=hamming(i)
    envio.append(mensaje_codificado)
# "envio" ES LA MATRIZ QUE LLEVA EL TEXTO YA CODIFICADO POR COMPLETO 
print(envio)



