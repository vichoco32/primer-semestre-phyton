#EJERCICIO 6

g1 = {"Marcos", "Gabriela", "Benjamin", "Matias"}
g2 = {"Marcos", "Nicolas", "Diego", "Matias"}

estudiantes_en_comun = g1.intersection(g2)

if len(estudiantes_en_comun) > 0:
    print("Los siguientes estudiantes están en ambos grupos:")
    for estudiante in estudiantes_en_comun:
        print(estudiante)
else:
    print("No hay estudiantes en común entre los dos grupos")