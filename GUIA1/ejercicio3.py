#EJERCICIO 3

a = float(input("Ingrese el lado a del triángulo"))
b = float(input("Ingrese el lado b del triángulo"))
c = float(input("Ingrese el lado c del triángulo"))

if a == b == c:
    print("El triángulo es equilatero")
elif a == b or b == c or a ==c:
    print("El triángulo es iscoleces")
else:
    print("El triángulo es escaleno")

sp = (a + b + b) / 2
area = ((sp * (sp - a)) * (sp - b) * (sp - c) )* 0.5

print("El área del triángulo es de:", area)