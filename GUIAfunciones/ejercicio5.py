# EJERCICIO 5

def obtencion_num():
    numeros=[]
    while True:
        numero=int(input("Ingresar uno o más números positivos y escribir -1 para terminar la lista: "))
        if numero==-1:
            break
        if numero<0:
            print("Solo se deben ingresar números positivos")
            continue
        numeros.append(numero)
    return numeros
def calculo(numeros):
    sum_total=sum(numeros)
    suma_numeros_pares=sum(num for num in numeros if num%2==0)
    suma_numeros_impares=sum(num for num in numeros if num%2!= 0)
    prom=sum_total/len(numeros)
    num_mayor=max(numeros)
    print("La suma de pares es:", suma_numeros_pares)
    print("La suma de impares es:", suma_numeros_impares)
    print("La suma total es:", sum_total)
    print(f"El promedio es: {prom:.2f}",)
    if num_mayor>prom:
        print("El número mayor ingresado fue:", num_mayor)
        print("El número es mayor que el promedio y es", num_mayor)
    elif num_mayor<prom:
        print("El número mayor ingresado fue:", num_mayor)
        print("El número es menor que el promedio y es", num_mayor)
    else:
        print("El número mayor ingresado fue:", num_mayor)
        print("El número es igual al promedio y es", num_mayor)
numeros=obtencion_num()
calculo(numeros)