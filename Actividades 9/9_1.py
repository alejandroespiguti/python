# Calcular una factura. Crea un programa que lea precio, unidades y porcentaje de descuento, calcule subtotal, descuento, IVA y total, 
# y muestre cada importe con dos decimales. Añade una condición que indique si el pedido supera un umbral de envío gratuito.

precio = float(input("Introduce el precio:"))
unidades = int(input("Introduce las unidades:"))
porcentaje_descuento = float(input("Introduce el porcentaje de descuento:"))

subtotal = precio * unidades
descuento = subtotal * porcentaje_descuento / 100
precio_sin_iva = subtotal - descuento

iva = precio_sin_iva * 21 / 100
total = precio_sin_iva + iva

print("El subtotal es:", round(subtotal, 2), "euros")
print("El descuento es de:", round(descuento, 2), "euros")
print("El IVA es:", round(iva, 2), "euros")
print("El total es:", round(total, 2), "euros")

print("Envío gratuito:", total >= 100)