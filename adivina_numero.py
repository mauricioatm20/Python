import random

def adivina_el_numero(x):
    print("=======");
    print("welcom");
    print ("=======");
    print("adivina el numero");
    
    numero_aleatorio= random.randint(1,x)
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        #el usuario introduce el numero 
        prediccion = int(input(f"adivina un numero entre 1 y {x}:"))
        if prediccion < numero_aleatorio:
            print("intenta otra vez numero pequeño")
        elif prediccion > numero_aleatorio:
            print("intenta otra vez numero grande")
            
    print (f"felicidades has acertado {numero_aleatorio}")
    
adivina_el_numero(10)  