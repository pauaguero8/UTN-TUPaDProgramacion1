# 7) Crear una matriz (lista anidada) de 7x2 con temperaturas mínimas y máximas.
# Calcular el promedio de las mínimas y máximas.
# Mostrar en qué día se registró la mayor amplitud térmica.

temps = [
    [10, 20],
    [12, 22],
    [8, 18],
    [9, 19],
    [11, 21],
    [7, 17],
    [13, 23]
]

suma_min = 0
suma_max = 0

for t in temps:
    suma_min += t[0]
    suma_max += t[1]

print("Promedio mínimas:", suma_min / 7)
print("Promedio máximas:", suma_max / 7)

mayor_amp = 0
dia = 0

for i in range(7):
    amp = temps[i][1] - temps[i][0]
    if amp > mayor_amp:
        mayor_amp = amp
        dia = i + 1

print("Mayor amplitud en día:", dia)