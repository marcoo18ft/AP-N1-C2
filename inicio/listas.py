# Las LISTAS son colecciones ordenadas y mutables,
# es decir, son modificables una vez creadas.
# Pueden almacenar elementos de diferentes tipos al mismo tiempo,
# ideales para almacenar una colección de datos que necesita ser modificada o accedida por índices.
# Almacena los datos en 2 espacios de memoria, el índice y el dato mismo.

print("\nTrabajando con LISTAS.\n======================")
lista = ["Armando Casas", True, 1.73]
print(lista)

print(type(lista))

print(lista[0])
print(lista[1])
print(lista[2])

print(type(lista[0]))
print(type(lista[1]))
print(type(lista[2]))

str_nombre = input('Ingrese su nombre: ')
lista[0] = str_nombre # Cambio válido, acceso al elemento por ÍNDICE
print(lista[0])
print(f"{lista}\n")

# Reemplace el segundo elemento de la lista por su edad
# La edad debe ser un número entero

int_edad = int(input('Ingrese su edad: '))
lista[1] = int_edad
print(lista[1])
print(lista)

nuevo_elemento = 25
lista.append(nuevo_elemento)
print(lista)