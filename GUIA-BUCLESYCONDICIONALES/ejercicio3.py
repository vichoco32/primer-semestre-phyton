#Ejercicio 3
tarifa_diurna = 12000
tarifa_nocturna = 16000
incremento_domingo_diurno = 2000
incremento_domingo_nocturno = 3000

empleado1 = {
    "Lunes": tarifa_nocturna * 10,
    "Martes": tarifa_nocturna * 10,
    "Miércoles": tarifa_nocturna * 10,
    "Jueves": tarifa_diurna * 10,
    "Viernes": tarifa_diurna * 10,
}

empleado2 = {
    "Martes": tarifa_nocturna * 10,
    "Miércoles": tarifa_nocturna * 10,
    "Jueves": tarifa_nocturna * 10,
    "Domingo": tarifa_diurna * 10 + incremento_domingo_diurno,
}

empleado3 = {
    "Miércoles": tarifa_diurna * 10,
    "Jueves": tarifa_diurna * 10,
    "Viernes": tarifa_diurna * 10,
    "Sábado": tarifa_nocturna * 10,
    "Domingo": tarifa_nocturna * 10 + incremento_domingo_nocturno,
}

for empleado, horarios in zip(["Empleado 1", "Empleado 2", "Empleado 3"], [empleado1, empleado2, empleado3]):
    total_semanal = sum(horarios.values())
    print(f"{empleado}:")
    for dia, pago_diario in horarios.items():
        print(f"{dia}: Pago diario: {pago_diario} CLP")
    print(f"Total Semanal: {total_semanal} CLP\n")