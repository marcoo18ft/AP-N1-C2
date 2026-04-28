# Dentro del lenguaje, tenemos la opción de crear nuestras PROPIAS funciones
# para eso usamos la palabra reservada DEF

def suma(a,b):
    # Este será el contenido de la función
    resultado = a + b
    print(f'{a} + {b} = {resultado}')

def resta(a,b):
    resultado = a - b
    print(f'{a} - {b} = {resultado}')

def multiplicacion(a,b):
    resultado = a * b
    print(f'{a} x {b} = {resultado}')

def division(a,b):
    if b != 0:
        resultado = a / b
        print(f'{a} / {b} = {resultado}')
    else:
        print('No es posible dividir por 0!')

def pedir_datos():
    str_numero_1 = input('Ingrese primer número: ')
    str_numero_2 = input('Inrese segundo número: ')

    if str_numero_1.isdigit() and str_numero_2.isdigit():
        num_1 = float(str_numero_1)
        num_2 = float(str_numero_2)
    else:
        print('Valor NO corresponde a un número')
    return(num_1,num_2)


# str_numero_1 = input('Ingrese primer número: ')
# str_numero_2 = input('Inrese segundo número: ')

# if str_numero_1.isdigit() and str_numero_2.isdigit():
#     num_1 = float(str_numero_1)
#     num_2 = float(str_numero_2)
# else:
#     print('Valor NO corresponde a un número')

# a,b = pedir_datos()

# suma(a,b)
# resta(a,b)
# multiplicacion(a,b)
# division(a,b)


print('\nBienvenido a Mi primera CALCULADORA')
print('====================================')
ciclo = True

while ciclo == True:
    print('\n[1] Suma')
    print('[2] Resta')
    print('[3] Multiplicación')
    print('[4] División')
    print('[0] Salir')
    opcion = input('\nSeleccione su operación [0-4]: ')

    if opcion == '0':
        ciclo = False
        print('Gracias por usar mi calculadora!')
        print('Saliendo...')
    else:
        a,b = pedir_datos()
        
        if opcion == '1':
            suma(a,b)
        elif opcion == '2':
            resta(a,b)
        elif opcion == '3':
            multiplicacion(a,b)
        elif opcion == '4':
            division(a,b)
        else:
            print('Opción NO válida.')