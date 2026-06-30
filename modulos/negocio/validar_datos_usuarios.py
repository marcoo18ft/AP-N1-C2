from datos import listado_usuarios

def rut_en_uso(rut_ingresado):
    for usuario in listado_usuarios:
        if usuario['rut'] == rut_ingresado:
            return True