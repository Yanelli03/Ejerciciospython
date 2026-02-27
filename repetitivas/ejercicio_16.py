#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.

print('Calcular Salario')

horas_por_semana = 0
horas_acum = 0
trabajador = 0

trabajadores = int(input('¿Cuántos trabajadores tiene la empresa?: '))

sueldo_por_hora = float(input('Sueldo por hora: '))
for trabajador in range(1, trabajadores + 1) :
	horas_por_semana = int(input('¿Cuantas horas por semana trabaja el trabajador?'))
	horas_acum = horas_acum + horas_por_semana

	print('El trabajador tiene un sueldo: ',horas_por_semana*sueldo_por_hora)
	print('El pago a los trabajadores es: ',horas_acum*sueldo_por_hora)