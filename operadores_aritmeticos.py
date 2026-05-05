# OPERADORES ARITMÉTICOS

# Operador SUMA +
# Permite SUMAR 2 valores numéricos
suma = 25 + 45
print(suma)

# Permite CONCATENAR (unir) 2 cadenas de texto
concatenacion = 'Hola' + ' ' + 'Queridos Estudiantes!'
print(concatenacion)

# Operador RESTA -
# Permite RESTAR 2 valores numéricos
resta = 25 - 45
print(resta)

# Operador MULTIPLICACIÓN *
# Permite MULTIPLICAR 2 valores numéricos
mutiplicacion = 25 * 45
print(mutiplicacion)

# Permite MULTIPLICAR una cadena de texto por un valor numérico
multiplicacion_2 = 'Hola' * 3
print(multiplicacion_2)

# Permite elevar un numero a una potencia
potencia = 2 ** 3
print(potencia)

# Operador DIVISIÓN /
# Permite DIVIDIR 2 valores numéricos
# Si el denominador es 0, la operación arrojará un error
# ZeroDivisionError
def division(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print('No se puede DIVIDIR por 0')
    except Exception as error:
        print(f'Error en la operación: {error}')

division(25,0)

# Permite obtener el resto de una división
resto = 9.5 % 5.3
print(resto)