# Que permita crear dos listas de distintas longitudes.
#  ●Que la longitud y los elementos de cada lista sean especificados por el usuario.
#  ●Que imprima las listas indicando que son las listas originales.
#  ●Que elimine de la primera lista los nombres de la segunda.
#  ●Que imprima la primera lista indicando que se han eliminado los elementos que 
# estaban también en la segunda.

def crear_lista(nombre_lista): #crear una funcion
    #variable para guardar al cantidad de elementos
    longitud = int(input(f"¿Cuántos elementos tendrá la {nombre_lista}? "))
    lista = []
    for i in range(longitud): #recibe la cantidad de elementos
        #variable para ingresar los elementos
        elemento = input(f"Ingrese el elemento {i + 1} para la {nombre_lista}: ")
        lista.append(elemento)
    return lista

def eliminar_duplicados(lista1, lista2):
    return [elemento for elemento in lista1 if elemento not in lista2]

# Crear listas
lista1 = crear_lista("primera lista")
lista2 = crear_lista("segunda lista")

# Mostrar listas originales
print("\nLista 1 original:", lista1)
print("Lista 2 original:", lista2)

# Eliminar elementos de lista1 que están en lista2
lista1_filtrada = eliminar_duplicados(lista1, lista2)

# Mostrar resultado
print("\nLista 1 después de eliminar elementos que también están en la lista 2:", lista1_filtrada)
