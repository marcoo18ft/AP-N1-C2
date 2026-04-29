# Dentro del lenguaje, tenemos la opción de crear nuestras PROPIAS funciones
# para eso usamos la palabra reservada DEF

# DEF es acrínimo de DEFINIR, porque estamos definiendo una FUNCIÓN
# Luego de DEF ponemos el NOMBRE de la función
# Luego del NOMBRE de la FUNCIÓN ponemos sus ARGUMENTOS
# Los ARGUMENTOS serán los insumos que usará la función para hacer su trabajo

def suma(a,b):
    # Este será el contenido de la función
    resultado = a + b
    # Usamos la palabra reservada RETURN para RETORNAR o DEVOLVER el resultado de nuestra FUNCIÓN
    return resultado

def resta(a,b):
    resultado = a - b
    return resultado

def multiplicacion(a,b):
    resultado = a * b
    return resultado

def division(a,b):
    if b != 0:
        resultado = a / b
        return resultado
    else:
        print('No es posible dividir por 0!')

def pedir_datos():
    str_numero_1 = input('Ingrese primer número: ')
    str_numero_2 = input('Inrese segundo número: ')

    # Cuando utilizamos (llamamos) a una función que tiene un RETURN, necesitamos recibir ese valor en una variable
    num_1 = convertir_float(str_numero_1)
    num_2 = convertir_float(str_numero_2)

    if num_1 and num_2 != False:
        return(num_1,num_2)
    else:
        return(False,False)

def convertir_float(valor):
    try:
        return float(valor)
    except (ValueError, TypeError):
        return False


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

    opciones_validas = ['0','1','2','3','4']

    if opcion in(opciones_validas):
        if opcion == '0':
            ciclo = False
            print('Gracias por usar mi calculadora!')
            print('Saliendo...')
        else:
            a,b = pedir_datos()
            operacion = ''

            if a and b != False:
                if opcion == '1':
                    operacion = '+'
                    valor = suma(a,b)
                elif opcion == '2':
                    operacion = '-'
                    valor = resta(a,b)
                elif opcion == '3':
                    operacion = 'x'
                    valor = multiplicacion(a,b)
                elif opcion == '4':
                    operacion = '/'
                    valor = division(a,b)
                print(f'{a} {operacion} {b} = {valor}')
            else:
                print('Valor NO corresponde a un número!')
    else:
        print('Opción NO válida.')