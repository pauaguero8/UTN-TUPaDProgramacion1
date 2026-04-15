# TP integrador – Repetitivas- Condicionales y
# Secuenciales.
# Ejercicio 1— “Caja del Kiosco”

total_sin_descuento = 0
total_con_descuento = 0
ahorro_total = 0

nombre = input("Ingrese su nombre sin espacios: ")

while not (nombre.isalpha() and nombre.strip()):
    print("Nombre inválido")
    nombre = input("Ingrese su nombre sin espacios: ")

productos = int(input("Ingrese la cantidad de productos a comprar: "))
    
while not (productos > 0 or productos.isdigit()):
    print("Cantidad de productos inválido")
    productos = int(input("Ingrese la cantidad de productos a comprar: "))

for i in range(productos):
    precio = int(input(f"Ingresar precio del producto n° {i+1}: "))
    descuento = input("¿Tiene descuento? S: Si/N: No: ")

    while not (descuento in ["S", "N", "s", "n"]):
        print("Error. Ingrese una opción correcta")
        descuento = input("¿Tiene descuento? S: Si/N: No: ")

    total_sin_descuento += precio

    if (descuento == "S" or descuento == "s"):
        total_con_descuento += precio*0.90
        ahorro_total += precio*0.10
    else:
        total_con_descuento += precio
    
    print(f"Producto {i+1} - Precio: {precio} Descuento (S/N): {descuento}")

promedio = total_con_descuento/productos

print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {productos}")
print(f"Total sin descuentos: {total_sin_descuento}")
print(f"Total con descuentos: {total_con_descuento:.2f}")
print(f"Ahorro: {ahorro_total:.2f}")
print(f"Promedio por producto: {promedio:.2f}")