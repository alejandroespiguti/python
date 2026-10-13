# Guarda si una persona está matriculada (True), si tiene autorización especial (False) y su edad (17). 
# Puede acceder si está matriculada y tiene al menos 18 años, o si tiene autorización especial. 
# Calcula y muestra el resultado como True o False. Cambia los valores para comprobar también un caso en el que sí pueda acceder.

matriculado = True
autorización_especial = False
edad = 17

acceso = (matriculado and edad >= 18) or autorización_especial

print("¿Puedes acceder?:", acceso)

matriculado = True
autorización_especial = False
edad = 18

acceso = (matriculado and edad >= 18) or autorización_especial

print("¿Puedes acceder?:", acceso)