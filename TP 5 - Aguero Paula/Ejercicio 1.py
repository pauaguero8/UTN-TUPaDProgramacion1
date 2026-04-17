# 1) Crear una lista con las notas de 10 estudiantes.
# Mostrar la lista completa.
# Calcular y mostrar el promedio.
# Indicar la nota más alta y la más baja.

notas = [6, 7, 8, 5, 9, 4, 10, 6, 7, 8]

print("Lista de notas:")
for n in notas:
    print(n)

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))