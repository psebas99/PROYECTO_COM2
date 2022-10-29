from os import environ
import math
from hammingdeco import hammingdeco 
from decodemorse import decoder

envio = ['0101010', '0000000', '1111111', '1000011', '0111100', '0111100', '0000000', '1100110', '1111111', '1101001', '1010101', '0100101', '0000000', '0100101', '0000000', '1000011', '1010101', '1000011', '0110011', '0111100', '1000011', '1000011', '0111100', '1010101', '1000011', '0010110', '1111111', '1000011', '0000000', '0100101', '1001100', '0010110', '1111111', '0100101', '1110000', '1101001']
tren=hammingdeco(envio)

n= len(tren)
m = (n/6)
m= math.floor(m) 
segmento=[]
for d in range(m):
    p= 6*d
    segmento.append(tren[p:p+6])

#print(segmento)

texto_morse = []

for f in segmento:
    char_morse = ''
    for g in f:

        if g != '1':
            char_morse+= '-'
        else:
            char_morse+= '.'
    texto_morse.append(char_morse)
    

#print(texto_morse)
palabra = ''

for e in texto_morse:
    #print(e)
    palabra += e + ' '

print(palabra)
decoder(palabra)






 

     




