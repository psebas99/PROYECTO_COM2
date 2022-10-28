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


texto_codificado = []

palabra = ['a', 'b', 'c', 'd', 'e', 'f','g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?']

for c in palabra:
    if c != " " and c.lower() in codigo_morse:
        texto_codificado.append(codigo_morse[c.lower()])
    else:
        texto_codificado.append(c)

texto_binario = []
print("Texto codificado: {}".format(texto_codificado))
letras = ""
for d in texto_codificado:
    for e in d:
        if e!=  "-" :
            letras += "1"
        else:
            letras += "0"
    texto_binario.append(letras)
    letras = ""


print("Texto codificado en binario: {}".format(texto_binario))


