# Los CONJUNTOS o sets son colecciones desordenadas, NO indexadas de elementos únicos, NO almacena datos duplicados.
# Son ideales para realizar operaciones de conjunto como uniones, intersecciones y diferencias,
# así como para eliminar elementos duplicados de una colección.
# NO se puede acceder a los elementos por un ÍNDICE ni por una CLAVE.

print("Trabajando con CONJUNTOS.\n==========================")
conjunto = {"Armando Casas", True, 1.73}
# conjunto[1] = "Nuevo Valor" # Cambio NO válido, no se puede acceder a los elementos por ÍNDICE
# print(sorted(conjunto)) # Si se tiene distintos tipos de datos, no se puede aplicar la función SORTED para ordenar
print(type(conjunto))
print(conjunto)

conjunto.add(str_nombre) # Se agrega un nuevo valor al conjunto.
conjunto.add(str_nombre) # El conjunto ya tiene este valor, NO se agrega nuevamente.
print(f"{conjunto}\n")