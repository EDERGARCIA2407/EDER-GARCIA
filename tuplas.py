vocales = ("a","e","i","o","u")
print(vocales[2])

#vocales[2] = "I", No lo puede cambia de i a I por se tupla

print(vocales[:3] + vocales[2:]) 
print(vocales.index("o")) #imprime en que posicion esta la letra O

lista_vocales= list(vocales) # con esto la tupla se convierte en lista
                            #si se pueden modificar
lista_vocales[2]= "I"
print(lista_vocales)

tupla_vocales = tuple(lista_vocales) #se convierne una lista en tupla
tupla_vocales[2]= "I"
print(tupla_vocales)