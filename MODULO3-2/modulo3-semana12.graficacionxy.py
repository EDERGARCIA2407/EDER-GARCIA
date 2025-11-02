#grafico de dispecion
#funcion scatter

import random
import matplotlib.pyplot as plt

#genera numero aleatorios del 1 al 100 en el eje de las x
eje_x = [random.randint(1, 100) for n in range(100)]
#genera numero aleatorios del 1 al 100 en el eje de las y
eje_y = [random.randint(1, 100) for n in range(100)]

#funcion scatter
plt.scatter(eje_x, eje_y)
#titulo de la grafica
plt.title("grafica de dispersion")
plt.show()
