# Los DICCIONARIOS son colecciones no ordenadas de pares KEY : VALUE, usando 2 espacios de memoria.
# Permiten almacenar datos de manera que cada elemento pueda ser recuperado, actualizado o eliminado usando su clave.

print("Trabajando con DICCIONARIOS.\n============================")
diccionario = {
    'nombre_personal' : 'Armando Casas',
    'Está emocionado?' : True,
    'Altura' : 1.73
}
print(type(diccionario))
print(diccionario)
print(diccionario['nombre_personal'])

diccionario['nombre_personal'] = str_nombre # Cambio válido, acceso al elemento por KEY
print(diccionario['nombre_personal'])
print(f"{diccionario}\n")