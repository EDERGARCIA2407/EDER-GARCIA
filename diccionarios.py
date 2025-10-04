#los diccionarios se habren con{} y con : y ,
tiempo = {
    "Hamilton": "1:49.8",
    "Bottas": "1:56.4",
    "Perez": "1:53.8",
    "Verstappen": "1:52.3" #ya no se coloca coma al final de la lista
}
#metodo items devulver una lista de tuplas
print(tiempo.items()) #imprime la lista con los nombres y tiempos

#metodo keys nos devuelve solo las claves "nombres"
print(tiempo.keys())
#metodo value devuleve todos los valos del direccionario "tiempos"
print(tiempo.values())
#regresar solo una clave
print(tiempo.get("Perez"))
#regresar solo una clave y sino es igual manda un mensaje
print(tiempo.get("peres", "no esta" ))

##### Convertir una tupla () a direccionario, 

tiempo1= dict(
    Hamilton = "1:49.8",
    Bottas = "1:56.4",
    Perez = "1:53.8",
    Verstappen= "1:52.6"
)
print(tiempo1)

#### el diccionario () no puede tener claves duplicadas, pero valores si pueden ser 
            #duplicados
# tiempo1= dict(
#     Perez = "1:49.8", # marcaria error por que esta duplicada
#     Bottas = "1:56.4",
#     Perez = "1:53.8",
#     Verstappen= "1:52.6"
# )
# print(tiempo1)