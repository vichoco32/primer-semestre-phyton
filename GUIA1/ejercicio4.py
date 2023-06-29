#EJERCICIO 4

nombre1 = input("Ingrese su nombre")
nombre2 = input("Ingrese el nombre de otra persona")

if nombre1[0] == nombre2[0]:
    print("Ambos nombres comienzan con la misma letra")
elif nombre1[-1] == nombre2[-1]:
    print("Ambos nombres terminan con la misma letra")
else:
    print("Ambos nombres difieren tanto en la letra inicial como en la final")