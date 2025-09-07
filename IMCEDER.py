
#DAMOS LA BIENVENIDA AL ISSTE
#DEJO ESPACIO PARA QUE SE VEA MEJOR
print("""  
                         """)


print("""  *********BIENVENIDOS Al ISSSTE**********   
            DONDE LA SALUD ES NUESTRA PRIORIDAD""")

print("TE DIREMOS CUAL ES TÚ INDICE DE MASA CORPORAR (IMC)?")
print("")
print("Favor de ingresar los sigientes datos")
print("""  
                         """)

#SOLICIAMOS EL NOMBRE Y SE UTLIZA WHILE PARA QUE SE CUMPLA LA CONDICION,
# PERO SI CAPTURAN UN DIGITO EN LUGAR DE UNA PALABRA 
# NOS ENVIA UN MENSAJE DE ERROR
while True:
    nombre = input("¿Cual es tu nombre?__")
    if nombre.isdigit():
        print("**ERROR** espara una palabara y no un numero")
#SI EN EL NOMBRE SE CAPTURA UN ESTACIO VACIO
#  NOS ENVIA MENSAJE DE ERROR
    elif nombre.strip() == "":
        print("**ERROR** el Nombre no puede estar vacio")
#SI SE CAPTURA PALABRAS SE CIERRA EL CLICLO Y SE SIGUE CON LA SIGUIENTE PREGUNTA
    else:
        print("   ")
        break

#SOLICIAMOS EL APELLIDO PATERNO Y SE UTLIZA WHILE PARA QUE SE CUMPLA LA CONDICION,
#  PERO SI CAPTURAN UN DIGITO EN LUGAR DE UNA PALABRA 
# NOS ENVIA UN MENSAJE DE ERROR
while True:
    apellidouno = input("¿Cual es tu apellido Paterno?__")
    if apellidouno.isdigit():
        print("**ERROR** espara una palabara y no un numero")
#SI EN EL APELLIDO PATERNO SE CAPTURA UN ESTACIO VACIO
#  NOS ENVIA MENSAJE DE ERROR
    elif apellidouno.strip() == "":
        print("**ERROR** el Apellido no puede estar vacio")
#SI SE CAPTURA CORRECTAMENTE SE CIERRA EL CLICLO Y SE SIGUE CON LA SIGUIENTE PREGUNTA 
    else:
        print("   ")
        break
#SOLICIAMOS EL APELLIDO MATERNO Y SE UTLIZA WHILE PARA QUE SE CUMPLA LA CONDICION
#  PERO SI CAPTURAN UN DIGITO EN LUGAR DE UNA PALABRA 
# NOS ENVIA UN MENSAJE DE ERROR

while True:
    apellidodos = input("¿Cual es tu apellido Materno?__")
    if apellidodos.isdigit():
        print("**ERROR** espara una palabara y no un numero")
#SI EN EL APELLIDO MATERNO SE CAPTURA UN ESTACIO VACIO
#  NOS ENVIA MENSAJE DE ERROR
    elif apellidodos.strip() == "":
        print("**ERROR** el Apellido no puede estar vacio")
#SI SE CAPTURA CORRECTAMENTE SE CIERRA EL CLICLO Y SE SIGUE CON LA SIGUIENTE PREGUNTA   
    else:
        print("   ")
        break
#SE SOLICITA LA EDAD, SI EN EL EDAD SE CAPTURA UN ESTACIO VACIO
#  NOS ENVIA MENSAJE DE ERROR
while True:
    edad = input("¿Cuántos años tienes?__").strip()
    if edad.strip() == "":
        print("**ERROR** la Edad no puede estar vacio")
#SI EN EL EDAD, NO ES UN NUMERO
#  NOS ENVIA MENSAJE DE ERROR
    elif not edad.isdigit():
        print("**ERROR** la Edad no acepta palabas, solo numeros")
    else:
        print("   ")
        break
#SE HACE UNA VARIABLE TIPO FLOAT PARA COLOQUE EL PESO CON DECIMALES 
# Y AL MISMO TIEMPO IMPRIMA LA PREGUNTA

peso = float(input("¿Cual es tú pesos en KG__"))
print("   ")
#SE HACE UNA VARIABLE TIPO FLOAT PARA COLOQUE EL ALTURA CON DECIMALES 
# Y AL MISMO TIEMPO IMPRIMA LA PREGUNTA
altura = float(input("¿Cuál es tu altura en METROS?__"))
#SE REALIZA LA FORMULA PARA GENERAR LA IMC = PESO/(ALTURA*ALTURA)
imc = peso / (altura**2)
print(""" 
             """)
#SE IMPRIME LA INFORMACION RECOLECTADA,
#SE COLOCA EL NOMBRE UTILIZANDO CAPITALIZE PARA OBTERNER LA 
#PRIMERA LETRA CON MAYUSCULA
#TAMBIEN SE IMPRIME EL RESULTADO EL IMC REDONDEADO ROUND
print(f"Tú Nombre Completo es:{nombre.capitalize()} {apellidouno.capitalize()} {apellidodos.capitalize()}")
print(f"Tú Edad es:{edad}" )
print("Tú inidice de masa corporal es:" ) 
print(f"{round(float(imc))}  IMC")

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

