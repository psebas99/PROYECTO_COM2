from operator import xor

aux = int

d1=int
d2=int
d3=int
d4=int

p1 = int
p2 = int
p3 = int

p11=int
p12=int
p13=int


e1 = int
e2 = int
e3 = int

er = int

correlativo = int
correlativo1 = int

mensaje = str('')
mensaje1 = str('')

# archivo1=open('Mensajes_incorrectos.txt','w')
# archivo2=open('Mensajes_correctos.txt','w')
#texto = ['0101010', '1010101', '1110000', '0001111', '0000000']
palabra = ['0101010', '1010101', '1110000', '0001111', '0000000']

for j in palabra:

    for i in j:
        if i == 0:
            p1 = int(j[0])
        if i == 1:
            p2 = int(j[1])
        if i == 2:
            d1 = int(j[2])
        if i == 3:
            p3 = int(j[3])
        if i == 4:
            d2 = int(j[4])
        if i == 5:
            d3 = int(j[5])
        if i == 6:
            d4 = int(j[6])

    print(str(p1))



