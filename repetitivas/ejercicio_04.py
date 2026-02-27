#Realizar un algoritmo que pida números 

igual_0 = 0

mayor_0 = 0

menor_0 = 0

veces = int(input('¿Cuantos numeros vas a introducir?: '))

for i in range(veces):
	num = int(input('Ingresa un numero: '))
	if num == 0:
		igual_0 += 1
	elif num < 0:
		menor_0 += 1
	else:
		mayor_0 += 1


print('Ingresaste', igual_0, 'ceros')

print('Ingresaste', mayor_0, 'menores a cero')

print('Ingresaste', menor_0, 'menores a cero')
