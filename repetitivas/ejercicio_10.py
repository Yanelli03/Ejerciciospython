# Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

tabla = 1
num = 1
for tabla in range(1, 6):
	for num in range (1, 11):
		print(tabla,'*',num,'=',tabla*num)
