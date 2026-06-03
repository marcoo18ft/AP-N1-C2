from datos import listado_libros
from prettytable import PrettyTable
from negocio import procesar_libro

def agregar_libro():
    titulo = '\nAgregar Libro'
    print(titulo)
    print('=' * len(titulo))
    listar_libros()

    print('\nIngrese los datos del libro:')
    procesar_libro()


def listar_libros():
    tabla_libros = PrettyTable()
    tabla_libros.field_names = ['N°','Título','ISBN','Editorial','Páginas','Categoría']

    titulo = '\nListado de Libros'
    print(titulo)
    print('=' * len(titulo))
    for libro in listado_libros:
        tabla_libros.add_row([libro['id'],libro['titulo_libro'],libro['isbn'],libro['editorial'],libro['paginas'],libro['categoria']])
    print(tabla_libros)

def modificar_libro():
    titulo = '\nModificar Libro'
    print(titulo)
    print('=' * len(titulo))

def eliminar_libro():
    titulo = '\nEliminar Libro'
    print(titulo)
    print('=' * len(titulo))