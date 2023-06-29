# EJERCICIO 1

def ingreso_de_numeros(cantidad):
    num=[]
    for i in range(cantidad):
        numero=int(input(f"Ingresar número {i+1}: "))
        num.append(numero)
    return num
def calculo_sum_total(numeros):
    sum_total=sum(numeros)
    return sum_total
def suma_num_pares(numeros):
    sum_pares=sum(numero for numero in numeros if numero % 2 == 0)
    return sum_pares
def suma_num_impares(numeros):
    sum_impares=sum(numero for numero in numeros if numero % 2 != 0)
    return sum_impares
cantidad_de_num=int(input("¿Cuántos números ingresará?: "))
num_ingresados=ingreso_de_numeros(cantidad_de_num)
sum_total=calculo_sum_total(num_ingresados)
sum_pares=suma_num_pares(num_ingresados)
sum_impares=suma_num_impares(num_ingresados)
print("La suma de todos los números es: ", sum_total)
print("La suma de los números pares es: ", sum_pares)
print("La suma de los números impares es: ", sum_impares) 