#crea una lista hasta una cierta cantidad de alumnos
#crea un lista de tres calificaciones
#crea que como minimo tenga una calificacion
#mostrar una linea por dada alumno, con su calificacion promedio

#RETO SEMANAL 7
lista = [] # se crea una lista vacia
num_alumnos = int(input("Ingresa el número de alumnos: "))#se solicita la cantidad de alumnos que desea ingresar sus calificaciones
nota = input("*Favor de ingresar minimo una calificación*")
contador =  0 # se agraga un contador
while True: #miestras esto se verdadero se ejecutara
    
    if num_alumnos > contador: 
        nombre = input("Nombre del alumno:  ").capitalize() #ingresa en nomber de alumno y lo coloca con la inicial con mayuscualas
        calificacion1 = int(input(f"Ingrese la Primera Calificación {nombre}:  "))#solicita la calf. 1 y se coloca el nombre del alumno
        calificacion2 = int(input(f"Ingrese la Segunda Calificación {nombre}:  "))#solicita la calf. 2 y se coloca el nombre del alumno
        calificacion3 = int(input(f"Ingrese la Tercera Calificación {nombre}:  "))#solicita la calf. 3 y se coloca el nombre del alumno
        promedio = int(calificacion1 + calificacion2 + calificacion3) //3 #se saca el promedio de calificaciones
        contador += 1 #se suba al contador 1
        alumno = [nombre, calificacion1, calificacion2, calificacion3, "Promedio es:", promedio ] # se hace una lista para que guarde las calificaciones y el promedio
        lista.append(alumno)#se agrega a la lista la variable alumnos
        
                
    else:    
        num_alumnos == contador #si el numero de alumnos capturado es igual al contador
        print(lista) #se imprime la lista
        print(f"Fin de capturas de Calificaciones de los alumnos.")
        break
    

            
