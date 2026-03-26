frase = input ('ingresa una frase: ' )
letra = input ('Ingresa una letra: ')
while len(letra) != 1:
    letra = input('Ingresa una letra: ')
count = 0
for i in frase:
    if 1 == letra:
        count += 1


print("La letra '{ letra }' esta { count } veces en '{ frase }'")