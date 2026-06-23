from datos import listado_usuarios,escribir_data_usuarios,usuario_no_encontrado
from prettytable import PrettyTable
from negocio import procesar_usuario,crear_tabla_usuarios,buscar_usuario_nombre,buscar_usuario_correo
from presentacion.solicitud_datos import solicitar_dato,nuevos_datos_usuario,solicitar_contrasena
import bcrypt

def agregar_usuario():
    titulo = '\nAgregar Usuario'
    print(titulo)
    print('=' * len(titulo))
    listar_usuarios()

    print('\nIngrese los datos del usuario:')
    lista_modificada = procesar_usuario()
    escribir_data_usuarios(lista_modificada)

def listar_usuarios():
    tabla_usuarios = PrettyTable()

    titulo = '\nListado de Usuarios'
    print(titulo)
    print('=' * len(titulo))
    tabla_usuarios = crear_tabla_usuarios()
    print(tabla_usuarios)

def login_usuario(correo_usuario):
    usuario = buscar_usuario_correo(correo_usuario)
    if usuario:
        contrasena = solicitar_contrasena('Contraseña Usuario: ')
        contrasena = contrasena.encode('utf-8')
        if bcrypt.checkpw(contrasena, usuario['contrasena']):
            return 'pass correcta'
        else:
            return 'pass incorrecta'
    else:
        print(usuario_no_encontrado)
        return 'no encontrado'

def modificar_usuario():
    titulo = '\nModificar Usuario'
    print(titulo)
    print('=' * len(titulo))
    nombre_usuario = solicitar_dato('Ingrese el nombre del usuario: ')
    usuario = buscar_usuario_nombre(nombre_usuario)
    if usuario:
        print(f'\nDatos del Usuario\n{"=" * 17}')
        print(f'N°: {usuario['id']} \nNombre: {usuario['nombre']} \nEmail: {usuario['correo']} \nRUT: {usuario['rut']}')
        nuevos_datos_usuario()
    else:
        print(usuario_no_encontrado)

def eliminar_usuario():
    titulo = '\nEliminar Usuario'
    print(titulo)
    print('=' * len(titulo))