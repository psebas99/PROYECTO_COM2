
import os
from time import time

class Node: #Declaracion de las variables para crear los nodos 
    probability = 0.0 #Declaracion de float 
    symbol = "" #Variable vacia
    encoding = ""
    visited = False #Variable Boolean
    parent = -1 #longitud de 0 a -1, variable entera

class Huffman: #Declaracion de las variables para la creacion del arbol de Hiffman
    Tree = None #retornar arbol
    Root = None #Retornar Raíx 
    Nodes = [] # Lista Array
    probs = {} #Bloque instancia el metodo 
    dictEncoder = {}
    #DECLARACION DE VARIABLES 
    #1 
    def __init__(self, symbols): #Inicializamos las funciones, con los atributos que va a utilizar
        self.initNodes(symbols) #Retorna valores
        self.buildTree() 
        self.buildDictionary()

    #2 NODOS CON SU PROBABILIDAD RESPECTIVA 
    def initNodes(self, probs): #Creamos los nodos con sus distintas probabilidades
        for symbol in probs:
            node = Node() #Inicializamos el node
            node.symbol = symbol 
            node.probability = probs[symbol]#Asignamos una probabilidad a cada simbolo o a cada letra
            node.visited = False #Variable que no es fija que va a ir cambiando
            self.Nodes.append(node)#Creamos una lista por cada nodo creado 
            self.probs[symbol]=probs[symbol]#Establece para cada probabilidad un simbolo

    #3 CONSTRUCCION DEL ARBOL
    def buildTree(self): # realizamos las operaciones de acuerdo al reglamento para la constucciond el arbol
        indexMin1 = self.getNodeWithMinimumProb() #Buscamos el menos numero de la primera probabilidad 
        indexMin2 = self.getNodeWithMinimumProb() #BUscamos el menos numero de la segunda probabilidad

        while indexMin1 != -1 and indexMin2 != -1: #(!= ecalúa como verdadero si 2 variables son diferentes)
            node = Node()
            node.symbol = "." #Llamo el simbolo digitado para que me de el resultado
            node.encoding = ""
            #Llamamos a las dos probabilidades minimas
            prob1 = self.Nodes[indexMin1].probability
            prob2 = self.Nodes[indexMin2].probability
            node.probability = prob1 + prob2 #Sumamos las probabilidades
            node.visited = False #False = 1
            node.parent = -1 #Restamos la probabilidad a -1
            self.Nodes.append(node)
            self.Nodes[indexMin1].parent = len(self.Nodes) - 1 #Lista o cadena que queremos metadata_dir
            self.Nodes[indexMin2].parent = len(self.Nodes) -1

            #Regla: 0 a mayor probabilidad, 1 a menor probabilidad.
            if prob1 >= prob2:
                self.Nodes[indexMin1].encoding = "0"
                self.Nodes[indexMin2].encoding = "1"
            else: 
                self.Nodes[indexMin1].encoding = "1"
                self.Nodes[indexMin2].encoding = "0"

            indexMin1 = self.getNodeWithMinimumProb()
            indexMin2 = self.getNodeWithMinimumProb()
            
    #4 NODO DE MENOR PROBABILIDAD
    def getNodeWithMinimumProb(self): #Realizamos una comparacion para obtener el nodo de menor probabilidade
        minProb = 1.0 #La minima probabilidad no puede ser mayor de 1
        indexMin = -1 #Indice para restar a la probabilidad

        for index in range(0, len(self.Nodes)): #Index es el numero de probabilidad
            if (self.Nodes[index].probability < minProb and 
               (not self.Nodes[index].visited)): #Si index es menor a 1 es que es falso
                minProb = self.Nodes[index].probability
                indexMin = index #Numero de probabilidad
        #(!= distinto de)
        if indexMin != -1: 
            self.Nodes[indexMin].visited = True

        return indexMin 

    #5 ASIGNACION DE SIGNO A CADA CARACTER QUE CONSTITUYE EL ARBOL DE HUFFMAN
    def showSymbolEncoding(self, symbol):
        found = False
        index = 0
        encoding = "" #Reflejara el resultado

        for i in range(0, len(self.Nodes)):
            if self.Nodes[i].symbol == symbol:
                found = True
                index = i
                break
        if found:
            while index != -1 :#Si found es true entonces mientras index es distinto a -1 se nos guardara en encoding
                encoding = "%s%s" % (self.Nodes[index].encoding, encoding)
                index = self.Nodes[index].parent 
        else:
            encoding = "simbolo desconocido"

        return encoding 

    #6 CONSTRUCCION DE DICCIONARIO
    def buildDictionary(self):

        for symbol in self.probs:
            encoding = self.showSymbolEncoding(symbol)
            self.dictEncoder[symbol] = encoding

    #7 FUNCION - Agrupa los codigos binarios codificados de acuerdo al mensaje escrito en consola
    def encode(self,plain): 
        encoded = ""
        for symbol in plain:
            encoded = "%s%s" % (encoded, self.dictEncoder[symbol])

        return encoded

    #INICIO DE LA DECODIFICACION 
    def decode(self, encoded): #Recibe la cadena del codigo binario enviado desde el emisor para decodificar
        index = 0
        decoded= ""


        while index < len(encoded): #Mientras buscamos en la longitud de la parte codificada

            found = False #Establecemos una variable
            aux = encoded[index:]#Va a buscar a cada parte codificada un simbolo
                                 #No va a ser fija va a ir buscando cual es compatible con cada una
            for symbol in self.probs:
                if aux.startswith(self.dictEncoder[symbol]):#Parte decodificada 
                    decoded = "%s%s" % (decoded, symbol) #Parte decodificada
                    index = index + len(self.dictEncoder[symbol])#Busqueda a}para cada simbolo a cada probabilidad
                    break

        return decoded 
  
  
    #FIN DE LA DECODIFICACION - IMPRESION EN CONSOLA



