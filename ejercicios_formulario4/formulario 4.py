import random
numeros_lista=[]
for lista in range(1,11):
    numeros_lista.append(random.randint(1,10))
    for numero in numeros_lista:
        print(numero," + ",numero**2," + ",numero**3)
    


