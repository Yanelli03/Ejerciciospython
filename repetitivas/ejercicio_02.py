import random

numero_escondido = random.randint(1, 100)
intentos = 0

while intentos < 10:
	numero = int(input('Adivina el número: '))
	intentos = intentos + 1
	if numero_escondido == numero:
		print('Lo Adivinaste')
		break
	elif numero_escondido > numero:
		print('Más Grande ')
	else:
		print('Más Pequeño')

if intentos == 10:
  print('Perdiste! Buuu')		
