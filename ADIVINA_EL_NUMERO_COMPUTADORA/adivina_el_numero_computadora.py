import random

def adivina_el_numero_computadora(x):

    print("=====================")
    print(" ¡Bienvenido al Juego! ")
    print("=====================")
    print(f"Selecciona un numero entre 1 y {x} para que la computadora intente adivinarlo")

    limite_inferios = 1
    limite_superior = x
    
    respuesta = ""
    while respuesta != "c":
    # Generar prediccion
        if limite_inferios != limite_superior:
            prediccion = random.randint(limite_inferios, limite_superior)
        else:
            prediccion = limite_inferios #tambien podria ser el superior

    # obtener respuesta usuario
    respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta ingresa ()").lower()

    if respuesta == "a":                                 
        limite_superior = prediccion -1
    elif respuesta == "b":
        limite_inferios = prediccion + 1
    print (f"la cpc lo a adivinado: {prediccion}")


# Intervalo inicial: [1, 10]    
# Prediccion: 6
# Respuesta "a"
# Intervalo: [1, 5]