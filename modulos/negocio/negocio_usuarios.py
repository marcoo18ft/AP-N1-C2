from presentacion.solicitud_datos import solicitar_datos_usuario
from datos import listado_usuarios
from datos.data_usuarios import escribir_data_usuarios
from prettytable import PrettyTable

def procesar_usuario():
    nombre, correo, telefono, rut, contrasena = solicitar_datos_usuario()
    nuevo_usuario = {
        'id': len(listado_usuarios) + 1,
        'nombre':nombre.title(),
        'correo':correo,
        'telefono':telefono,
        'rut':rut,
        'contrasena':contrasena,
        'habilitado':True
    }
    listado_usuarios.append(nuevo_usuario)
    return listado_usuarios

def crear_tabla_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ['N°','Nombre','Email','Celular','RUT']

    for usuario in listado_usuarios:
        tabla_usuarios.add_row([usuario['id'],usuario['nombre'],usuario['correo'],usuario['telefono'],usuario['rut']])
    
    return tabla_usuarios

def buscar_usuario_nombre(nombre):
    for usuario in listado_usuarios:
        if usuario['nombre'].lower() == nombre.lower():
            return usuario

def buscar_usuario_correo(correo):
    for usuario in listado_usuarios:
        if usuario['correo'].lower() == correo.lower():
            return usuario
        
def bloquear_usuario(correo_usuario):
    for usuario in listado_usuarios:
        if usuario['correo'].lower() == correo_usuario.lower():
            usuario.update({'habilitado':False})
            escribir_data_usuarios(listado_usuarios)
            return True