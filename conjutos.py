
# conjunto {} con llaves
canasta = {"manzana", "naranja", "manzana", "pera","naranja","platano"}
print(canasta) #conjuntos no imprime duplicados de la lista
print("manzana" in canasta) #in busca dentro de la lista canasta "true"
print("melon" in canasta) #in busca melon dentro d ela canasta "false"

#lista [] con cochetes
vocales = ["a","e","i","o","u","a"]
print(vocales)
vocales = list(set(vocales))#convierte la lista en llaves
print(vocales)

#cojunto dentro de otro conjunto
vocales1 = {"a","e","i","o","u","a"}
vocales2 = {"e","i","o"}
print(vocales2.issubset(vocales1)) #funcion issubset busca los datos de una lista en otra
                                #si esta coloca "true"

#resta de conjuntos
vocales1 = {"a","e","i","o","U" }
vocales2 = {"A","E","I","O","U"}
print(vocales1 - vocales2) #no hace la resta porque todos son diferentes

#unir conjuntos
print(vocales1 | vocales2) #une las dos lista en una

#busqueda en un dato en un cojunto
print( vocales1 & vocales2) # & buscar un valor dentro de dos cojuntos

#busca solos lo datos que no estan repetidos
print( vocales1 ^ vocales2) #coloca solo los datos que no estan repetidos