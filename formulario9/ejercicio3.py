#Obtener la cantidad de elementos mayores a 5 en la tupla.

def mayores_a_cinco(numeros):
    return numeros > 5

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
resultado = tuple(filter( mayores_a_cinco, tupla))
resultado = len(resultado)
print(resultado)