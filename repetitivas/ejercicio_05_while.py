#Algoritmo que pida caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' en caso contrario, el programa termina cuando se introduce un espacio.

while True:
	car = input('Introduce un caracter: ')

	while len(car) != 1:
		car = input('Introduce un caracter: ')
	if car == ' ':
		break

	if car.upper() in 'AEIOU':
		print('Es vocal')
	else:
		print('No es vocal')
