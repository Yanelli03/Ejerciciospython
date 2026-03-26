#Función ConvetirEspaciado: Recibe una cadena de caracteres, y devuelve otra con los mismos caracteres separados con espacio.Parámetros de entrada: Cadena de caracteres Dato devuelto: Cadena igual a la anterior pero con espacios entre los /caracteres

def convertir_espaciado(cad):
    nuevo_cad = ''
    for letra in cad:
        nuevo_cad += letra + ''
    return nuevo_cad

cadena = input('Introduce una cadena de texto: ')
print(convertir_espaciado(cadena))  