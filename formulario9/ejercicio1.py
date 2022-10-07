import random
aciertos = 0
for indice in range(10):
	
    num1 = random.randint(2,10)
    num2 = random.randint(2,10)
	
    resultado = num1*num2
	
	
    print("Multiplicación ",indice)
    print(num1," * ",num2," = ")
    num_usuario = int(input())

    if num_usuario == resultado:
        aciertos = aciertos+1
    else:
        
        print("No has acertado. La respuesta es ",resultado)
    
    print("Tu nota ha sido: ",aciertos)

