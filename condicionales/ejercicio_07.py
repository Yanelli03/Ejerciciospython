# Realiza un algoritmo que calcule la potencia

base = int(input('Dime la base: '))

exponente = int(input('Dime el exponente: '))

if exponente >0:

	print ('La potencia es ' ,base**exponente)

elif exponente == 0 :
	print('La potencia es 1')

else : 
	print('La potencia es ',1/(base**exponente))
