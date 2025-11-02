#probando ámbitos
titulo = "probando ámbitos"
suma = 10.5

def sumar():
    suma = 2 + 2
    print(titulo)
    print("suma en ambito loca", suma,id(suma))

print("antes de llamar a la funcion")
print("suma en ambitos global",suma,id(suma))
sumar()
print("despues de llamar a la funcion sumar")
print("suma en ambito global",suma,id(suma))