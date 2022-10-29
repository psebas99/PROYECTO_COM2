from os import environ
import math
from hammingdeco import hammingdeco 
#from decodemorse import decoder

envio = ['1001100', '0100101', '0100101', '1101001', '1001100', '1111111', '1000011', '1110000', '1001100', '0000000', '1001100', '1010101', '0101010', '0100101', '1000011', '0000000', '0011001', '0101010', '1000011', '0111100', '1111111', '1000011', '1010101', '1000011', '0000000', '0111100', '1111111', '1000011', '1001100', '1111111', '1000011', '0000000', '0100101', '1001100', '1010101', '1100110', '0000000', '1001100', '0100101', '1000011', '1110000', '0111100', '0000000', '0100101', '1100110', '0101010', '1001100', '1001100', '0000000', '1001100']
tren=hammingdeco(envio)

n= len(tren)
m = (n/6)
m= math.floor(m) 
segmento=[]
for d in range(m):
    p= 6*d
    segmento.append(tren[p:p+6])

print(segmento)

texto_morse = []

for f in segmento:
    char_morse = ''
    for g in f:

        if g != '1':
            char_morse+= '-'
        else:
            char_morse+= '.'
    texto_morse.append(char_morse)
    

print(texto_morse)

#decoder(texto_morse)






 

     




