#

palabra = input("Escribe una palabra: ")

if palabra == palabra[::-1]: 
    print("Es un palindromo")
else:
    print("No es un palindromo")
