#Escribe un programa que diga si un número introducido por teclado es o no primo

número = int(input('Introduce un número para comprobar si es primo: '))

es_primo = True

if número <=1 :
	es_primo = False

else:
	for i in range(2,int(número **0.5)+1):
		if número % i == 0:
			es_primo = False 
			break
if es_primo:

	print('Es primo') 

else:
	print('No es primo')	

