#Ejercicio 3 Parcial 2
T_Min={9, 5, 2, 7, 6, 1}
T_Max={12, 14, 11, 10, 15, 9}

#A
if 9 in T_Max and 9 in T_Min:
    print("La temperatura 9° sí está en ambos sets")
else:
    print("La temperatura 9°C no está en ambos sets")

#B
if 6 in T_Min or 6 in T_Max:
    print("La temperatura 6°C está mínimo en un set")
else:
    print("La temperatura 6°C no está en ningun set")
if 17 in T_Min or 17 in T_Max:
    print("La temperatura 17°C está mínimo en un set")
else:
    print("La temperatura 17°C no está en ningun set")

#C
T_Min={temp**4 for temp in T_Min}
T_Max={temp**4 for temp in T_Max}
print("Las temperaturas mínimas elevadas a 4 son: ", T_Min)
print("Las temperaturas máximas elevadas a 4 son: ", T_Max)

#D
union_temperaturas = T_Min.union(T_Max)
print("La unión de los sets es: ", union_temperaturas)