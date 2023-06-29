# EJERCICIO 3

def bisiesto(año):
    if año%4!=0:
        return False
    elif año%400!=0:
        return False
    elif año%100!=0:
        return True
    else:
        return True
def main():
    año=int(input("Ingresar año: "))
    if bisiesto(año):
        print("El año ",año, "es un año bisiesto.")
    else:
        print("El año ",año, "no es bisiesto.")
if __name__ == "__main__":
    main()