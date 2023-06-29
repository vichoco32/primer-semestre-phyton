#Reto en clase n°3

ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
indice_calidad_aire = [134,99,245,50]

indice_minimo = min(indice_calidad_aire)
ciudad_minima = ciudades[indice_calidad_aire.index(indice_minimo)]

indice_maximo = max(indice_calidad_aire)
ciudad_maxima = ciudades[indice_calidad_aire.index(indice_maximo)]

print(f"La ciudad con el índice de calidad del aire mas bajo es {ciudad_minima}")
print(f"La ciudad con el índice de calidad del aire mas alto es {ciudad_maxima}")

if indice_maximo <= 50:
    print("El índice de calidad del aire está en la categoría Buena")
elif indice_maximo <= 100:
    print("El índice de calidad del aire está en la categoría Moderada")
elif indice_maximo <= 150:
    print("El índice de calidad del aire está en la categoría Dañina a la salud para grupos sensibles")
elif indice_maximo <= 200:
    print("El índice de calidad del aire está en la categoría Dañina a la salud")
elif indice_maximo <= 300:
    print("El índice de calidad del aire está en la categoría Peligrosa")