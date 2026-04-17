# 2) Pedir al usuario que cargue 5 productos en una lista.
# Mostrar la lista ordenada alfabéticamente.
# Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(5):
    prod = input(f"Ingrese un producto n° {i+1}: ")
    productos.append(prod)

ordenados = sorted(productos)

print("Lista ordenada:")
for p in ordenados:
    print(p)

eliminar = input("¿Qué producto desea eliminar? ")
if eliminar in productos:
    productos.remove(eliminar)
else:
    print("No está en la lista")

print("Lista actualizada:")
for p in productos:
    print(p)