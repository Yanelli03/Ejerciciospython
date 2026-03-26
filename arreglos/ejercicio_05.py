# Hacer un programa que inicialice un vector de números con valores aleatorios, 
# y posterior ordene los elementos de menor a mayor.

vector = [0] * 10
tam_vector = 10

import random
for indice in range(tam_vector):
    vector[indice] = random.randint(1, 10)

while True:
    cambios = 0

    for indice in range(tam_vector - 1):
        if vector[indice] > vector[indice + 1]:
            aux = vector[indice]
            vector[indice] = vector[indice + 1]
            vector[indice + 1] = aux
            cambios += 1
    if cambios == 0:
        break


for indice in range(tam_vector):
    print(vector[indice])