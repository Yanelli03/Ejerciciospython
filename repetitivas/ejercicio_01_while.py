#Crea una aplicación que pida un número y calcule su factoral

print('Programa de Factorial de un Número')

número = int(input('Dime un número: '))

resultado = 1
contador = 1

while contador <= número:
	pass
	resultado = resultado * contador
	contador = contador + 1
print('El factorial de',número, 'es:', resultado)