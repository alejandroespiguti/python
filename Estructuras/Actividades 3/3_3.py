# Una máquina vende un producto que cuesta 170 céntimos. Solicita el valor de cada moneda en céntimos, de una en una; acepta 10, 20, 50 y 100. 
# La persona puede introducir monedas hasta completar el precio.
# Si se introduce una moneda no aceptada, informa del problema y vuelve a solicitar una moneda sin aumentar el importe pagado. 
# Cuando se haya alcanzado o superado el precio, indica que entrega el producto y cuánto cambio debe devolver. 
# El programa debe terminar en cuanto la compra se pueda completar.No hace falta validar que la entrada se pueda convertir a número. 
# Al final, muestra el cambio tanto en céntimos como en euros.

precio = 170
pagado = 0

while pagado < precio:
    moneda = int(input("Introduce una moneda (10, 20, 50 o 100): "))
    
    
    if moneda == 10 or moneda == 20 or moneda == 50 or moneda == 100:
        pagado = pagado + moneda
    else:
        print("Moneda no aceptada.")
        
cambio = pagado - precio

print("Entregando el producto.")
print("Cambio en céntimos:", cambio)

cambio_euros = cambio / 100
print("Cambio en euros:", cambio_euros, "€")