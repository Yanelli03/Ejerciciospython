'''
strings con python
'''

name = "Francisco"
profession = "Professor"

greetings = "Hello Im Francisco"

traslate = '"Hello" es "Hola"'
print(traslate)

greetings = 'Hello I\m Francisco' 
print(greetings)

menu = 'Elige una opción: \n1.- Op1\.- Op2'
print(menu)

#strings Format
message1 ="Hello I'm {} and I'm {}",format(name,profession)
print(message1)
# f strinf
message2 = f"Hello I'm {} and I'm {}",format(name,profession)
print(message2)

#metodos para strings

movie = "Volver al futuro"
print = (movie.upper)
print = (movie.lower)
print = (movie.capitalize)
print = (movie.title)
print = (movie.split(" "))
print = (movie.startswith(" "))
print = (movie.endswith("V"))
print = ("a" in movie)
