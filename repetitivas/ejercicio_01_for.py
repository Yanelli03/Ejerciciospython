print('Programa que calcula el factorial de un Numero')

número = int(input('Ingresa un número: '))

factorial = 1

for i in range(número): #[0, 1, 2, 3, 4]
	factorial *= (1 + 1)

print('El factorial de', número, 'es', factorial)