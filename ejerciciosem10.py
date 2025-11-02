#solicitar al usuario un sierto nuemero de personas para agregar a un formulario
#solcitar el nombre de todas las personas que ingresara
#pregunte la edad de cada persona
#pregunte el sexo de cada persona, refiriendose a ella por su nombre
#si no se especifica el sexo, se guardara en una variable "No especifiado"
#se unen los tres datos introducidoes en una dupla y se imprime en pantalla

def agragar_datos(lista, valor ="no especificado"):
    """ 
    funcion que agrega undato a un lista especifica
    """
    if valor == "":
        valor = "no especificado"
    lista.append(valor)
    return lista    
    """"""



nombres = []
edades = []
sexos = []

personas = int(input("cuantas personas se quieren registar: "))
for i in range(personas):
    nombre = input(f"ingrese el nombre de la persona {i + 1}: ").title()
    nombre = agragar_datos(nombres, nombre)
for i in range(personas):
    edad = input(f"Ingrese la edad de {nombres[i]}: ")
    edades = agragar_datos(edades, edad)
for i in range(personas):
    sexo = input(f"¿Cual es el sexo de {nombres[i]}? ")
    sexos = agragar_datos(sexos,sexo)

for i in zip(nombres,edades,sexos):
    print(i)



