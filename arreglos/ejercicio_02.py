# Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

tam_vector = 5
vector1 = [''] * 5
vector2 = [''] * 5

for indicador in range(tam_vector):
    vector1[indicador] = input(f'Dame la cadena {indicador + 1}: ')
for i in range(tam_vector):
    vector2[i] = vector1[tam_vector - 1 - i]

print('Vector invertido:')
for i in range(tam_vector):
    print(f'La cadena {i + 1}: {vector2[i]}')