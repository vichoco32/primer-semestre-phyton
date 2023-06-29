#EJERCICIO 5

lab1 = float(input("Ingrese la nota del laboratorio 1: "))
lab2 = float(input("Ingrese la nota del laboratorio 2: "))
lab3 = float(input("Ingrese la nota del laboratorio 3: "))

prom = lab1 * 0.3 + lab2 * 0.4 + lab3 * 0.3

if prom < 4.0:
    print("El estudiante reprobo la asignatura")
elif prom >= 4.0 and prom < 6.0:
    print("El estudiante aprobó la asignatura")
else:
    print("El estudiante aprobó con distinción")