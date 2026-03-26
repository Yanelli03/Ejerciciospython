#Crear una función recursiva que permita calcular el factorial de un número.

def factorial(num):
    if num == 1:
        return 1
    else:
         return num *factorial(num - 1)

numero = int(input('numero: '))

resultado = factorial(numero)

print('El factorial es:', resultado)
