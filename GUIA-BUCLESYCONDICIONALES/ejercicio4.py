#Ejercicio 4
n = int(input("Ingresar valor de n: "))
sum_impares = 1  
cubo = 1  
print("1^3 =", cubo)
for i in range(2, n + 1):
    sum_impares += (i - 1) * 2  
    cubo = cubo + sum_impares  
    print(i, "^3 =", end=" ")
    for j in range(i):
        print(sum_impares, end="")
        if j != i - 1:
            print(" + ", end="")
        sum_impares += 2
    print(" =", cubo)