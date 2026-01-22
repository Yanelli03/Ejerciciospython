# Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

#input regresa un string para hacer operaciones se debe
#convertir

# int()

print ("Cálculo de Área y Perímetro de un Rectángulo")

base = input('Ingresa la base: ')
base = int(base)

height = input('Ingrsa la altura: ')
height = int(height)

area = base * height
perimeter =  base + base + height + height

print("Area:", area)
print("Perímetro:", perimeter) 

