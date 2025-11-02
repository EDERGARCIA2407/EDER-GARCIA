#debe usar almenos dos fuciones
#preguntas cuantos alumnos se registraran, en caso que no ingresar una cantidad,
#se asume que registraran 3 alumnos
#preguntara el nombre y 2 calificaciones
#mostrar el nombre en pantalla con inicial mayuscula y promedio
#al finalizar el programa se motarar una lista con el nombre de cada alumno y sus calif.

def captura_alumnos(numero =3):

    """ registra alumnos y dos calificaciones
        recibe como parametro la cantidad de alumnos a registrar
        sino se especifica el numero de alumnos, se registraran"""
    litsa_alumnos=[]
    for i in range(numero):
        nombre = input(f"{i+1}.-Ingrese el nombre del alumno: ").capitalize()
        calificacion1 = int(input(f"Ingrese la primera calificacion de {nombre}: "))
        calificacion2 = int(input(f"Ingrese la segunda calificacion de {nombre}: "))
        litsa_alumnos.append([nombre,calificacion1,calificacion2])
        promedio(nombre,calificacion1,calificacion2)
    print("las calificaciones de los alumnos son: ", litsa_alumnos)

def promedio(nombre, calificacion1, calificacion2):
    """ calcula el promedio de un alumno y lo despliega en pantalla por medio de un mensaje
    recibe como parametros el nombre y dos calificaciones del alumno"""
    promedio= (calificacion1 + calificacion2) /2
    print(f"El promedio de {nombre} es: {promedio}")

numero_alumnos=input("CUANTOS ALUMNO DESEA REGISTRAR: ")

if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else:
    captura_alumnos()