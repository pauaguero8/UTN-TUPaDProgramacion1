# Actividades
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f...) para
# realizar la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f...) para realizar
# la impresión por pantalla.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

import math

radio = float(input("Ingrese el radio del circulo: "))
area = math.pi * (radio**2)
perimetro = 2 * math.pi * radio

print(f"El area del circulo es de {area} y su perimetro de {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos/3600
print(f"{segundos} equivalen a {horas} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero*i}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero_1 = int(input("Ingrese un número entero distinto de 0: "))
numero_2 = int(input("Ingrese otro número entero distinto de 0: "))
suma = numero_1 + numero_2
division = numero_1/numero_2
multiplicacion = numero_1*numero_2
resta = numero_1 - numero_2

print(f"Suma = {suma}\nDivisión = {division}\nMultiplicación = {multiplicacion}\nResta = {resta}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:

# IMC = peso en kg / ((altura en m)**2)

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso/(altura**2)

print(f"Su IMC es de {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

# Temperatura en Fahrenheit = (9/5 * Temperatura en Celsius) + 32

temperatura = float(input("Ingrese la temperatura en °C: "))
temperatura_fahrenheit = (9/5 * temperatura) + 32

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

promedio = (a + b + c)/3

print(f"El promedio de los 3 números es de {promedio}")