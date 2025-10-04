#Longitud de una frase
#Crear un programa para identificar la longitud de una palabra ingresada
#La palabra correcta debe tener entre cuatro y ocho letras
#Si la longitud de la palabra se encuentra en el rango de cuatro a ocho letras, 
# se debe imprimir un mensaje que indique que la palabra es correcta.
#Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: 
# “Hacen falta letras. Solo tiene N letras” (siendo N el número de letras de la palabra).
#Si la palabra tiene más de 8 letras debe indicar un mensaje que diga:
#“Sobran letras. Tiene N letras” (siendo N el número de letras de la palabra).

palabra = input("Ingresa una palabra: ") #solicita ingresar la letra
letras =len(palabra) #se declara variable y muestre la cantidad de letras de la palabra 

if letras <=8 and letras >= 4: #se coloca la condicion del conteo de las letras
    print("La parabra es correcta")
    print("Palabra corresta" , {letras}, "letras") # se imprime la cantidad de letras que coontiene la palabra

elif letras <=3: #se coloca condicion menor o igual a 3 letras
    print("Hace falta letras. Solo tiene", {letras},"letras")

elif letras > 8: #se coloca condicion mayor a 8 letras
    print("Sobran letras. Tiene", {letras}, "letras")

else:
    print("")
#####################################################################

#2.	Encuentra el cuadrante
#Crear un programa que en base a 2 números de entrada, coordenadas, 
#identifique en cuál de los 4 cuadrantes se encuentra el punto.

#se solicita el ingreso de los valores en x y y
x = int(input("Ingrese el valor en x: "))
y = int(input("Ingrese el valor en y: "))

if x == 0 and y == 0: #se coloca la condicion para el origen
    print("El punto está en el origen",{x,y})
elif x > 0 and y > 0: # se coloca la condicion para el I cuandrante
    print("El punto esta en el Cuadrente I", "x=", (x), "y=", (y)) #se impirme el num. cuandrante y valores en x y 
elif x < 0 and y > 0:# se coloca la condicion para el II cuandrante
    print("El punto esta en el Cuadrente II", "x=", (x), "y=", (y)) 
elif x < 0 and y < 0:# se coloca la condicion para el III cuandrante
    print("El punto esta en el Cuadrente III", "x=", (x), "y=", (y)) 
elif x > 0 and y < 0:# se coloca la condicion para el IV cuandrante
    print("El punto esta en el Cuadrente IV", "x=", (x), "y=", (y)) 
else:
    print("Fin de programa")


