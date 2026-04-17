# 4) Dada una lista con valores repetidos:
# Crear una nueva lista sin elementos repetidos.
# Mostrar el resultado.

lista = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

for n in lista:
    if n not in sin_repetidos:
        sin_repetidos.append(n)

print("Lista sin repetidos:")
for n in sin_repetidos:
    print(n)