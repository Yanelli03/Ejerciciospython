# Programa que declare tres vectores 'vector1', 'vector2' y 'vector3' de cinco 
# enteros cada uno, pida valores para 'vector1' y 'vector2' y calcule 
# vector3=vector1+vector2.

vector1 = [0] * 5
vector2 = [0] * 5
vector3 = [0] * 5
tam_vector = 5

for indice in range(tam_vector):
    vector1[indice] = int(input(f"Introduce el elemento {indice+1} del vector 1: "))

for indice in range(tam_vector):
    vector2[indice] = int(input(f"Introduce el elemento {indice+1} del vector 2: "))

for indice in range(tam_vector):
    vector3[indice] = int(input(f"Introduce el elemento {indice+1} del vector 3: "))

print("La suma de los vectores es:")
for indice in range(tam_vector):
    print(vector3[indice])