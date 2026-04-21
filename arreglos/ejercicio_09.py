# Queremos guardar los nombres y la edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# * Todos lo alumnos mayores de edad.
# * Los alumnos mayores (los que tienen más edad)
cant_dias = 5
temperatura = [[0.0] * 2 for _ in range(5)]

for indice in range(cant_dias):
    temperatura[indice][0] = float(input(f'Día {indice+1}. Temperatura minima: '))
    temperatura[indice][1] = float(input(f'Día {indice+1}. Temperatura maxima: '))

print('Temperaturas medias')
print('===================')
for indice in range(cant_dias):
    print(f'Dia {indice+1}. Temperatura media: {(temperatura[indice][0]+temperatura[indice][1])/2}')

temp_min = temperatura[0][0]
for indice in range(cant_dias):
    if temperatura[indice][0]<temp_min:
        temp_min = temperatura[indice][0]

print('Días con menos temperaturas')
print('===================')
for indice in range(cant_dias):
    if temperatura[indice][0]==temp_min:
        print(f'Dia {indice+1}')
existe_temperatura = False

print('Días con temperatura maxima')
print('===================')
temp_max = int(input('Introduce la temperatura: '))
for indice in range(cant_dias):
    if temperatura[indice][1]==temp_max:
        print(f'Dia {indice+1}')
        existe_temperatura = True

if existe_temperatura == False:
    print('No hay ningun día con dicha temperatura.')