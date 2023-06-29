#Ejercicio 2 Parcial 2
def piramide_numerica(filas):
    for i in range(1,filas+1):        
        for j in range(filas-i):
            print("",end="")
        for j in range(i,i+1):
            print(j%10,end="")
        for j in range(i-1,0,-1):
            print(j%10,end="")
        print("") 
filas=10
piramide_numerica(filas)