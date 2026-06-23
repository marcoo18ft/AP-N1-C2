from datos import datos_menu,opciones_validas_menu,datos_sub_menu,mensaje_volver,opciones_validas_sub_menu,opcion_incorrecta,titulo_app
from datos import numero_version
from presentacion.control_libro import agregar_libro,listar_libros,modificar_libro,eliminar_libro
from presentacion.control_usuario import agregar_usuario,listar_usuarios,modificar_usuario,eliminar_usuario,login_usuario
from presentacion.solicitud_datos import solicitar_dato
from negocio import bloquear_usuario
import sys

def titulo_principal():
    print(f'\n{titulo_app} v{numero_version}')
    print(f'{'=' * len(titulo_app)}=={'=' * len(numero_version)}')
    print()

def acceso():
    correo_usuario = ''
    while correo_usuario == '':
        titulo_principal()
        titulo = 'Login Sistema'
        print()
        print(titulo)
        print('=' * len(titulo))
        cantidad_intentos = 0    
        correo_usuario = solicitar_dato('Correo Usuario: ')

        while cantidad_intentos < 3:
            cantidad_intentos+=1
            respuesta = login_usuario(correo_usuario)
            if respuesta == 'pass correcta':
                menu_principal()
            elif respuesta == 'pass incorrecta':
                print('Usuario NO autorizado.')
                if cantidad_intentos==3:
                    bloqueo = bloquear_usuario(correo_usuario)
                    if bloqueo:
                        print('Usuario Bloqueado!')
            elif respuesta == 'no encontrado':
                correo_usuario = ''
                break

def menu_principal():
    titulo_principal()

    while True:
        titulo = 'Menú Principal'
        print()
        print(titulo)
        print('=' * len(titulo))
        for clave, valor in datos_menu.items():
            print(f'[{clave}] {valor}')
        opcion_usuario = seleccionar_opcion(datos_menu)

        if opcion_usuario == '1':
            # Gestión Libros
            while True:
                opcion_sub_menu = sub_menu('Libro')
                if opcion_sub_menu == '1':
                    agregar_libro()
                elif opcion_sub_menu == '2':
                    listar_libros()
                elif opcion_sub_menu == '3':
                    modificar_libro()
                elif opcion_sub_menu == '4':
                    eliminar_libro()
                elif opcion_sub_menu == '0':
                    print(mensaje_volver)
                    break
                else:
                    print(opcion_incorrecta)

        elif opcion_usuario == '2':
            # Gestión Usuarios
            while True:
                opcion_sub_menu = sub_menu('Usuario')
                if opcion_sub_menu == '1':
                    agregar_usuario()
                elif opcion_sub_menu == '2':
                    listar_usuarios()
                elif opcion_sub_menu == '3':
                    modificar_usuario()
                elif opcion_sub_menu == '4':
                    eliminar_usuario()
                elif opcion_sub_menu == '0':
                    print(mensaje_volver)
                    break
                else:
                    print(opcion_incorrecta)
        elif opcion_usuario == '3':
            # Gestión Lectores
            while True:
                opcion_sub_menu = sub_menu('Lector')
                if opcion_sub_menu == '1':
                    pass
                elif opcion_sub_menu == '2':
                    pass
                elif opcion_sub_menu == '3':
                    pass
                elif opcion_sub_menu == '4':
                    pass
                elif opcion_sub_menu == '0':
                    print(mensaje_volver)
                    break
                else:
                    print(opcion_incorrecta)
        elif opcion_usuario == '4':
            # Gestión Préstamos
            while True:
                opcion_sub_menu = sub_menu('Préstamo')
                if opcion_sub_menu == '1':
                    pass
                elif opcion_sub_menu == '2':
                    pass
                elif opcion_sub_menu == '3':
                    pass
                elif opcion_sub_menu == '4':
                    pass
                elif opcion_sub_menu == '0':
                    print(mensaje_volver)
                    break
                else:
                    print(opcion_incorrecta)
        elif opcion_usuario == '5':
            # Gestión Sistema
            while True:
                opcion_sub_menu = sub_menu('Usuario')
                if opcion_sub_menu == '1':
                    pass
                elif opcion_sub_menu == '2':
                    pass
                elif opcion_sub_menu == '3':
                    pass
                elif opcion_sub_menu == '4':
                    pass
                elif opcion_sub_menu == '0':
                    print(mensaje_volver)
                    break
                else:
                    print(opcion_incorrecta)
        elif opcion_usuario == '6':
            # Sistema Alerta
            while True:
                opcion_sub_menu = sub_menu('Alerta')
                if opcion_sub_menu == '1':
                    pass
                elif opcion_sub_menu == '2':
                    pass
                elif opcion_sub_menu == '3':
                    pass
                elif opcion_sub_menu == '4':
                    pass
                elif opcion_sub_menu == '0':
                    print(mensaje_volver)
                    break
                else:
                    print(opcion_incorrecta)
        elif opcion_usuario == '0':
            print('Saliendo, gracias por gestionar su biblioteca')
            sys.exit(0)
        else:
            print(opcion_incorrecta)

def seleccionar_opcion(menu):
    while True:
        opcion = input(f'Seleccione su opción [0-{len(menu) - 1}]: ')
        if len(menu) <= 5:
            opciones = opciones_validas_sub_menu
        else:
            opciones = opciones_validas_menu
        if opcion in opciones:
            return opcion

def sub_menu(tipo_dato):
    titulo = f'Submenú {tipo_dato}'
    print()
    print(titulo)
    print('=' * len(titulo))
    for clave, valor in datos_sub_menu.items():
        if clave != '0':
            print(f'[{clave}] {valor} {tipo_dato}')
        else:
            print(f'[{clave}] {valor}')
    opcion_usuario = seleccionar_opcion(datos_sub_menu)
    return opcion_usuario