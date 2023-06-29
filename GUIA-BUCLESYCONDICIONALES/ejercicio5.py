#Ejercicio 5
import random

numeros = [random.randint(40, 350) for _ in range(20)]

print("Números generados:", numeros)

numero_buscado = int(input("Ingrese un número para buscar en la lista: "))

ocurrencias = numeros.count(numero_buscado)

print(f"El número {numero_buscado} aparece {ocurrencias} veces en la lista.")