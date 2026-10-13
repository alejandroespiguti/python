# Guarda en una variable una duración total de 7384 segundos. 
# Calcula cuántas horas completas, minutos restantes y segundos restantes contiene, usando división entera (//) y resto (%). 
# Muestra los tres resultados; deben ser 2 horas, 3 minutos y 4 segundos.

duracion_total = 7384

horas = duracion_total // 3600
minutos = (duracion_total % 3600) // 60
segundos = duracion_total % 60

print(duracion_total, "segundos son:", horas, "horas", minutos, "minutos", segundos, "segundos")