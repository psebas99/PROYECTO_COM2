
import math
from hamming import hamming

archivo2=open('Mensaje.txt','w')

#CODIFICACION MORSE
codigo_morse = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
    "g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
    "m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".--.", "q": "--.-",
    "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
    "x": "-..-", "y": "-.--", "z": "--..",
    
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    
    ".": ".-.-.-", ",": "-.-.--", "?": "..--..", "\"": ".-..-."
}

texto_codificado = ""

palabra = input("Ingrese una palabra o texto a codificar: ")

for c in palabra:
    if c != " " and c.lower() in codigo_morse:
        texto_codificado += codigo_morse[c.lower()]
    else:
        texto_codificado += c

texto_binario = ""
print("Texto codificado: {}".format(texto_codificado))

for d in texto_codificado:

    if d!=  "-" :
        texto_binario += "1"
    else:
        texto_binario += "0"
print("Texto codificado en binario: {}".format(texto_binario))

#SEPARACIÓN DE SEGMENTOS 

n= len(texto_binario)
#print(n)
m = (n/4)
m= math.ceil(m)
#print(m)
int(texto_binario)
archivo = []

for i in range(0, m):
    p = 4*i
    archivo.append(texto_binario[p:p+4])
 
#print(archivo)   



jason = []
for i in archivo:
    mensaje_codificado=hamming(i)
    #print(mensaje_codificado)
    jason.append(mensaje_codificado)

print(jason)




