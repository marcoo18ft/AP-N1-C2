from datos import listado_libros

def incoporar_libro(titulo_libro,isbn,editorial,paginas,categoria):
    nuevo_libro = {
        'titulo_libro':titulo_libro,
        'isbn':isbn,
        'editorial':editorial,
        'paginas':paginas,
        'categoria':categoria
    }
    listado_libros.append(nuevo_libro)
    for libro in listado_libros:
        print(libro)