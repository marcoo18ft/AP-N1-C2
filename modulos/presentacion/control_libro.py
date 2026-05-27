from datos import listado_libros
from prettytable import PrettyTable
from datos import agregar_libro

def agregar_libro():
    titulo = '\nAgregar Libro'
    print(titulo)
    print('=' * len(titulo))
    listar_libros()

    print('\nIngrese los datos del libro:')
    titulo_libro,isbn,editorial,paginas,categoria = solicitar_datos_libro()
    agregar_libro(titulo_libro, isbn, editorial, paginas, categoria)

def listar_libros():
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['Título','ISBN','Editorial','Páginas','Categoría']

    titulo = '\nListado de Libros'
    print(titulo)
    print('=' * len(titulo))
    for libro in listado_libros:
        tabla_libros.add_row([libro['titulo_libro'],libro['isbn'],libro['editorial'],libro['paginas'],libro['categoria']])
    print(tabla_libros)

def modificar_libro():
    titulo = '\nModificar Libro'
    print(titulo)
    print('=' * len(titulo))

def eliminar_libro():
    titulo = '\nEliminar Libro'
    print(titulo)
    print('=' * len(titulo))

def solicitar_datos_libro():
    titulo_libro = isbn = editorial = paginas = categoria = ''
    while titulo_libro == '':
        titulo_libro = input('Título: ').strip()
    while isbn == '':
        isbn = input('ISBN: ').strip()
    while editorial == '':
        editorial = input('Editorial: ').strip()
    while paginas == '':
        paginas = input('Cantidad de Páginas: ').strip()
    while categoria == '':
        categoria = input('Categoría: ').strip()
    return titulo_libro,isbn,editorial,paginas,categoria