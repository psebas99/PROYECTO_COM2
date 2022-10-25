from operator import xor

aux=int


p1=int
p2=int
p3=int
p4=int

e1=int
e2=int
e3=int
e4=int

er=int

correlativo=int
correlativo1=int

mensaje=str('') 
mensaje1=str('')

archivo1=open('Mensajes_incorrectos.txt','w')
archivo2=open('Mensajes_correctos.txt','w')

archivo='Hamming_incorrecto.txt'

with open(archivo) as objeto:
    for palabra in objeto:



        for i in range(0,12):
            if i==0:
                b1=int(palabra[0])
            if i==1:
                b2=int(palabra[1])
            if i==2:
                b3=int(palabra[2])
            if i==3:
                b4=int(palabra[3])
            if i==4:
                b5=int(palabra[4])
            if i==5:
                b6=int(palabra[5])
            if i==6:
                b7=int(palabra[6])
            if i==7:
                b8=int(palabra[7])
            if i==8:
                b9=int(palabra[8])
            if i==9:
                b10=int(palabra[9])
            if i==10:
                b11=int(palabra[10])
            if i==11:
                b12=int(palabra[11])
            

        p1=xor(b3,b5)
        p1=xor(p1,b7)
        p1=xor(p1,b9)
        p1=xor(p1,b11)
        p2=xor(b3,b6)
        p2=xor(p2,b7)
        p2=xor(p2,b10)
        p2=xor(p2,b11)
        p3=xor(b5,b6)
        p3=xor(p3,b7)
        p3=xor(p3,b12)
        p4=xor(b9,b10)
        p4=xor(p4,b11)
        p4=xor(p4,b12)
        e1=xor(p1,b1)
        e2=xor(p2,b2)
        e3=xor(p3,b4)
        e4=xor(p4,b8)
        er=(8*e4)+(4*e3)+(2*e2)+(1*e1)

        correlativo1=(128*b3)+(64*b5)+(32*b6)+(16*b7)+(8*b9)+(4*b10)+(2*b11)+(1*b12)
            
        if er==3:
            if b3==1:b3=0
            else: b3=1

        if er==5:
            if b5==1:b5=0
            else: b5=1

        if er==6:
            if b6==1:b6=0
            else: b6=1

        if er==7:
            if b7==1:b7=0
            else: b7=1    

        if er==9:
            if b9==1:b9=0
            else: b7=1

        if er==10:
            if b10==1:b10=0
            else: b10=1

        if er==11:
            if b11==1:b11=0
            else: b11=1    

        if er==12:
            if b12==1:b12=0
            else: b12=1    


        correlativo=(128*b3)+(64*b5)+(32*b6)+(16*b7)+(8*b9)+(4*b10)+(2*b11)+(1*b12)
        mensaje=mensaje+chr(correlativo)
        mensaje1=mensaje1+chr(correlativo1)

archivo2.write(mensaje+"\n")
archivo1.write(mensaje1+"\n")
print("Su mensajae correcto es:",mensaje)
print("Su mensaje incorrecto es:",mensaje1)