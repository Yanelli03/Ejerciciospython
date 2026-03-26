# Suponiendo que hemos introducido una cadena por teclado que representa una frase 
# (palabras separadas por espacios), realiza un programa que cuente cuantas 
# palabras tiene.

fullname = input("Escribe tu nombre completo: ")
# print(fullname.title())
words = fullname.split(" ")
iniciales = ""
for word in words:
    iniciales += word[0]

print(iniciales.upper())