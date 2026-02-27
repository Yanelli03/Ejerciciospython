""" a """

def say_hello():
	print("Hello")

say_hello() 
print(say_hello)
print(type(say_hello))

#Funcion con parametros sin retorno

def say_hello_by_name(name):
	print("Hola", name)

say_hello_by_name("Yane")
say_hello_by_name("Humans")
say_hello_by_name("Inges")

def tabla(num):
	print("Tabla del ", num)
	print()
	for i in range(10):
		print(num,"*",(i+1),"=", (i+1)* num)
tabla(5)
tabla(13)
tabla(7)


#Funciones con parametro y con retorno

def suma(num1,num2):
	return num1+num2

result_suma=suma(23, 57)
print(result_suma)

def iniciales(name, ape1, ape2):
	return name[0] + ape1[0] + ape2[0]

curp=iniciales("Maricruz Yanelli","Gasca","De Luis")
print(curp)

print(iniciales("Juan José","Domínguez","Hernández"))

#Funciones con parametros posicionales 
#Funciones con parametros nombrados

def super_heroe(name, hero):
	print(name, "is of", hero)

super_heroe("Batman", "Batman movie")
super_heroe("Superman","Superman movie")
super_heroe("Dayanne", "Wonder Woman movie")

super_heroe(hero="Flash", name="The Flash")


print(iniciales(ape1="Gasca", name="Yanelli", ape2="De Luis"))


#Funciones con parametros opcioneales

def mult(nume1, nume2=10):
	return nume1*nume2

print(mult(10, 24))
print(mult(10))
print(mult(24))
