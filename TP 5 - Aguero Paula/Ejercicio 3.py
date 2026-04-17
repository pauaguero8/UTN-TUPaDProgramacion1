# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# Crear una lista con los pares y otra con los impares.
# Mostrar cuántos números tiene cada lista.

import random

numeros = []

for i in range(15):
    numeros.append(random.randint(1, 100))

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Números:")
for n in numeros:
    print(n)

print("Pares:")
for p in pares:
    print(p)
print("Cantidad:", len(pares))

print("Impares:")
for i in impares:
    print(i)
print("Cantidad:", len(impares))