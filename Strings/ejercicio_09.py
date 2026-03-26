# Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.

frase = input("Ingresa una frase: ")
palabra = input("Ingresa una palabra: ")

if palabra in frase:
    print(f"'{palabra}' se encuentra en '{frase}'")
else:
    print(f"'{palabra}' No se encuentra en '{frase}'")
