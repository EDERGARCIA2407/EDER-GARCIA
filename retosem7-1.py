#crea un lista de tres calificaciones
#crea que como minimo tenga una calificacion
#mostrar una linea por dada alumno, con su calificacion promedio

lista = [] # se crea una lista vacia
alumnos = 0 # variable iniciando 0

while alumnos <=5: # maximo de capturas serian 6 alumnos
    opcion = input("Agregar alumno (1) o terminar (2): ")
    if opcion == "1": #se guarda como cadena
       nombre = input("Ingrese el nombre del alumno: ").capitalize() #imprima la primera letra en mayuscula
       calificacion1 = int(input(f"Ingrese la Primera Calificación {nombre}:"))     
       calificacion2 = int(input(f"Ingrese la Segunda Calificación {nombre}:"))
       alumno = [nombre, calificacion1, calificacion2] # se hace una lista para que guarde
       lista.append(alumno) #se agrega a la lista
       alumnos += 1 #se coloca un contador
    elif opcion == "2": #si el usuario coloca la opcion 2 entonces
       print(f"El programa ha terminado con {alumnos} alumnos.")
       break
    else :
       print("Se ha ingresado una opción inválida") #si capturar alguna otra opcion dada
       continue       
       
print("La lista de alumnos es: ")
print(lista) #imprime la lsita que se ingreso