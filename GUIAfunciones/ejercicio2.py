# EJERCICIO 2

def names():
    names=[]
    while True:
        name=input("Ingresar un nombre (o presione Enter para finalizar): ")
        if name== "":
            break
        names.append(name)
    return names
def numero_letras_contadas(names):
    num_total_letras=0
    for name in names:
        num_total_letras+=len(name)
    return num_total_letras
def resultados(names, num_total_letras):
    print("Nombres ingresados:")
    for name in names:
        print(name)
    print("Total de letras contadas:", num_total_letras)
lista_nombres=names()
num_total_letras=numero_letras_contadas(lista_nombres)
resultados(lista_nombres, num_total_letras)