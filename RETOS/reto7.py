#Reto en clase n°7

def long_pal(frase):
    palabras = frase.split()
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    return diccionario

frase = input("Ingresar frase: ")
resultado = long_pal(frase)
print(resultado)