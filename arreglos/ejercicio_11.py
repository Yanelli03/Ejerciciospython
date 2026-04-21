# Diseñar el algoritmo correspondiente a un programa, que:
# * Crea una tabla bidimensional de longitud 5x5 y nombre 'diagonal'.
# * Carga la tabla de forma que los componentes pertenecientes a la diagonal de la 
num_filas = 5
num_cols = 5
matriz = [[0.0] * 5 for _ in range(5)]

for fila in range(num_filas):
    for col in range(num_cols):
        if fila==col or fila==(num_filas-1)-col:
            matriz[fila][col] = 1
        else:
            matriz[fila][col] = 0
for fila in range(num_filas):
    for col in range(num_cols):
        print(matriz[fila][col])
    print('')