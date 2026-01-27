# Condicionales con Python

# if, else, elif

"""

if exp_bool:
	instrucciones
else:
    instrucciones



  if expo_bool:
    instrucciones
 elif expo_bool:
    instrucciones
else: 
    instrucciones
"""

print('Inicio')

numero = int(input('Ingresa un número: ')) 

if numero> 0:
	print("Es un numero positivo")
elif numero == 0:
	print('Es Cero')

else:
	print("Es un numero negativo")

print("Fin")

