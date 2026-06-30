import maskpass
import bcrypt
import re
from negocio.validar_rut import rut_valido
from negocio.validar_datos_usuario import rut_en_uso

def solicitar_datos_libro():
    titulo_libro = isbn = editorial = paginas = categoria = ''
    
    titulo_libro = solicitar_dato('Título: ')
    isbn = solicitar_dato('ISBN: ')
    editorial = solicitar_dato('Editorial: ')
    paginas = solicitar_dato('Cantidad de Páginas: ')
    categoria = solicitar_dato('Categoría: ')
    return titulo_libro,isbn,editorial,paginas,categoria

def solicitar_datos_usuario():
    nombre_usuario = correo_usuario = telefono_usuario = rut_usuario = contrasena_usuario = ''
    
    nombre_usuario = solicitar_dato('Nombre Usuario: ')
    correo_usuario = validar_email()
    telefono_usuario = solicitar_dato('Teléfono: ')
    rut_usuario = ingreso_rut_valido()
    
    while contrasena_usuario == '':
        contrasena_usuario = maskpass.askpass(prompt="Contraseña: ", mask="*").strip()
        contrasena_segura = validar_contrasena_segura(contrasena_usuario)
        if contrasena_segura == False:
            contrasena_usuario = ''
        else:
            password = contrasena_segura.encode('utf-8')
            contrasena_encriptada = bcrypt.hashpw(password, bcrypt.gensalt())

    return nombre_usuario,correo_usuario,telefono_usuario,rut_usuario,contrasena_encriptada

def solicitar_dato(mensaje_input):
    dato_ingresado = ''
    while dato_ingresado == '':
        dato_ingresado = input(f'{mensaje_input}').strip()
        return dato_ingresado
    
def solicitar_contrasena(mensaje_input):
    contrasena = ''
    while contrasena == '':
        contrasena = maskpass.askpass(prompt=f"{mensaje_input}", mask="*").strip()
        return contrasena

def validar_email():
    correo = ''
    while correo == '':
        correo = input('Correo Electrónico: ').strip()
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,5}+$'
        
        if re.match(patron, correo):
            usuario = 
            return correo
        else:
            print('Correo inválido, ingrese nuevamente.')
            correo = ''

def ingreso_rut_valido():
    rut = ''
    while rut == '':
        rut = input('Correo Electrónico: ').strip()
        if rut_valido(rut) == False:
            print('RUT Inválido, ingrese nuevamente.')
            rut = ''
        else:
            if rut_en_uso(rut):
                print('RUT ingresado ya está en uso, intente nuevamente.')
                rut = ''
            else:
                return rut

def validar_contrasena_segura(password):
    # Diccionario con los patrones y sus respectivos mensajes de error
    reglas = {
        r'.{8,}': "La contraseña debe tener al menos 8 caracteres.",
        r'[A-Z]': "La contraseña debe tener al menos una letra mayúscula.",
        r'[a-z]': "La contraseña debe tener al menos una letra minúscula.",
        r'\d': "La contraseña debe tener al menos un número.",
        r'[!@#$%^&*(),.?":{}|<>]': "La contraseña debe tener al menos un carácter especial."
    }
    
    errores = []
    
    # Comprobamos cada regla
    for patron, mensaje in reglas.items():
        if not re.search(patron, password):
            errores.append(mensaje)
            
    # Si la lista de errores está vacía, la contraseña es segura
    if not errores:
        return password
    else:
        print(f'Errores en su contraseña: {errores}')
        return False

def nuevos_datos_libro():
    pass

def nuevos_datos_usuario():
    pass