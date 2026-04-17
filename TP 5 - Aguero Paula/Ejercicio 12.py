# 12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista
# Mostrar la lista original.
# Mostrar la lista ordenada de menor a mayor.
# Mostrar la lista ordenada de mayor a menor.
# Investigar el uso de sorted() y del parámetro reverse.

nums = []

for i in range(8):
    nums.append(int(input(f"Ingrese el número {i+1} de la lista: ")))

print("Original:")
for n in nums:
    print(n)

asc = sorted(nums)
print("Ordenada:")
for n in asc:
    print(n)

desc = sorted(nums, reverse=True)
print("Descendente:")
for n in desc:
    print(n)