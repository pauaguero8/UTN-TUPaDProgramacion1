# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

# Lunes (4)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Martes (3)
martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error. Ingrese un nombre sin espacios")
    operador = input("Nombre del operador: ")

opcion = 0

while opcion != 5:
    print("1) Reservar turno\n2) Cancelar turno\n3) Ver agenda\n4) Resumen\n5) Salir")

    opcion = input("Ingrese la opción: ")
    while not opcion.isdigit():
        print("Error. Ingrese una opción numérica")
        opcion = input("Ingrese la opción: ")

    opcion = int(opcion)

    # Reservar
    if opcion == 1:
        dia = input("Elija el día: 1) Lunes 2) Martes: ")
        while not dia.isdigit():
            print("Error. Ingrese una opción numérica")
            dia = input("Elija el día: 1) Lunes 2) Martes: ")

        dia = int(dia)

        nombre = input("Paciente: ")
        while not nombre.isalpha():
            print("Error. Ingrese un nombre sin espacios")
            nombre = input("Paciente: ")

        if dia == 1:
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Paciente ya tiene turno")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("Sin lugar")

        elif dia == 2:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Paciente ya tiene turno")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("Sin lugar")

    # Cancelar
    elif opcion == 2:
        dia = input("Elija el día: 1) Lunes 2) Martes: ")
        while not dia.isdigit():
            print("Error. Ingrese una opción numérica")
            dia = input("Elija el día: 1) Lunes 2) Martes: ")

        dia = int(dia)

        nombre = input("Paciente: ")
        while not nombre.isalpha():
            print("Error. Ingrese un nombre sin espacios")
            nombre = input("Paciente: ")

        encontrado = False

        if dia == 1:
            if lunes1 == nombre:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre:
                lunes4 = ""
                encontrado = True

        elif dia == 2:
            if martes1 == nombre:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre:
                martes3 = ""
                encontrado = True

        if not encontrado:
            print("Paciente no encontrado")

    # Ver agenda
    elif opcion == 3:
        dia = input("Elija el día: 1) Lunes 2) Martes: ")
        while not dia.isdigit():
            print("Error. Ingrese una opción numérica")
            dia = input("Elija el día: 1) Lunes 2) Martes: ")

        dia = int(dia)

        if dia == 1:
            print("Turno 1:", lunes1 or "(libre)")
            print("Turno 2:", lunes2 or "(libre)")
            print("Turno 3:", lunes3 or "(libre)")
            print("Turno 4:", lunes4 or "(libre)")

        elif dia == 2:
            print("Turno 1:", martes1 or "(libre)")
            print("Turno 2:", martes2 or "(libre)")
            print("Turno 3:", martes3 or "(libre)")

    # Resumen general
    elif opcion == 4:
        ocup_lunes = sum([lunes1!="", lunes2!="", lunes3!="", lunes4!=""])
        ocup_martes = sum([martes1!="", martes2!="", martes3!=""])

        print("Lunes:", ocup_lunes, "ocupados,", 4 - ocup_lunes, "libres")
        print("Martes:", ocup_martes, "ocupados,", 3 - ocup_martes, "libres")

        if ocup_lunes > ocup_martes:
            print("Día con más turnos: Lunes")
        elif ocup_martes > ocup_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate")
    
    elif opcion == 5:
        break