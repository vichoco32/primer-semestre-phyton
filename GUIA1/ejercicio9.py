#Ejercicio 9

import statistics

numeros = [4,3,8,12,6,10,14,3,6]

#a
numeros.pop()

#b
numeros.insert(0,2)

#c
numeros = list(set(numeros))

#d
media = statistics.mean(numeros)
mediana = statistics.median(numeros)

print("Lista después de las operaciones:", numeros)
print("Media de la lista:", media)