import random


def adivina_el_numero(x):

    print("=====================")
    print(" ¡Bienvenido al Juego! ")
    print("=====================")
    print("Tu meta es adivinar el numero aleatorio")

    numero_aleatorio = random.randint(1, x) #numero aleatorio entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatorio:
        # El usuario ingresa un numero
        prediccion = int(input(f"Ingresa un numero entre 1 y ¨{x}: "))    #f-string

        if prediccion < numero_aleatorio:
            print("intenta de nuevo, este numero es pequeño")
        elif prediccion > numero_aleatorio:
            print("intenta otra vez, este numero es grande")

    print(f"adivinaste el numero {numero_aleatorio} correctamente")


adivina_el_numero(10)