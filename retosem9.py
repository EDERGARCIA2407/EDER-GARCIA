#El programa que desarrollarás debe tener las siguientes características: 
#1. Que en un bucle infinito solicite al usuario una letra (debes especificar 
#al usuario la condición para terminar el programa. Por ejemplo, para |
#salir, escriba alto, presione 0 o cualquier otra que se te ocurra).
# 2. Harás una función que imprima en la pantalla la letra siguiente en el 
#alfabeto y la letra anterior a la ingresada.
# 3. El programa debe continuar en el bucle hasta que el usuario decida 
#salir del programa

def letras_antes_despues(letra):
    #La función ord() en Python toma un solo caráctery devuelve su código Unicode, 
    #que es un número entero que representa ese carácter en el estándar Unicode.
    num_letra = ord(letra)
    #Convierte el número anterior al código Unicode de la letra en su carácter correspondiente
    #La función chr() convierte un número entero en su carácter Unicode equivalente.
    anterior= chr(num_letra - 1 )  
    #Convierte el número anterior al código Unicode de la letra en su carácter correspondiente
    siguiente =chr(num_letra + 1) 
    print(f">>Letra Ingresada: {letra}") # se imprime la letra ingresada
    print(f">>>Letra Anterior es: {anterior}") # se imprime la letra siguiente
    print(f">>>>Letra Siguiente es: {siguiente}") # se imprime la eltra anterior
    

print("Escribe una letra para ver la anterior y la siguiente en el alfabeto")
print("Para salir del programas escribe - 'salir'")

while True:#     #se hace un bucle
    letra = input("Ingresa letra: ") #se solicita la letra
    if letra.lower() == 'salir': #si se escribe salir, se sale del bucle
        print("///Fin de programa///")
        break
    letras_antes_despues(letra)#se le llama a la función





# def letra_antes_despues(letra):
#     if len(letra) != 1 or not letra.isalpha():
#         print("❌ Entrada inválida. Por favor, ingresa solo una letra.")
#         return

#     codigo = ord(letra)
#     anterior = chr(codigo - 1) if letra.lower() != 'a' else 'No hay anterior'
#     siguiente = chr(codigo + 1) if letra.lower() != 'z' else 'No hay siguiente'

#     print(f"🔠 Letra ingresada: {letra}")
#     print(f"⬅️ Letra anterior: {anterior}")
#     print(f"➡️ Letra siguiente: {siguiente}")

# print("📌 Escribe una letra para ver la anterior y la siguiente en el alfabeto.")
# print("🛑 Para salir, escribe 'salir'.")

# while True:
#     entrada = input("👉 Ingresa una letra: ")
#     if entrada.lower() == 'salir':
#         print("👋 Programa finalizado. ¡Hasta luego!")
#         break
#     letra_antes_despues(entrada)
