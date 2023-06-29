#Ejercicio n°1

#A
diccionario = {
    'Los Ríos': {
        'superficie':18429,
        'habitantes': 404432
},
'Magallanes': {
        'superficie': 1382291,
        'habitantes': 166533
    }
}

for region, datos in diccionario.items():
    superficie = datos['superficie']
    habitantes = datos['habitantes']
    print(f"{region}: {superficie} kilómetros de superficie, {habitantes} habitantes")

#B

for region, datos in diccionario.items():
    superficie = datos['superficie']
    habitantes = datos['habitantes']
    densidad = round(habitantes / superficie, 1)
    datos['Densidad'] = densidad

#C

capital_rios = region["Los Ríos"]["Capital"]
print("La capital de Los Ríos es:", capital_rios)


capital_magallanes = region["Magallanes"]["Capital"]
print("La capital de Magallanes es:", capital_magallanes)

