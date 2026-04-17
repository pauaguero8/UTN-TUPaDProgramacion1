# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# Inicializarlo con guiones "-" representando casillas vacías.
# Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# Mostrar el tablero después de cada jugada.

tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

for turno in range(9):
    fila = int(input("Fila: "))
    col = int(input("Columna: "))

    while not tablero[fila][col] == "-":
        print("Espacio ya ocupado. Selecione otro.")
        fila = int(input("Fila: "))
        col = int(input("Columna: "))
    
    letra = input("Ingrese X u O según corresponda: ")
    
    tablero[fila][col] = letra

    print("Tablero:")

    for f in tablero:
        for c in f:
            print(c, end=" ")
        print()