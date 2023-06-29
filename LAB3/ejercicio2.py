#Ejercicio 2

a = [21,8,15,3,12] 
b = [10,9,12,15,18]
c = [2,3,8,9,12]
#A
a.extend(b+c)
print(a)

#B
a.insert(14,20)
print(a)

#C
a.sort(reverse=True)
print(a)

#D
a.append([4,5,6])
print(a)
a.pop()

#E
suma_de_a = sum(a)
print(suma_de_a)

#F
print(len(a))
cantidad_de_datos = len(a)
promedio_simple = (suma_de_a / cantidad_de_datos)
print(promedio_simple)