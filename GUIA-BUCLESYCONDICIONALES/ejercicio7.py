#Ejercicio 7
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n - 1)
n=int(input("Ingresar número entero que sea positivo: "))
if n<0:
    print("El número debe ser positivo")
else:
    resultado=factorial(n)
    print(f"El factorial de {n} es: {resultado}")