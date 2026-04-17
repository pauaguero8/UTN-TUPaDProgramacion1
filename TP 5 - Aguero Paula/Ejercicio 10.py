# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# Mostrar el total vendido por cada producto.
# Mostrar el día con mayores ventas totales.
# Indicar cuál fue el producto más vendido en la semana.

import random

ventas = []

for i in range(4):
    fila = []
    for j in range(7):
        fila.append(random.randint(10, 100))
    ventas.append(fila)

for i in range(4):
    print(f"Producto n° {i+1}: ", end="")
    for j in range(7):
        print(ventas[i][j], end=" ")
    print()

for i in range(4):
    total = 0
    for j in range(7):
        total += ventas[i][j]
    print(f"Total producto {i+1}: {total}")

mayor = 0
dia = 0

for j in range(7):
    total = 0
    for i in range(4):
        total += ventas[i][j]
    if total > mayor:
        mayor = total
        dia = j + 1

print("Día con más ventas:", dia)

mayor = 0
prod = 0

for i in range(4):
    total = 0
    for j in range(7):
        total += ventas[i][j]
    if total > mayor:
        mayor = total
        prod = i + 1

print("Producto más vendido:", prod)