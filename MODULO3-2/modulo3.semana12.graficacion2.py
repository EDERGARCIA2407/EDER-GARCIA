#generar un histograma

import numpy as np
import matplotlib.pyplot as plt

#genera 1000 muestras con una desviacion 0
datos = np.random.normal(0,1.0,1000)
#se genera la grafica histograma
plt.hist(datos)
plt.show()
