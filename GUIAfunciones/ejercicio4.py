# EJERCICIO 4

def total_vuelto(vuelto):
    num_billetes=[20000, 10000, 5000, 2000, 1000]
    num_monedas=[500, 100, 50, 10]
    des_billetes = {}
    des_monedas = {}
    for num in num_billetes: 
        cantidad = vuelto // num
        if cantidad > 0:
            des_billetes[num] = cantidad
            vuelto -= cantidad * num
    for num in num_monedas:
        cantidad = vuelto // num
        if cantidad > 0:
            des_monedas[num] = cantidad
            vuelto -= cantidad * num
    return des_billetes, des_monedas
compra = int(input("Ingrese el monto total de la compra: "))
pago=int(input("Ingrese el monto con el cual pagara: "))
if pago<compra:
    print("El monto de pago es insuficiente, por favor realice un nuevo pago o cancele la compra")
else:
    vuelto=pago-compra
    des_billetes, des_monedas = total_vuelto(vuelto)
    print("Vuelto: $", vuelto)
    print("Desglosamiento del vuelto en billetes:")
    for num, cantidad in des_billetes.items():
        print(cantidad, "billete(s) de $", num)
    print("Desglosamiento del vuelto en monedas:")
    for num, cantidad in des_monedas.items():
        print(cantidad, "moneda(s) de $", num)