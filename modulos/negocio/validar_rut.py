def rut_valido(rut):
    # Limpiar el rut
    rut_completo = rut.replace('.','').replace('-','').lower()

    # Validar largo del rut
    if len(rut_completo) < 2:
        return False
    
    # Separar el rut del dígito verificador
    numero_rut = rut_completo[:-1]
    digito_verificador_ingresado = rut_completo[-1]
    # Invertimos el rut
    rut_invertido = ''.join(reversed(numero_rut))

    # Aplicar módulo 11
    if not numero_rut.isdigit():
        return False
    
    serie_modulo_once = [2,3,4,5,6,7]
    suma = 0
    multiplicador = 0

    for digito in rut_invertido:
        suma += int(digito) * serie_modulo_once[multiplicador % 6]
        multiplicador+=1
    
    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 11:
        digito_verificador = 0
    elif digito_verificador == 10:
        digito_verificador = 'k'
    
    if digito_verificador_ingresado == str(digito_verificador):
        return True
    else:
        return False

# respuesta = funcion_validar_rut('12.345.678-9')
# print(respuesta)

# respuesta = funcion_validar_rut('12.345.678-5')
# print(respuesta)