#Función calcularTemperaturaMedia: Recibe dos números reales que representan dos temperaturas y devuelve la temperatura media.

def calcular_temperatura_media (tmin,tmax):
    return (tmin + tmax) / 2

cantidad = int (input('¿Cuántas temperaturas vas a calcular? : '))

for indice in range (cantidad):
    tmin = float(input("Introduce temperatura minima: "))
    tmax = float(input("Introduce temperatura máxima : "))

media = calcular_temperatura_media
print("Temperatura media:", media)

    