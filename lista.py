
###### lista 1
# cuadrados = [0,1,4,9,16,25]
# for i in range(len(cuadrados)):
#     #print(f"{i}**2 = {cuadrados[i]}") #imprime al al cuadado el dato
#    # cuadrados [i] = cuadrados [i] * i
#    # print(f"Ahora estan al cubo {cuadrados[i]}")

#     cuadrados.append(7 ** 3) #append nos añade un elemento a la lista
#     cuadrados.insert(6, 6 ** 3) #insert coloca un numero en la lista iniciando con la prosiocn
#     cuadrados.extend([27,100,-1]) #inserta los valores al final de la lista
#     cuadrados.extend(range(-2,-4,-1 ))
#     print(cuadrados)

#     del cuadrados[9:] #solo se nuestra hasta el dato 9
#     print(cuadrados)
#     cuadrados.remove(25) #remueve el primer elemento
#     print(cuadrados)
#     valor_removido = cuadrados.pop(2) # se extrae el dato 1
#     print(valor_removido)
#     cuadrados.clear()   
#     print(cuadrados)

######## listas 2

# vocales = ["a","e","i","o","u"]
# vocales[1:4]= ["E","I","O"] #sustituye las letras con mayuscula (1)a partir e hasta (3)o
# print(vocales, len(vocales))
# vocales[1:4]=[] #elimina lo que esta dentro de los datos 1 al 4
# print(vocales, len(vocales))
# vocales[1:2] = ["e","i","o","u"] #agrega las vocales izq 0,1 y de der 
# print(vocales, len(vocales))
# vocales.extend(["i", "i"])  #se agregan mas letras a la lista
# print(vocales, len(vocales))
# print(vocales.index("i"))#buscar la primera letra de la lista y coloca la posicion
# print(vocales.count("i"))#cuenta las veces que hay de esa letra en la lista
# print(vocales.index("i",3)) #busca la letra i desde el posicion 2
# vocales.reverse() #colocar una lista alreves
# print(vocales, len(vocales))
# vocales.sort()#lista ordenada acendente
# print(vocales, len(vocales))

##### lista 3

# carro =[ "Audi", "Ford", "BMW", "VW"]
# carro.sort(key=len) #se ordenas de menos elemento a mas elementos
#                     #si hay dos elementos con las misma cantidad de letras
#                     # los ordena de forma acendente 
# print(carro)

#### lista 4 listas dentro de listas

# lista = [[0,1], [2,3,4], [5,6]]
# print(lista[0],lista[1:2])
# print(lista[2][1])

#### lista 5

vocales1 = ["a","e","i","o","u"]
vocales2 = vocales1
print(vocales1,vocales2)
print(id(vocales1),id(vocales2))
vocales3 = vocales1.copy()
print(vocales1,vocales3)
print(id(vocales1),id(vocales3))
print(id(vocales1[2]), id(vocales2[2]),id(vocales3[2])) #se impirme solo el id un valos ej, la "i"

del vocales1[2] #elimina la letra "i", 
print(vocales1,vocales3) #imprime son la letra "i" vocales1, vocales3 no lo elimina
                         #porque se creo otro objeto

