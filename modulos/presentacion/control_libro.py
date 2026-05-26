
from datos import listado_libros





def agregar_libro():
  titulo = "Agregar libro"
  print(titulo)
  print(f'{"=" * len(titulo)}')
titulo_libro, isbn, editorial, paginas, categorias = solicitar_datos_libro()
def listado_libros():
    titulo = "Listado de Libros"
    print(titulo)
    print(f'{"=" * len(titulo)}')
    print(listado_libros)
listado_libros()
def modificar_libro():
    titulo = "Modificar Libro"
    print(titulo)
    print(f'{"=" * len(titulo)}')

def eliminar_libro():
    titulo = "Eliminar Libro"
    print(titulo)
    print(f'{"=" * len(titulo )}')


def solicitar_datos_libro():
    titulo_libro = input("Titulo :")
    isbn = input("ISBN :")
    editorial = input ("Editorial :")
    paginas = input("Número de páginas :")
    categorias = input("Categoria: ")
    return titulo_libro, isbn, editorial, paginas, categorias