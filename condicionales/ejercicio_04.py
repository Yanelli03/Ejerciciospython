# Crea un programa que pida al usuario dos números y muestre su división

print('Calcular división')

dividendo = int(input('Dime el número 1: ')) 
divisor = int(input('Dime el número 2: '))

if divisor == 0 :
	print ('No se puede dividir por 0')

else:
	resultado: dividendo/divisor

	print('La división es: ' ,dividendo/divisor)
