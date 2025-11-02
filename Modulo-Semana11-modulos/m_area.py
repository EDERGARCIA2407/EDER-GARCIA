#Modulo m_area(m_area.py)

""" Modulo que contiene la funcion area"""

def area(**dato):
    """ Recibe como parametro un diccionario con los datos de una figura
        calcula el area de la figura
    """
    if dato["figura"] == "Rectangulo":
        return dato["base"]*dato["altura"]
    elif dato["figura"] == "triangulo":
        return dato["base"]*dato["altura"]/2
    elif dato["figura"] == "circulo":
        return 3.141593 * dato["radio"]**2
    else:
        print("firgura desconocida")
