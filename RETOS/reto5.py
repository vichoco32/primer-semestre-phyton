#Reto en clase n°5

def numeroprimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeropar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
def mayor50(numero):
    if numero > 50:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))

if numeropar(numero):
    print("El número es par.")
else:
    print("El número es impar.")
if numeroprimo(numero):
    print("El número es primo.")
else:
    print("El número no es primo.")
if mayor50(numero):
    print("El número es mayor que 50.")
else:
    print("El número es menor o igual a 50.")