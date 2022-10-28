from os import environ
from hammingdeco import hammingdeco 

envio = ['0101010', '0010110', '1111111', '1110000', '0110011', '0001111', '0110011', '0111100', '1111111', '0110011', '0110011', '1101001', '1111111']

tren=hammingdeco(envio)

texto_morse = ""

for d in tren:

    if d!=  "1" :
        texto_morse += "-"
    else:
        texto_morse += "."
        
print(texto_morse)




 

     




