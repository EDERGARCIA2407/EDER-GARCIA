#Simulacion de una grafica de Galton de 3000 canicas
#En total tendra 12 niveles de obstaculos. Debera decidir si va a caer
# a un lado o al otro 12 veces.
#El resultado sera un histograma que represente la cantidad de canicas
#en cada contenedor, nombre en los ejes y titulo al grafico
#Deberas empleas dos funciones:
#1. Para calcular los resultados del las canicas
#2. Para graficar en un Histograma


import matplotlib.pyplot as plt
import random
import numpy as np

def simular_canicas(n_canicas, niveles):
    """
    Simula la trayectoria de cada canica a través de los niveles.
    Cada nivel representa izquierda o derecha.
    Retorna una lista con el número de veces que cada canica cayó a la derecha.
    """
    resultados = np.random.normal(niveles, 0.5, n_canicas)
    return resultados

def graficar_histograma(resultados, niveles):
    """
    Grafica un histograma de los resultados de las canicas.
    """
    plt.hist(resultados, niveles, color='blue')
    plt.title('Simulación de Máquina de Galton (3000 canicas, 12 niveles)')
    plt.xlabel('Contenedor (número de veces que cayó a la derecha)')
    plt.ylabel('Cantidad de canicas')
    plt.show()

# Parámetros de la simulación
n_canicas = 3000
niveles = 12

# Ejecutar simulación y graficar
resultados = simular_canicas(n_canicas, niveles)
graficar_histograma(resultados, niveles)
