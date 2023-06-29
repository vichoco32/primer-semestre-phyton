#Ejercicio 1
texto = "La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participación democrática."
texto = texto.lower()
palabras = texto.split()
contador = 0
palabras_encontradas = []
for palabra in palabras:
    if palabra == "universidad":
        contador += 1
        palabras_encontradas.append(palabra)


print("La palabra 'universidad' se repite", contador, "veces.")

tupla_palabras = tuple(palabras_encontradas)

print("Palabras encontradas:", tupla_palabras)