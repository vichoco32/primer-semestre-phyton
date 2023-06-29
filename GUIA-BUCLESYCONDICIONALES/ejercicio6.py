#Ejercicio 6
import time 
hora = time.localtime()
dia = hora.tm_mday
segundos = 0
for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
            segundos += 1
            time.sleep(1)