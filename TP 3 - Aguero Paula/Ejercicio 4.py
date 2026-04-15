# Ejercicio 4 — “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

nombre_agente = input("\nIngrese su nombre de agente: ")
while not nombre_agente.isalpha():
    print("Error: solo se permiten letras.")
    nombre_agente = input("Ingrese su nombre de agente: ")

print(f"\nBienvenido/a, Agente {nombre_agente}. ¡Buena suerte!")

juego_activo = True

while juego_activo:
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nSISTEMA BLOQUEADO: alarma activa con tiempo crítico.")
        print("DERROTA (bloqueo). La bóveda quedó sellada.")
        juego_activo = False
        break

    if cerraduras_abiertas == 3:
        print(f"\n¡VICTORIA! Las 3 cerraduras fueron abiertas, Agente {nombre_agente}.")
        juego_activo = False
        break
    if energia <= 0:
        print("\nDERROTA: te quedaste sin energía.")
        juego_activo = False
        break
    if tiempo <= 0:
        print("\nDERROTA: se acabó el tiempo.")
        juego_activo = False
        break

    print(f"\n--- Estado | Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'} ---")
    print("1) Forzar cerradura (-20 energía, -2 tiempo)")
    print("2) Hackear panel    (-10 energía, -3 tiempo)")
    print("3) Descansar        (+15 energía, -1 tiempo)")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: ingrese 1, 2 o 3.")
        opcion = input("Opción: ")
    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar >= 3:
            print("La cerradura se trabó por el uso excesivo. ¡Alarma activada!")
            alarma = True
            racha_forzar = 0
        else:
            if energia < 40:
                print("Energía baja: riesgo de alarma.")
                num_str = input("Ingrese un número del 1 al 3: ")
                while not num_str.isdigit() or int(num_str) < 1 or int(num_str) > 3:
                    print("Error: ingrese un número entre 1 y 3.")
                    num_str = input("Ingrese un número del 1 al 3: ")
                if int(num_str) == 3:
                    alarma = True
                    print("¡La alarma se activó!")
                else:
                    cerraduras_abiertas += 1
                    print(f"Cerradura forzada. Cerraduras abiertas: {cerraduras_abiertas}/3.")
            else:
                cerraduras_abiertas += 1
                print(f"Cerradura forzada. Cerraduras abiertas: {cerraduras_abiertas}/3.")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0
        print("Hackeando panel...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"  Paso {paso}/4 - Código parcial: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"¡Código completo! Cerradura abierta. Cerraduras abiertas: {cerraduras_abiertas}/3.")

    elif opcion == 3:
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
            print("Alarma activa: se pierden 10 puntos de energía extra durante el descanso.")
        print(f"Descansaste. Energía actual: {energia}.")