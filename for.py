# for i in 1,2,3:
#     print(i)

# for i in range(5):
#     print(i)

# for i in ["eder", "nancy", "yos", "eme"]:
#     print(i)

#quita la M de la letra
# for i in ("Hola Mundo"):
#     if i == "M":
#         pass
#     else :
#         #print(i) #si se coloca solo i, imprime de forma vertical
#         #print(i, end=" ")#imprime de forma horizontal y con espacio de cada letra
#                            # ejemplo H o l a  u n d o
#         print(i, end="") #imprime sin espacios

#primir numeros primos de 2 al 100
# for i in range (2,50): #seleciona un rango de 2 al 100
#     primo = True # variable primo es verdadero
#     for j in range(2,i): #dentro del f i hay otro rango
#         if i == j:
#             break
#         elif i % j == 0:
#             primo = False
#         else :
#             continue
#     if primo == True:
#         print(i, end=" ")

mix = [0,1.0, "dos", 3+4j]
#for i in mix:
    #print(f"{i:6} -Tipo: {type(i)}")
    #print(len(mix)) # imprime la cantidad de elementos que hay
sin_dos =mix[:2] + mix[3:] # imprime los dos pirmeros datos + imp. los 
print(sin_dos)  
dupicado = mix * 2
print(dupicado, end=" ")  