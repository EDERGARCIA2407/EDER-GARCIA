#Las graficas de datos nos ofrece una representacion visula del comportamineto
# \de la infomracion 
#instalara la biblioteca pip install matplotlib
#para generar una distribucion gauss

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
numeros = np.random.rand(5) #colocando el numero 10, genera 10 numeros aleatorios
#para generar una distribucion gauss
np.random.normal(media_superior, desviacion_estandar, tamaño_muestras)
print(numeros)
plt.plot(numeros)
plt.show()