# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

lista = [1, 2, 3, 4, 5, 6, 7]

ultimo = lista[-1]

for i in range(len(lista)-1, 0, -1):
    lista[i] = lista[i-1]
lista[0] = ultimo

print("Lista rotada:")
for n in lista:
    print(n)