
#DAMOS LA BIENVENIDA AL ISSTE
#DEJO ESPACIO PARA QUE SE VEA MEJOR
print("""  
                         """)

print("""  *********BIENVENIDOS Al ISSSTE**********   
        DONDE LA SALUD ES NUESTRA PRIORIDAD""")
print("")

print("TE DIREMOS CUAL ES TÚ INDICE DE MASA CORPORAR (IMC)?")
print("")
print("Favor de ingresar los sigientes datos")
print("""  
                         """)
#SE REALIZO UNA VARIABLE ESPACIO, PARA TENER ESPACIO ENTRE CADA PREGUNTA
espacio = (" ")
#SE HACE UNA VARIABLE TIPO STR PARA COLOCAR EL NOMBRE Y AL MISMO TIEMPO IMPRIMA LA PREGUNTA

nombre = input("¿Cual es tu nombre? : ")
print(espacio)
#SE HACE UNA VARIABLE TIPO STR PARA COLOCAR EL APELLINO PATERNO Y AL MISMO TIEMPO IMPRIMA LA PREGUNTA
apellidouno = str(input("¿Cual es tu apellido Paterno? : "))
print(espacio)
#SE HACE UNA VARIABLE TIPO STR PARA COLOCAR EL APELLIDO MATERNO Y AL MISMO TIEMPO IMPRIMA LA PREGUNTA
apellidodos = str(input("¿Cual es tu apellido Materno? : "))
print(espacio)
#SE HACE UNA VARIABLE TIPO ENTERO INT Y AL MISMO TIEMPO IMPRIMA LA PREGUNTA
edad = int(input("¿Cuántos años tienes? : "))
print(espacio)
#SE HACE UNA VARIABLE TIPO FLOAT PARA COLOQUE EL PESO CON DECIMALES 
# Y AL MISMO TIEMPO IMPRIMA LA PREGUNTA
peso = float(input("¿Cuál es tu peso en KG? : "))
print(espacio)
#SE HACE UNA VARIABLE TIPO FLOAT PARA COLOQUE EL ALTURA CON DECIMALES 
# Y AL MISMO TIEMPO IMPRIMA LA PREGUNTA
altura = float(input("¿Cuál es tu altura en METROS? : "))
#SE REALIZA LA FORMULA PARA GENERAR LA IMC = PESO/(ALTURA*ALTURA)
imc = peso / (altura**2)
print(espacio)
#SE IMPRIME LA INFORMACION RECOLECTADA,
#SE COLOCA EL NOMBRE UTILIZANDO CAPITALIZE PARA OBTERNER LA 
#PRIMERA LETRA CON MAYUSCULA
#TAMBIEN SE IMPRIME EL RESULTADO EL IMC REDONDEADO ROUND
print(f"Tú Nombre Completo es:{nombre.capitalize()} {apellidouno.capitalize()} {apellidodos.capitalize()}")
print(f"Tú Edad es:{edad}" )
print("Tú inidice de masa corporal es:" ) 
print(f"{round(float(imc))}  IMC")

#COMO AYUDA PARA SABER LOS SIMBOLOS 
#a==b a es igual que b
#a!=b a distintos que b
#a<=b a es menor o igual que b
#a>=b a es mayo o gual que b

#SE UTILIZA EL IF Y ELIF PARA TENER LOS RANGOS DONDE SE ENCUENTRA IMC CALCULADO
#Y NOS IMPRIME EL RESULTADO EN FUNCION DE IMC OPTENIDO
if imc >=0 and imc<=18.49:
    print ("ESTAS BAJO DE PESO")
elif imc >=18.5 and imc<=24.90:
    print("*TÚ PESO ES NORMAL* (sigue asi...)")
elif imc >=25 and imc<=29.90:
    print("**ESTAS CON SOBREPESO**")
elif imc >=30 and imc<=34.90:
    print("**ESTAS EN OBESIDAD LEVE**")
elif imc >=35 and imc<=39.90:
    print("**ESTAS EN OBESIDAD MODERADA**")
elif imc >=40:
    print("**ESTAS EN OBESIDAD MORDIBIDA**")

print("///GRACIAS POR SU VISTA///")