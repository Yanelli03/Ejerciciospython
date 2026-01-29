# Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde

print('Calcular horas')

minutos_completos = int(input("Ingresa la cantidad de minutos: "))

horas = minutos_completos // 60
minutos_res = minutos_completos % 60

print("minutos es igual a:",  horas, "horas y", minutos_res, "minutos")




