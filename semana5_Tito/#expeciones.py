#expeciones.py
while True:
    try:
    
        edad = int(input("ingresa tu edad:"))
        print(" tu edad es", edad)

    except ValueError:
        print("error informacion invalida")
        
    

        print("fin del programa")
        break
    