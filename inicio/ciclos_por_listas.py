# Ciclo FOR (por) para iterar LISTAS
# Recorro cada uno de los elementos de la lista

lista_bandas = ['P.O.D.','Skillet','Demon Hunter']
nombre_personal = 'Erick Bailey'

# Usamos el método RANGE para crear un rango de números
# Si a RANGE le pasamos 1 argumento, creará una lista de números de la cantidad entregada
# La lista inicia en el índice 0
lista_numeros = range(5)

# SI a RANGE le pasamos 2 argumentos, le indicamos desde donde inicia y el elemento final -1
lista_numeros_2 = range(10,20)

# Si a RANGE le pasamos 3 argumentos, le indicamos desde donde inicia, el elemento final -1 y el avance entre elementos
lista_numeros_3 = range(5,26,5)

banda_encontrada = False
buscar_banda = input('Qué banda busca?')

for banda in lista_bandas:
    banda_mayusculas = banda.upper()
    if banda_mayusculas == buscar_banda.upper():
        banda_encontrada = True
if banda_encontrada == True:
    print('Banda Encontrada!')
else:
    print('Banda NO encontrada!')

print()
for letra in nombre_personal:
    print(letra)

print()
for numero in lista_numeros:
    resultado = numero * 5
    print(resultado)

print()
for elemento in lista_numeros_2:
    print(elemento)

print()
for elemento in lista_numeros_3:
    print(elemento)