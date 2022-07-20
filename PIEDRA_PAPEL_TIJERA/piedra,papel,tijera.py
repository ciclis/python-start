from random import randrange, choice

while True:

 print("Bienvenido al Jego de Piedra Papel Tijera")

 print("elige una opcion: 1) PIEDRA  2) PAPEL 3) TIJERA")
 eligio=input("-Selecciona algo :")

 if eligio=="1":
    print("PAPEL")
 elif eligio=="2":
    print(" TIJERA")
 elif eligio=="3":
    print("PIEDRA")
 else:
    print("Opción no válida")

 print("te ha ganado una maquina sucio humano, jajaja2")

 jugar_denuevo = input("Quieres jugar de nuevo (s/n): ")
 if jugar_denuevo.lower() != "s":
     break