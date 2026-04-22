# Teniendo 3 escalas de temperatura (Celsius, Fahrenheit, Kelvin)
# Cree un conversor de temperaturas que le pida al usuario la temperatura y escala inicial
# Y la escala a la que desea convertir, luego muestre el resultado de la conversión

# °C a F = 1,8°C + 32°
# F a °C = 5/9(°F-32°)

# °C a K = °C + 273°
# K a °C = K - 273°

# K a F = (1,8°C + 32°) + 273°
# F a K = (5/9(°F-32°)) + 273°

msg_escala_erronea = 'Escala final NO corresponde.'

print("Sistema Conversor de Temperaturas")
print("=================================")
print("Para comenzar ingrese su escala inicial")
print("C - para Celsius")
print("F - para Fahrenheit")
print("K - para Kelvin")

print()
escala_inicial = input("Ingrese escala inicial: ").upper()
str_temperatura = input("Ingrese su temperatura: ")
escala_final = input("Ingrese escala final: ").upper()

if str_temperatura.isdigit():
    temperatura = float(str_temperatura)
else:
    print("El valor de temperatura NO corresponde.")

if escala_inicial == "F":
    if escala_final == "K":
        resultado = (5/9 * (temperatura-32)) + 273
    elif escala_final == "C":
        resultado = 5/9 * (temperatura-32)
    else:
        print(msg_escala_erronea)
elif escala_inicial == "C":
    if escala_final == "K":
        resultado = temperatura + 273
    elif escala_final == "F":
        resultado = 1,8 * temperatura+ 32
    else:
        print(msg_escala_erronea)
elif escala_inicial == "K":
    if escala_final == "F":
        resultado = (1,8 * temperatura + 32) + 273
    elif escala_final == "C":
        resultado = temperatura - 273
    else:
        print(msg_escala_erronea)
else:
    print("Escala inicial NO corresponde.")

print(f'{temperatura} {escala_inicial}° = {round(resultado,2)} {escala_final}°')