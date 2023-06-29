#Reto en clase n°2

estudiante = []

estudiante["nombre"] = input("Ingrese el nombre del estudiante")
estudiante["asignatura"] = input("Ingrese el nombre de la asignatura")
estudiante["Nota del laboratorio 1"] = float(input("Ingrese la nota"))
estudiante["Nota del laboratorio 2"] = float(input("Ingrese la segunda nota"))

promedio = (estudiante["Nota del laboratorio 1"] * 0.3) + (estudiante["Nota del laboratorio 2"] * 0.7)

estudiante["promedio"] = round(promedio,1)

print("Informacion del estudiante")
print(f"Nombre"(estudiante["nombre"]))
print(f"Asignatura"(estudiante["asignatura"]))
print(f"Nota del laboratorio 1"(estudiante["Nota del laboratorio 1"]))
print(f"Nota del laboratorio 2"(estudiante["Nota del laboratorio 2"]))
print("Promedio final",(estudiante["promedio"]))