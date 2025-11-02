#modulo m_factoria(m_factorial2.py)

""" modulo que contiene la funcion recursiva del factorial"""

def factorial(num):
    """ calcular el factorial de un numero"""
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)
print(__name__)

if __name__ == "__main__":
    import sys
    print(factorial(int(sys.argv[1])))
