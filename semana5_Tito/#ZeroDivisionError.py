#ZeroDivisionError
#3w
#espinoza hernandez dylan abraham

try:
    
    nombre = input("Ingresa tu nombre: ")
    
    saludo = "Hola " - nombre 
    
    print(saludo)

except TypeError:
    print("Error: No puedes restar cadenas de texto. ¡Revisa la operación matemática!")
