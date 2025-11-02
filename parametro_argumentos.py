def sumar(parametro1, parametro2):
    """funcion que suma dos paramentros y los imprime en pantalla"""
    print("suma: ",parametro1 + parametro2)
argumento1 = 5
argumento2 = 7
#estamos invocando a la funcion por medio de paramentros variable
sumar(argumento1, argumento2)

#invocando a la funcion pro medio de parametro variables
sumar("mundo ","hola")
sumar("hola ","mundo") #debe ser igual a los argumentos
#sumar("hola")#se debe colora dos parametros por que se declararon dos parametros

###################################################
#Parametros opcionales

def muestra_alumno(nombre, edad =18, sexo= "F"):
    """ esta funcion que muestra en pantalla el nombre, edad y sexo de un alumno
     recibe tres parémetros"""

    print(f"Nombre:  {nombre}, Edad: {edad}, Sexo: {sexo}")

#EJECUCION DE FUNVION CON PARÁMETRO OBLIGATORIO
muestra_alumno("MARIA")
#EJECUCION UTILIZANDO EL PARAMETRO OBLICATORIO Y UN OPCIONAL
muestra_alumno("MARIA",22)
#EJECUCION DE FUNCION CON EL PRIMER Y UTLIMO PARAMENTRO
muestra_alumno("JUAN", sexo = "M")

