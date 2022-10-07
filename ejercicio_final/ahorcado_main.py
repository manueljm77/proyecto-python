# se importan los archivos internos 
import random
import ahorcado_palabras  as Listas_palabras
import ahorcado_dibujos  as Ahorcado

# se elige las palasbras de la lista al azar 
random =random.choice(Listas_palabras.Listas_palabras)
vacio =[]
lista_elegida =[]
for i in range(0 ,len(random ) ):
    lista_elegida.extend(random[i])

for i in range(0 ,len(random)):
    vacio.append("_")
    
    
   # se  imprime nombre y bienvenida del juego 
print (Ahorcado)
print("juego ahorcado bienvenido!!\n")
print(vacio)


# print(random_word)
# print(lista elegida)

vidas =len(random) #  se da el numero de  vidas dependiendo cuantas letras tenga la palabra 
print(f"tus vidas : {vidas}")

# se itera la lista hasta salir ciclo hasta que acabe el juego 
                
while vidas>0 :
    
    adivina=input("adivina una letra\n")
    
    for  i in range (0,len(random)):
        
        

        if adivina == lista_elegida[i]:
            vacio[i] = adivina
            print(vacio)
            
            
        
        elif not lista_elegida.__contains__(adivina) :
            vidas-=1
            try:
                print(Ahorcado.Ahorcado[vidas])
            except IndexError:
                print("fuera de rango")
                

            print(f"estas perdiendo 1 vida, quedan : {vidas}")
                     
            
            
            
            # se termina de iterar 
            break
         # se declara la accion con un booleano si es cierto o falso 
    if not vacio.__contains__("_"):
        
        print("Ganaste,¡Tienes buen OJO! ")
        print (exit(0))
    
       
     
        








            
        
        
        
            
            
            
            
        
    
    





