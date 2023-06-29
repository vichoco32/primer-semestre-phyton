#EJERCICIO 2

palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")

lon_palabra1 = len(palabra1)
lon_palabra2 = len(palabra2)
if lon_palabra1 > lon_palabra2:
    print("La primera palabra tiene más caracteres.")
    print("La segunda palabra tiene menos caracteres.")
elif lon_palabra1 < lon_palabra2:
    print("La segunda palabra tiene más caracteres.")
    print("La primera palabra tiene menos caracteres.")
else:
    print("Ambas palabras tienen la misma cantidad de caracteres.")