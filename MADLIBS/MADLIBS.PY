# unir cadenas de caracteres
# supongamos que queremos crear una cadena k diga:
# aprende a programar con _______

#   organizacion = "freeCodeCamp"

#   print("Aprende a programar con " + organizacion)
#   print("Aprende a programar con {}".format(organizacion))
#   print(f"Aprende a programar con {organizacion}")  #f-string

#MAD LIBS

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")


madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1}. ¡Aprende a programar con freeCodeCamp y alcanza tus {sustantivo_plural}"

print(madlib)