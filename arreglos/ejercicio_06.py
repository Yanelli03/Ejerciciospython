# Crea un programa que pida un número al usuario un número de mes (por ejemplo, 
# el 4) y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. 
# Debes usar un vector. Para simplificarlo vamos a suponer que febrero tiene 28 días.

dias = [0] * 12
nombre_mes = [""] * 12

dias[0] = 31
dias[1] = 28
dias[2] = 31
dias[3] = 30
dias[4] = 31
dias[5] = 30
dias[6] = 31
dias[7] = 31
dias[8] = 30
dias[9] = 31
dias[10] = 30
dias[11] = 31

nombre_mes[0] = "Enero"
nombre_mes[1] = "Febrero"
nombre_mes[2] = "Marzo"
nombre_mes[3] = "Abril"
nombre_mes[4] = "Mayo"
nombre_mes[5] = "Junio"
nombre_mes[6] = "Julio"
nombre_mes[7] = "Agosto"
nombre_mes[8] = "Septiembre"
nombre_mes[9] = "Octubre"
nombre_mes[10] = "Noviembre"
nombre_mes[11] = "Diciembre"

while True:
    mes = int(input("Introduce un mes (1-12): "))
    if mes<1 or mes>12:
        print("Error: mes incorrecto.")
    if mes >=1 and mes<=12:
        break
print(f"El mes de {nombre_mes[mes-1]} tiene {dias[mes-1]} dias" )
