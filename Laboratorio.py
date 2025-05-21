def imprimir_tablero(matriz):
    for fila in matriz:
        print(" ".join(str(celda) for celda in fila))
    print() 

def contar_vecinos(fila, columna, matriz):
    vecinos = 0
    
    if columna > 0:
        vecinos += matriz[fila][columna - 1]

    if columna < len(matriz[0]) - 1:
        vecinos += matriz[fila][columna + 1]
    return vecinos

def siguiente_generacion(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    nueva = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos(i, j, matriz)
            if matriz[i][j] == 1:
                if vecinos == 1 or vecinos == 2:
                    nueva[i][j] = 1  
                else:
                    nueva[i][j] = 0  
            else:
                if vecinos == 1:
                    nueva[i][j] = 1  
                else:
                    nueva[i][j] = 0  
    return nueva

matriz = [
    [0,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
]


print("Generación 0:")
imprimir_tablero(matriz)

generacion_1 = siguiente_generacion(matriz)
print("Generación 1:")
imprimir_tablero(generacion_1)

generacion_2 = siguiente_generacion(generacion_1)
print("Generación 2:")
imprimir_tablero(generacion_2)
