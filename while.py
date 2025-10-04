# print("imprimir menores a 10")

# x = 1

# while x <= 10:
#     print(x)
#     x += 5

# factorial = 5
# contador = factorial - 1
# while contador > 0:
#     factorial *= contador
#     contador -= 1
# print(f"EL FACTORIA DE 5 ES: {contador}")

#for i in 1,2,3:
 #   print(i)

#se usa range para imprimir todos los numero 
# for i in range(4):
#     print(i)
# #se puede impirmir una lista 
# for i in ("eder", "gil"):
#     print(i)
#
# for i in ("hola Mundo"):
# if i == "M":
#     pass 

# else:
#     print(i,end="")

for i in range(2,100):
    primo = True
    for j in range(2,i):
        if i ==j:
            break
        elif 1 % j == 0:
            primo == False
        else: 
            continue
    if primo == True:
        print (1, end = "")
        