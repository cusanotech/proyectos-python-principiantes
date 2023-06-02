'''
   # Consisten en pedirle al usuario que adivine 
  un número elegido aleatoriamente por el programa.

   # El objetivo es que el usuario (quien dara el input) adivine correctamente el número 
  (elegido aleatoriamente por el programa) en la menor cantidad de intentos posible.
  
   # El programa establece un rango de números posibles y 
  elige aleatoriamente un número dentro de ese rango.

   # Luego, el programa le pide al usuario que adivine el número
  y le da una pista sobre si el número a adivinar es mayor o menor que el número
  que el usuario ha ingresado. De esta manera, el usuario puede ajustar sus conjeturas para acercarse al número correcto.
  
   # El juego continúa hasta que el usuario adivine el número correcto, 
  momento en el que el programa le da una felicitación y le muestra 
  el número de intentos que le tomó adivinar el número.
  
'''

import random

print("\t#### ADIVINA EL NUMERO ####")

print("Este juego consiste en que adivines el número que el programa escogió. Ten en cuenta que el número estará entre 0 y 100. ¡Buena suerte!")

numero = random.randint(0, 100)
adivinado = False


while not adivinado:    # Mientras adivinado sea falso continue si no break
    try:
        
        numero_usuario = int(input("Ingresa un número: "))
        if 0 <= numero_usuario <= 100:  
            if numero_usuario == numero:
                adivinado = True
            elif numero_usuario > numero:
                print("Más bajo")
            else:
                print("Más alto")
        else:
            print("Ingresa un número entre 0 y 100.")
            
    except ValueError:  #notificamos el error de valor ingreso por el usuario y que continue con sus intentos
        print("Estás ingresando algo incorrecto. Por favor, ingresa un número entero.")
        

print("¡Has adivinado el número! ¡Felicitaciones!") 

