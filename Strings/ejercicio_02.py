cadena = input('Escribe una frase: ')
subcad =input('Escribe una subcadena: ')

if cadena.startswith(subcad):
    print(f'{ cadena }comienza con { subcad }')
else:
    print(f'{ cadena } No comienza con { subcad }')
