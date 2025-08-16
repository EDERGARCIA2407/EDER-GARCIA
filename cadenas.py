#colocar 3 comillas al inicio y al final para separar los texto
#print ("""
#funcionamiento de :
#programas: opcionales
#-1 para acceder
#-2 prar salir""")

#subscripting e indexado
#texto = "Python"
#print(texto [0])
#print(texto [5])
#print(texto [-1])
#print(texto [-6])

#letra = texto [0]
#print (letra)

#texto [0] = "p" #no podemos modificar una cadena

#letra = "p"
#print (letra)

#texto_compuesto = letra + texto [1]
#print(texto_compuesto)

#variable = "#"
#print(variable *40)
##################################################
#slicing o substringing

# texto = "Python"

# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[0:3])

# print(texto[-3::-1])
# print(texto[::-1]) #letras al reves

# print(texto[1:50])

##########################################
#cadena y formatos

# texto = "Hola Mundo Buenastardes"
# print(texto.lower()) #imprime con minusculas todo el texto
# print(texto.upper()) #imprime con mayusculas
# print(texto.capitalize()) #imprime solo la primera letra mayuscula
# print(texto.title()) #imprime solo la primera letra mayuscula de cada palabra
# print(texto.swapcase()) #imprime la primera letra en minusculas y el resto con mayusculas

# texto = texto.upper()
# print(texto)

print("{} + {} = {}".format(2,3,2+3))
print("{} + {} = {}".format("Hola", "Mundo" ,"Hola Mundo"))
print("{:.3f} + {:.4f} = {}".format(2,3,2+3)) #que se coloque decimales 1.000 y 2 .0000
print("{1} + {0} ={2}".format(2,3,2+3)) #se coloca la secuencia 0=2, 1=3, 2=2+3
print("{2} + {0} = {1}".format("Hola", "Mundo" ,"Hola Mundo"))
print("{:d} = {:b} = {:o} = {:x}".format(15,15,15,15))


