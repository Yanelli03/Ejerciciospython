# Programa que declare un vector de diez elementos enteros y pida números para 
# rellenarlo hasta que se llene el vector o se introduzca un número negativo. 
# Entonces se debe imprimir el vector (sólo los elementos introducidos).

vector = [0] * 10
indice = 0
tam_vector = 10

while True:
    vector[indice] = int(input(f"Introduce un nmero en el vector. Numero {indice+1}: "))
    indice = indice + 1
    if indice == tam_vector or vector[indice-1]<0:
        break

indice = 0
print("Elementos del vector: ")
while indice < tam_vector-1 and vector[indice]>=0:
    print(vector[indice])
    indice = indice + 1