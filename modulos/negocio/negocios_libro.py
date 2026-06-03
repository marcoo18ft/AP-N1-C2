from presentacion.datos_libro import solicitar_datos_libro,solicitar_dato
from datos import listado_libros
import os

def procesar_libro():
    titulo_libro, isbn, editorial, paginas, categoria = solicitar_datos_libro()
    nuevo_libro = {
        'id': len(listado_libros) + 1,
        'titulo_libro':titulo_libro.title(),
        'isbn':isbn,
        'editorial':editorial,
        'paginas':paginas,
        'categoria':categoria.title()
    }
    listado_libros.append(nuevo_libro)

    ruta_archivo = os.path.join('modulos/datos','info_libros.py')
    ruta_absoluta = os.path.abspath(ruta_archivo)
    ruta_final = os.path.realpath(ruta_absoluta)
    archivo_libros = open(ruta_final,'+w', encoding="utf-8")
    archivo_libros.write(f'listado_libros = {listado_libros}')
    archivo_libros.close()