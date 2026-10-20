# Un sistema permite hasta tres intentos para introducir un código. El código correcto es "4826".
# Pide el código y comunica si el acceso está autorizado. Si no es correcto, permite intentarlo de nuevo y avisa de 
# cuántos intentos quedan. Después del tercer error, muestra que el acceso se ha bloqueado. 
# Cuando el código sea correcto, no vuelvas a pedirlo.
# Prueba el caso en que se acierta en el primer intento, en el último intento y en ninguno. 
# Resuelve el ejercicio usando un bucle y condicionales.

codigo_correcto = "4826"
codigo = ""
intentos = 0

while intentos < 3 and codigo != codigo_correcto:
    codigo = input("Introduce el código: ")
    intentos = intentos + 1
    
    if codigo != codigo_correcto:
        if intentos < 3:
            print("Código incorrecto. Te quedan", 3 - intentos, "intentos.")
            
        else:
            print("Acceso rechazado.")
    else:
        print("Acceso autorizado.")