str_edad = input('Ingrese su Edad: ')
edad = int(str_edad)

# Condicional IF
if edad >= 18:
    # Este set de acciones se ejecuta cuando la respuesta es V
    print('Ud. es mayor de edad.')
else:
    # Este set de acciones se ejecuta cuando la respuesta es F
    print('Ud. es menor de edad.')

# Solicite al usuario el ingreso de datos personales (nombre, edad y título)
# Si el usuario es mayor de edad, muestre por pantalla todos sus datos
# Si el usuario NO es mayor de edad, muestre un mensaje indicando que es menor de edad.

nombre = input('Ingrese su Nombre: ')
str_edad = input('Ingrese su Edad: ')
titulo = input('Ingrese su Título: ')
edad = int(str_edad)

datos_personales = {
    'nombre':nombre,
    'edad':edad,
    'titulo':titulo
}

if datos_personales['edad'] >= 18:
    print(datos_personales)
else:
    print('Ud. es menor de edad.')

# Para evaluar varias condiciones usamos IF con ELIF

# Clase Alta ÉliteSobre $7.000.000
# Clase Alta Profesional $3.500.000 - $7.000.000
# Clase Media Alta $2.000.000 - $3.500.000
# Clase Media $1.200.000 - $2.000.000
# Clase Media Baja $700.000 - $1.200.000
# Clase Baja Menos de $600.000

str_sueldo_mensual = input('Ingrese su sueldo mensual: $')
sueldo_mensual = 0.0 # float (str_sueldo_mensual)

if str_sueldo_mensual.isdigit():
 sueldo_mensual = float(str_sueldo_mensual)

else :
    print ( " valor ingresado no corresponde ")

if sueldo_mensual > 0:

 if sueldo_mensual > 7000000:
    print('Ud. pertenece al grupo Alta Elite')
elif 3500000 < sueldo_mensual <= 7000000:
    print('Ud. pertenece al grupo Alta Profesional')
elif 2000000 < sueldo_mensual <= 3500000:
    print('Ud. pertenece al grupo Media Alta')
elif 1200000 < sueldo_mensual <= 2000000:
    print('Ud. pertenece al grupo Media Emergente')
elif 700000 < sueldo_mensual <= 1200000 :
     print("ud.pertenece al grupo media baja ")
elif 600000 < sueldo_mensual <= 700000 : 
    print("ud.pertenece al grupo baja menos")

else : 
    print('Sueldo ingresado NO corresponde...')