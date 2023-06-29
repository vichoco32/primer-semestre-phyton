#Ejercicio 8

def obtener_estacion(mes):
    if mes in (1, 2, 12):
        return "Verano"
    elif mes in (3, 4, 5):
        return "Otoño"
    elif mes in (6, 7, 8):
        return"Invierno"
    elif mes in (9, 10, 11):
        return "Primavera"
    else:
        return "Mes inválido"

mes_ingresado = int(input("Ingresa un número de mes (1-12): "))

estacion = obtener_estacion(mes_ingresado)
print("La estación correspondiente a ese mes es:", estacion)