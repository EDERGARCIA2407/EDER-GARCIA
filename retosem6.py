
#RETO SEMANAL 6
while True: #se ejecuta hasta que se cumpla
    contraseña1 = input("Ingrese contaseña: ") # solicita la contraseña
    if not contraseña1[0].isnumeric(): # la condición, si no tiene un numero en el primer carácter
     print("La contraseña debe tener un número") #envia mensaje al usuario
    else:          # si se cumple pasa a la siguiente pregunta
        print("")
        break
contador = 0 # se genera un contador de intentos
while contador <3: #muetras el contador de intentos sea menor que 3, se estará repitiendo el ciclo
    contraseña2 = input("Ingrese la contraseña nueva: ")# se solicita la nueva contraseña
    if contraseña1 == contraseña2: #condicion de que sean iguales
        print("Contraseña correcta \nFin de programa") #si se cumple la condicion se imprime mensaje
        break
    else:
         contador += 1 #se agrega una mas al contador
    if contador == 3: #si cumple esta condicion se finaliza el programa
        print("Fin de programa") #imprime fin de programa por no cumplir 
    else:
        print("")



#   while True:
#     contraseña2 = input("Ingrese la contraseña nueva: ")
#     if contraseña1 != contraseña2:
#         print("La contraseña no concide")
#     else:
#         contraseña1 == contraseña2
#         print ("Contraseña correcta \nFin de programa")   
#         break