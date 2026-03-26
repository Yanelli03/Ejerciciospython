#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
#sustituye la aparición del primer carácter en la cadena por el segundo carácter.

frase = input("Ingresa una frase: ")

letra_1 = input("Ingresa una letra: ")
letra_2 = input("Ingresa otra letra (sustituye a la primera): ")

#Metodo 1
print(frase.replace(letra_1, letra_2))