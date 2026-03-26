# Diseñar el algoritmo correspondiente a un programa, que:
#  * Crea una tabla bidimensional de longitud 5x5 y nombre 'matriz'.
#  * Carga la tabla con valores numéricos enteros.
#  * Suma todos los elementos de cada fila y todos los elementos de cada columna 
# visualizando los resultados en pantalla. 

matriz = [[0.0] * 5 for _ in range(5)]
num_filas = 5
num_cols = 5

for fila in range(num_cols):
    for col in range(num_cols):
        matriz[fila][col] = int(input(f"Introduce el numero de la fila {fila+1} y columna {col+1}: "))

for fila in range(num_filas):
    suma = 0
    for col in range(num_cols):
        suma = suma + matriz[fila][col]
    print(f"La suma de los elementos de la fila {fila+1} es {suma}")

for col in range(num_cols):
    suma = 0
    for fila in range(num_filas):
        suma = suma + matriz[fila][col]
    print(f"La suma de los elementos de la columna {col+1} es {suma}")
