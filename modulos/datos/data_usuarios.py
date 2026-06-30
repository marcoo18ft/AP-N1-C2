import os

def escribir_data_usuarios(lista_usuarios):
    ruta_archivo = os.path.join('modulos/datos/data_almacenada','info_usuarios.py')
    ruta_absoluta = os.path.abspath(ruta_archivo)
    ruta_final = os.path.realpath(ruta_absoluta)
    archivo_libros = open(ruta_final,'+w', encoding="utf-8")
    archivo_libros.write(f'listado_usuarios = {lista_usuarios}')
    archivo_libros.close()
    print("Usuario agregado correctamente")

    except PermissionError:
    print("No a sido posible grabar los datos : No tiene permisos de escritura .")
    except FileNotFoundError:
    print("No a sido posible grabar los datos : No se encuentra el archivo .")
    except OSError as