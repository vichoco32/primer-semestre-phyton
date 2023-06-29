#Ejercicio 1 Parcial 2
pal=input("Ingresar palabra: ")
pal=pal.lower()
pal=pal.replace(" "," ")
if pal==pal[::-1]:
    print("La palabra ingresada SÍ es un palíndromo")
else:
    print("La palabra ingresada NO es un palíndromo")