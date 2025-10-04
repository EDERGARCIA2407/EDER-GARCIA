#RETO SEMANA 5
#VARIABLE PARA AÑO ACTUAL 
a_actual = int(input("Introduce el año actual: "))
#VARIABLE PARA OTRO AÑO
a_otro = int(input("Introduce otro año para calcular: "))
#OPERACION DE LOS AÑOS INTRODUCCIDOS POR EL USUARIO
resultado =  a_otro - a_actual
#CONDICIONES
#SI EL RESULTADO DE LA OPERACION ES MAYOR QUE 0
if resultado > 0:
#IMPRIME EL AÑO     
    print(f"Falta {resultado} años para llegar al año que has introduccido")
#SEGUNDA CONDICION SI AÑO ACTUAL = QUE OTRO
elif a_actual == a_otro:
#IMPRIME 
    print(f"Has indroduccido el mismo año que el actual")
#IMPRIME EL RESULTADO
    print(f"Para llegar {a_otro} faltan {resultado} años ")
