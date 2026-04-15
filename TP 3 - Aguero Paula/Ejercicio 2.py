#Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
clave_correcta = "python123"

intento = 1
intento_fallido = 0

while intento < 4:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    print(f"Intento {intento}/3 - Usuario: {usuario}")
    print(f"Clave: {clave}")

    if (usuario == usuario_correcto and clave == clave_correcta):
        print("Acceso concedido.")
        break
    else:
        print("Error: credenciales inválidas.")
        intento_fallido += 1

    intento += 1
    
if (intento_fallido == 3):
    print("Cuenta bloqueada.")
else:
    opcion = 0

    while opcion != 4:
        print(f"1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")

        while not (opcion.isdigit()):
            print("Error: ingrese un número válido.")
            opcion = int(input("Opción: "))
            if (opcion < 0 and opcion > 4):
                print("Error: opción fuera de rango.")
                opcion = input("Opción: ")

        opcion = int(opcion)

        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            nueva_clave = input("Ingrese la nueva clave: ")
            confirmacion_nueva_clave = input("Repita la nueva clave: ")
            if (nueva_clave == confirmacion_nueva_clave):
                if (len(nueva_clave) > 6):
                    clave_correcta = nueva_clave
                    print("Clave modificada.")
                else:
                    print("Error: mínimo 6 caracteres")
            else:
                print("Las claves no coinciden")

        elif opcion == 3:
            print("¡Vos podes!")