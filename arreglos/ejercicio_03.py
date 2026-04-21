# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.
tam_notas = 5
notas = [0] * 5

for indice in range(tam_notas):
    while True:
        nota = int(input(f'Introduce la nota {indice+1}: '))
        if 0 <= nota <= 10:
            notas[indice] = nota
            break

nota_max = notas[0]
nota_min = notas[0]
suma = 0

for indice in range(tam_notas):
    suma += notas[indice]
    if notas[indice] > nota_max:
        nota_max = notas[indice]
    if notas[indice] < nota_min:
        nota_min = notas[indice]

nota_media = suma / tam_notas
print('\nNotas:' )
for indice in range(tam_notas):
    print(notas[indice])
print()
print(f'Nota medía: {nota_media}')
print(f'Nota máxima: {nota_max}')
print(f'Nota mínima: {nota_min}')