#EJERCICIO 1

numero1 = input("Ingrese numero 1: ")
numero2 = input("Ingrese numero 2: ")
numero3 = input("Ingrese numero 3: ")

menor = numero1
mayor = numero1

if numero2 < menor:
    menor = numero2
elif numero2 > mayor:
    mayor = numero2

if numero3 < menor:
    menor = numero3
elif numero3 > mayor:
    mayor = numero3

print("El numero mayor es: " + mayor)
print("El numero menor es: " + menor)


