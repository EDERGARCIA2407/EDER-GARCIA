
#el usuario introduzca el nombre de un Pokémon
#si no existe que le mande un mensaje de error;
#si existe, que muestre una imagen
# las estadísticas
#peso, tamaño, movimientos, habilidades y tipos

#se agregan las librerias necesarias para usar
import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

#se solicita al usuario el nombre del pokemon
pokemon = input("pon un pokemon: ")

#se trae la url
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
respuesta = requests.get(url)

#en caso que halla un error
if respuesta.status_code != 200:
    print("Pokemon no encontrado")
    exit()

datos = respuesta.json()


#se coloca una excepcion en caso que halla un error
try :
    url_imagen = datos ['sprites']['front_default']
    imagen = Image.open(urlopen(url_imagen))
except:
    print("el pokemon no tiene imagen") 
    exit() 


#se imprime la imagen
plt.title(datos['name'])
imgplot = plt.imshow(imagen)
plt.show()


espacios =("******************")

print(espacios)
print ("MOVIMIENTOS DE " + pokemon + ' SON: ')
movimientos = datos['moves']
for i in range(int(len(movimientos))):
    movimiento = movimientos[i]['move']['name']
    print(movimiento)

#se imprime todos los movimiento
print(espacios)
print ("EL PESO " + pokemon + ' ES: ')
peso = datos['weight']
print(peso)

#se imprime todas las habilidades
print(espacios)
print ("HABILIDADES DE " + pokemon + ' SON: ')
habilidades = datos['abilities']
for i in range(int(len(habilidades))):
    habilidad = habilidades[i]['ability']['name']
    print(habilidad)

#se imprime el tipo
print(espacios)
print ("TIPO DEL " + pokemon + ' ES: ')
tipos = datos['types']
for i in range(int(len(tipos))):
    tipo = tipos[i]['type']['name']
    print(tipo)

#se imprime el tamaño
print(espacios)
print ("EL TAMAÑO DE " + pokemon + ' ES: ')
tamaño = datos['height']
print(tamaño)


