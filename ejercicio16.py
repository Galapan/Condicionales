# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta

jugador1 = input("Jugador 1, elija piedra, papel o tijera: ")
jugador2 = input("Jugador 2, elija piedra, papel o tijera: ")

opciones_validas = ["piedra", "papel", "tijera"]

if jugador1 not in opciones_validas or jugador2 not in opciones_validas:
    print("Opción incorrecta.")
else:
    if jugador1 == jugador2:
        print("Empate")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or \
         (jugador1 == "tijera" and jugador2 == "papel") or \
         (jugador1 == "papel" and jugador2 == "piedra"):
        print("Gana Jugador 1")
    else:
        print("Gana Jugador 2")

