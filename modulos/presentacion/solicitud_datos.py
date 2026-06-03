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

def solicitar_dato(mensaje_input):
    tipo_dato = ''
    while tipo_dato == '':
        tipo_dato = input(f'{mensaje_input}').strip()
        return tipo_dato

def nuevos_datos_libro():
    pass