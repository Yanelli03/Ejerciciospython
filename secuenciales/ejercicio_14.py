# Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.

num = int(input('Dime un numero de dos cifras: '))

import math

decenas = math.trunc(num/10)

unidades = (num % 10)

print('Primera cifra (decenas): ',decenas)

print('Segunda cifra (unidades): ',unidades)
