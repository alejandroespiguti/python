# Una sala admite como máximo 8 personas. El programa debe llevar la cuenta de cuántas hay dentro. En cada turno, pide una acción: entra, sale o fin.
# Si la acción es entra y aún hay plazas, aumenta el aforo ocupado en uno.
# Si la sala está llena, no admitas a nadie más e informa de ello.
# Si la acción es sale y hay personas dentro, reduce el aforo ocupado en uno.
# Si la sala está vacía, no permitas que salga una persona y avisa de que no hay nadie dentro.
# Si se escribe fin, termina el control e informa de cuántas personas quedan en la sala.
# Después de cada acción distinta de fin, muestra el aforo actual. Supón que las acciones introducidas son válidas. 
# Prueba entradas y salidas en los límites, como intentar entrar con la sala llena y salir cuando está vacía.

personas = 0
accion = ""

while accion != "fin":
    accion = input("¿Qué acción deseas realizar? (entrar, salir, fin): ")
    
    match accion:
        case "entrar":
            if personas < 8:
                personas = personas + 1
            else:
                print("la sala está llena.")
                
        case "salir":
            if personas > 0:
                personas = personas - 1
            else:
                print("No hay nadie dentro.")
                
    print("Aforo actual:", personas, "de 8")
    
print("Control finalizado.")
print("Personas que quedan en la sala: ", personas)