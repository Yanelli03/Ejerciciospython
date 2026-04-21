# Realizar un programa que defina un vector llamado "vector_numeros" de 10 enteros y a continuación lo inicialice con valores aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento del vector junto con su cuadrado y su cubo.

import random
numeros = []

for i in range(10):
    numeros.append(random.randint(1, 10))
for n in numeros:
    print(f'numero: {n}')
    print(f'Cuadrado: {n **2}')
    print(f'cubo: {n **3}')