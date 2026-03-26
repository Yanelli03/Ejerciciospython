# Queremos guardar los nombres y la edades de los alumnos de un curso. 
# Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre 
# un asterisco (*) Al finalizar se mostrará los siguientes datos:
#  * Todos lo alumnos mayores de edad.
#  * Los alumnos mayores (los que tienen más edad)

temperatura = [[0.0] * 2 for _ in range(5)]
cant_dias = 5

for indice in range(cant_dias):
    temperatura[indice][0] = float(input(f"Dia {indice+1}. Temperatura minima: "))
    temperatura[indice][1] = float(input(f"Dia {indice+1}. Temperatura maxima: "))

print("Temperaturas medias")
print("===================")

for indice in range(cant_dias):
    print(f"Dia {indice+1}. Temperatura media: {(temperatura[indice][0]+temperatura[indice][1])/2}")

temp_min = temperatura[0][0]
for indice in range(cant_dias):
    if temperatura[indice][0]<temp_min:
        temp_min = temperatura[indice][0]

print("Dias con menos temperatura")
print("===================")

for indice in range(cant_dias):
    if temperatura[indice][0]==temp_min:
        print(f"Dia {indice+1}")

existe_tem = False

print("Dias con temperatura maxima")
print("===================")

temp_max = int(input("Introduce la temperatura: "))
for indice in range(cant_dias):
    if temperatura[indice][1]==temp_max:
        print(f"Dia {indice+1}")
        existe_tem = True

if existe_tem == False:
    print("No hay ningun dia con dicha temperatura.")
