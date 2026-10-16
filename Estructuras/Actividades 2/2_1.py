import random

titular = "Alejandro"
saldo = random.randint(0, 1000)
estado = True


operacion = input("¿Qué operación quieres realizar?")
operacion_limpia = operacion.lower().strip()

match operacion_limpia:
    case "ingresar":
        cantidad = int(input("Dinero a ingresar: "))
        if cantidad > 0:
            saldo += cantidad
        else:
            print("Cantidad no válida")
            
    case "retirar":
        cantidad = int(input("Dinero a retirar: "))
        if cantidad > 0 and saldo >= cantidad:
            saldo -= cantidad
        else:
            print("Cantidad no válida")
            
            
    case "abrir":
        if not estado:
            estado = True
        else:
            print("La cuenta ya está activa")    
    case "cerrar":
        if estado and saldo == 0:
            estado = False
            print("Cuenta cerrada")
        else:
            print("La cuenta ya está cerrada")
            
            
    case "consultar":
        print("Tu saldo es: ", saldo)
    case _:
        print("Operación no válida")
        