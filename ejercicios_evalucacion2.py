# Los ejercicios a resolver deben incluirse dentro de un menú
# mediante el cual se ejecutará cada uno de ellos.

# 1.- Escriba una función que al ser llamada imprima el saludo "Buen día!"

# 2.- Escriba una función que solicite al usuario ingresar su nombre
# en una variable nombre_usuario
# y al ser llamada imprima el saludo "Buen día 'nombre_usuario'!"

# 3.- Escribir una función que pida al usuario un número entero menor a 10
# y al ser llamada entregue el factorial de ese número

def saludo ():
    print("Buen dia")

    


def menu_principal():
    while True:
        print()
        print('[1] Ejercicio 1')
        print('[2] Ejercicio 2')
        print('[3] Ejercicio 3')
        print('[0] Salir')

        opcion = input('Ingrese su Opción [0-3]')
        valores_opcion = ['0','1','2','3']

        if opcion in valores_opcion:
            if opcion == '1':
                saludo()

            elif opcion == '2':
                pass
            elif opcion == '3':
                pass
            elif opcion == '0':
                print('Saliendo del sistema...')
                break
        else:
            print('Opción ingresada NO corresponde...')

menu_principal()