if __name__=="__main__":
    #print ("\n\n......................CODIFICACION.................\n\n")
    mensaje = input("Ingrese la palabra u oracion: ")
   # print ("\n\nTotal de simbolos:\n\n %s"%(len(mensaje)))
    simbolos=''
    probabilidad= []
    msm=mensaje
    d=0

    for i in mensaje:
        if i in msm:
            simbolos+=i
            probabilidad.append(float(float(msm.count(i))/float(len(mensaje))))
            msm=msm.replace(i,'')
            d+= 1

    symbols=dict(zip(simbolos, probabilidad))#Funcion para llamar al simbolo y a su probabilidad
    #print ("\n\n Simbolos comprimidos: \n\n",d)
    #print ("\n\nPROBABILIDAD DE CADA SIMBOLO: \n\n", symbols)

    tiempo_inicial= time() #Funcion para determinar el timepo del programa

    print(symbols)
    









    #Codificacion de los simbolos 
    huffman = Huffman(symbols) #Llamamos ala clase Huffman
    #print("\n\nSimbolos codificandos usando el arbol de Huffman: \n\n")
    for symbol in symbols:
        print ("Simbolo: %s; Codificacion: %s" % (symbol, huffman.showSymbolEncoding(symbol)))
        print(symbol)
        print(huffman.showSymbolEncoding(symbol))
        
        
    encoded = huffman.encode(mensaje) #Llama funcion tras funcion para el proceso de codifciacion
    #print ("\n\Mensaje que se esta codificando: \n\n%s" % (mensaje))
    #print("\n\nCodificacion en bits : \n\n%s" % (encoded))#Notamos el msj en bits
    #print("\n\nLa longitud de codigo binario es: \n\n%s" % (len(encoded)))

    data = encoded

    #DECODIFICACION
    #print ("\n\n..........................DECODIFICACION...............\n\n")
    decoded = huffman.decode(data) #Llamamos a las funciones correspondientes y el mensaje llamado data
    #print("El codigo binario a decodificar es:\n\n", data)
    #print("\n\nEl mensaje decodificado es: \n\n %s" % (decoded))#Imprimimos el resultado de la funcion decoded

    #Calculo para el tiempo del procedimiento
    tiempo_final= time()
    tiempo_ejecucion= tiempo_final - tiempo_inicial 
   # print('\n\nEl tiempo de transmision es: ', tiempo_ejecucion)

os._exit(0)


