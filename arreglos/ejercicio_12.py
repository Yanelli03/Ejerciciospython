# Diseñar el algoritmo correspondiente a un programa, que:
# * Crea una tabla bidimensional de longitud 5x15 y nombre 'marco'.
# * Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, 
num_filas = 5
num_cols = 15
matriz = [[0.0] * 15 for _ in range(5)]

for fila in range(num_filas):
    for col in range(num_cols):
        if fila == 0 or fila ==num_filas-1 or col == 0 or col == num_cols-1:
            matriz[fila][col] = 1
        else:
            matriz[fila][col] = 0
for fila in range(num_filas):
    for col in range(num_cols):
        print(matriz[fila][col])
    print('')