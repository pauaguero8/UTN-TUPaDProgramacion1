# 11) Crear una lista con los nombres de 10 estudiantes.
# Solicitar al usuario que ingrese un nombre a buscar.
# Indicar si el nombre se encuentra en la lista.
# Mostrar la posición en la que aparece.
# Si no se encuentra, informar que no está en la lista.

nombres = ["Pedro", "Pablo", "Carla", "Julieta", "Juan", "Francisco", "Silvia", "Nicolas", "Carlos", "Elena"]

print("Estudiantes:")
for i in range(len(nombres)):
    print(nombres[i])

buscar = input("Nombre: ")

encontrado = False

for i in range(len(nombres)):
    if nombres[i] == buscar:
        print("Está en la posición:", i)
        encontrado = True

if not encontrado:
    print("No está en la lista")