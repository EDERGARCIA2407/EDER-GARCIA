import random

def tiro_dado(num_tiros):
    for dado in range(num_tiros):
        print("el dado " + str(dado +1) + "dió: " + str(random.randint(1,6)))
tiro_dado(6)



#print("El dado dio:" + str (random.randint(1,6)))#limite superior y limite inferior

