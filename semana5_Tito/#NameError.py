#NameError
#3w
#espinoza hernnandez dt¿ylan abrahgam


try:
    respuesta = input("¿Quieres ver el mensaje secreto? (escribe 'si'): ")

    if respuesta == "SI":
        mensaje = "¡Hola! Este es el mensaje secreto."
        print(mensaje)  


except NameError:
    print("Error: Intentaste acceder a una variable que no existe en el programa.")
