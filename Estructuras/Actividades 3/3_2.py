# Pide un número entero mayor que 1 y determina si es primo. Un número primo solo se puede dividir exactamente entre 1 y entre sí mismo.
# Prueba, si algún número entre 2 y el número anterior al introducido lo divide exactamente. Si encuentras un divisor, el número no es primo, 
# si terminas las comprobaciones sin encontrar ninguno, sí lo es. Muestra el resultado. Comprueba el programa con un número primo, uno compuesto y el 2, 
# que es el menor número primo.

numero = int(input("Introduce un número mayor que 1: "))


if numero > 1:
    primo = True
    
    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            
            
    if primo:
        print("EL número es primo.")
    else:
        print("El número no es primo.")
        
else:
    print("El número debe ser mayor que 1.")