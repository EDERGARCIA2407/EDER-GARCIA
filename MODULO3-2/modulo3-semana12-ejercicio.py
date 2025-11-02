#mostrar todas las calificaciones de un alumno en una grafica de barras

#definir una funcion para contruir la grafica
#definir un diccionario con las calificaciones del alumno
#pedir el nombre del alumno
#mandar llamar a la grafica y mostrar

import matplotlib.pyplot as plt

def diagrama_barras_calificaciones(notas, color, alumno):
    """ 
    Dibujar la grafica de barras con las calificaciones
    """
    plt.bar(notas.keys(), notas.values(), color=color)
    plt.title("Calificaciones de : " + alumno)
#definir direccionario para el alumno
calificaciones = {
    'Programación': 9,
    'Español': 6.5,
    "Calculo": 4,
    "Historia": 8,
    "Biología": 10,
    "ingles": 8

}
#llama la funcion para mostrar la grafica

alumno = input("nombre del alumno: ")
diagrama_barras_calificaciones(calificaciones, 'red', alumno)
plt.show()

