# Ciclo FOR (por) para iterar DICCIONARIOS
# Recorro cada uno de los elementos del diccionario

datos_personales = {
    'nombre':'Armando Casas',
    'edad':35,
    'profesión':'constructor'
}

for clave in datos_personales:
    print(clave)

for elemento in datos_personales.items():
    print(elemento)

for elemento in datos_personales.items():
    clave = elemento[0]
    valor = elemento[1]
    print(f'clave: {clave} valor: {valor}')