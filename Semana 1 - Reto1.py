#Importamos datetime
from datetime import datetime

#Definir variables
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

#variables para obtener hora actual de libreria daatetime
fecha = datetime.now()
hora = int(format(fecha.hour))


#condicionales
if (edad < 18 and hora >= 18):
    print("Usted debe ir a dormir")
elif (edad < 18 and hora <= 18):
    print("Usted tiene que hacer su tarea")
else:
    print("Usted no estas obligado hacer nada")

