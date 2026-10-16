# Una sala de cine vende entradas con estas reglas:
# la entrada general cuesta 8 €;
# las personas menores de 12 años pagan 5 €;
# las personas de 65 años o más pagan 6 €;
# los miércoles se aplica un descuento adicional de 1 €;
# una sesión en formato 3D añade 2 €.
# Pide la edad, el día de la semana y si la sesión es 3D. 
# Calcula el precio final y muestra el desglose de los importes aplicados. 
# Rechaza edades negativas y decide qué debe ocurrir con una edad que no pueda convertirse a número. 
# Normaliza el día introducido para aceptar mayúsculas y espacios sobrantes. 
# Prueba edades por debajo, justo en y por encima de 12 y 65, tanto en una sesión normal como en una sesión 3D.


edad = int(input("Introduce tu edad: "))

if edad < 0:
    print("La edad no puede ser negativa.")
else:
    dia = input("Introduce el día de la semana: ").strip().lower()
    respuesta = input("¿La sesión es 3D? si/no: ").strip().lower()

  
    match edad:
        case numero if numero < 12:
            precio_base = 5
        case numero if numero < 65:
            precio_base = 8
        case _:
            precio_base = 6


    match dia:
        case "miércoles" | "miercoles":
            descuento = 1
            dia_valido = True
        case "lunes" | "martes" | "jueves" | "viernes" | "sábado" | "sabado" | "domingo":
            descuento = 0
            dia_valido = True
        case _:
            print("El día introducido no es válido.")
            descuento = 0
            dia_valido = False


    match respuesta:
        case "si" | "sí":
            suplemento = 2
            respuesta_valida = True
        case "no":
            suplemento = 0
            respuesta_valida = True
        case _:
            print("Se debe responder sí o no.")
            suplemento = 0
            respuesta_valida = False

    if dia_valido and respuesta_valida:
        precio_final = precio_base - descuento + suplemento

        print("Precio base:", precio_base, "€")
        print("Descuento:", descuento, "€")
        print("Suplemento 3D:", suplemento, "€")
        print("Precio final:", precio_final, "€")
