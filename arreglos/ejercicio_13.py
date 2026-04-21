# De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana. Para guardar esta información se van a utilizar dos arreglos:
# * Nombre: Vector para guardar los nombres de los conductores.
# * kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
kms = [[0.0] * 8 for _ in range(10)]
dias = [''] * 7
nombre = [''] * 10

tamaño_conductor_max = 10
dias[0] = 'Lunes'
dias[1] = 'Martes'
dias[2] = 'Miercoles'
dias[3] = 'Jueves'
dias[4] = 'Viernes'
dias[5] = 'Sabado'
dias[6] = 'Domingo'

while True:
    num_conductores = int(input('¿Cuantos conductores tiene la empresa?: '))

    if num_conductores>tamaño_conductor_max:
        print(f'Como maximo puedo guardar la indormacion de {tamaño_conductor_max} conductores')
    if num_conductores <=tamaño_conductor_max:
        break

for indice_cond in range(num_conductores):
    nombre[indice_cond] = input(f"Nombre del conductor {indice_cond+1}: ")
    for indice_dias in range(6):
        kms[indice_cond][indice_dias] = int(input(f"¿Cuantos kilometros ha realizado el {dias[indice_dias]}?: "))
for indice_cond in range(num_conductores):
    kms[indice_cond][7] = 0
    for indice_dias in range(6):
        kms[indice_cond][7] = kms[indice_cond][7] + kms[indice_cond][indice_dias]
for indice_cond in range(num_conductores):
    print(f"{nombre[indice_cond]} ha realizado {kms[indice_cond][7]} kilometros")