#uso de la sentencia continue en un ciclo for
# for numero in range (1,11):
#     if numero % 2 == 1: # % es el residuo de una division ej 3/2 = 1.5 residuo es 5
#       continue
#     print(f"{numero} es numero par")

#Uso de la sentencia continue en un ciclo while

# numero = 0
# while numero < 11:
#    numero += 1
#    if numero % 2 == 0:
#       continue
# print(f"{numero} es numero imprar")
###############################################################

# #uso de la sentencia break
# numero = int(input("ingresa un digito: "))
# limite_inferior = 0
# limite_superior = 10
# buscado = 5
# intentos = 0

# while True:
#     intentos += 1
#     if numero == buscado:
#         print(f"el numero {numero} fue encontrado en {intentos} intentos")
#         break
#     elif numero < buscado:
#         limite_superior = buscado
#         buscado = (buscado + limite_inferior) // 2
#     elif numero < buscado:
#         limite_inferior = buscado

############

intentos = 0
while True:
    intentos += 1
    print(f"intento {intentos}")
    if intentos == 20:
        print("fin programa")
        exit()
        
