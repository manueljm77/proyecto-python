import math
t = int(input('Cuántos primos quieres?: '))
p = 1   #contador de primos encontrados
c = 3   #se evalúan desde 3 en adelante
r = '2' #cadena con el primer resulatdo listo
while p < t:
    fact1 = math.factorial(c-1)
    if fact1 % c == c-1:
        r = r + ',' + str(c)
        p += 1  #se ha encontrado otro primo
    c += 1      #probar con siguiente entero
print(r)        #mostrar resultados almacenados en r