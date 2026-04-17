# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# Mostrar la lista final actualizada.

estudiantes = ["Ana", "Luis", "Pedro", "Marta", "Lautaro", "Juan", "Camila", "Diego"]

print("Lista inicial:")
for i in range(len(estudiantes)):
    print(estudiantes[i])

opcion = input("Elija una opción 1) Agregar 2) Eliminar: ")

if opcion == "1":
    nuevo = input("Nombre: ")
    estudiantes.append(nuevo)
elif opcion == "2":
    borrar = input("Nombre: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)

print("Lista final:")
for e in estudiantes:
    print(e)