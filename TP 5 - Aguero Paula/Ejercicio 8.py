# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# Mostrar el promedio de cada estudiante.
# Mostrar el promedio de cada materia.

notas = [
    [6, 7, 8],
    [5, 6, 7],
    [9, 8, 10],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(5):
    suma = 0
    for j in range(3):
        suma += notas[i][j]
    print(f"Promedio estudiante {i+1}: {suma / 3}")

for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas[i][j]
    print(f"Promedio materia {j+1}: {suma / 5}")