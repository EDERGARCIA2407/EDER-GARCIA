
#el usuario introduzca el nombre de un Pokémon
#si no existe que le mande un mensaje de error;
#si existe, que muestre una imagen
# las estadísticas
#peso, tamaño, movimientos, habilidades y tipos

import requests
import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

pokemon = input("pon un pokemon: ")

url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
respuesta = requests.get(url)

if respuesta.status_code != 200:
    print("Pokemon no encontrado")
    exit()

datos = respuesta.json()



try :
    url_imagen = datos ['sprites']['front_default']
    imagen = Image.open(urlopen(url_imagen))
except:
    print("el pokemon no tiene imagen") 
    exit() 

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

print(espacios)
print ("EL PESO " + pokemon + ' ES: ')
peso = datos['weight']
print(peso)

print(espacios)
print ("HABILIDADES DE " + pokemon + ' SON: ')
habilidades = datos['abilities']
for i in range(int(len(habilidades))):
    habilidad = habilidades[i]['ability']['name']
    print(habilidad)

print(espacios)
print ("TIPO DEL " + pokemon + ' ES: ')
tipos = datos['types']
for i in range(int(len(tipos))):
    tipo = tipos[i]['type']['name']
    print(tipo)

print(espacios)
print ("EL TAMAÑO DE " + pokemon + ' ES: ')
tamaño = datos['height']
print(tamaño)
