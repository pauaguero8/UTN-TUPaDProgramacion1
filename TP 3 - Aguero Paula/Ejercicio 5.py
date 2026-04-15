# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

print("\n--- BIENVENIDO A LA ARENA ---")
nombre_gladiador = input("Nombre del Gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print(f"\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre_gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        if not opcion.isdigit():
            print("Error: Ingrese un número válido.")
        else:
            print("Error: opción fuera de rango. Ingrese 1, 2 o 3.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    if opcion == 1:
        if vida_enemigo < 20:
            danio_final = danio_pesado * 1.5
            print(f"¡GOLPE CRÍTICO! Atacaste al enemigo por {danio_final} puntos de daño!")
        else:
            danio_final = float(danio_pesado)
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")
        vida_enemigo -= int(danio_final)

    elif opcion == 2:
        print(">> ¡Iniciás una ráfaga de golpes!")
        for _ in range(3):
            vida_enemigo -= 5
            print("  > Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones -= 1
            print(f"¡Usaste una poción! HP actual: {vida_jugador}. Pociones restantes: {pociones}.")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

    if vida_jugador > 0 and vida_enemigo > 0:
        print("=== NUEVO TURNO ===")

if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")