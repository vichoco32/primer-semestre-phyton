#Ejercicio 7

nombres = ["Marcos", "Benjamin", "Matias", "Diego", "Nicolás"]
edades = [30, 42, 29, 34, 48]

trabajadores = list(zip(nombres, edades))

for trabajador in trabajadores:
    print(trabajador)