# Las TUPLAS son colecciones ordenadas e inmutables.
# Se utilizan para almacenar una secuencia de valores que no deben cambiar a lo largo de la ejecución programa.
# Son más rápidas que los diccionarios, por NO usar un par de valores para cada dato
# y protegen los datos de modificaciones accidentales.
# Su uso más general es para manejar datos de sólo lectura.

print("Trabajando con TUPLAS.\n======================")
tupla = ("Armando Casas", True, 1.73)
print(type(tupla))
print(tupla)
print(f"{tupla[0]}\n")

# tupla[1] = "Nuevo Valor" # Cambio NO válid