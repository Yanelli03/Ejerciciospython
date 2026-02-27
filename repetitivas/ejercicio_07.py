#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

tabla = int(input('¿De que numero quieres mostrar la tabla de multiplicar?'))
num = 1
for i in range(10):
	print(num, '*', tabla,'=',num*tabla)
	num +=1

