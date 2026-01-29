# Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

print ('Calcular sueldo base y 10% de comisión')

sueldo_base = int(input("sueldo_base: "))

venta_1 = float(input("venta_1: "))
venta_2 = float(input("venta_2: "))
venta_3 = float(input("venta_3: "))

comisión =(venta_1 + venta_2 + venta_3)* 0.10 

sueldo_total = sueldo_base + comisión 

print ("sueldo_total es : " , sueldo_total)
print ('la comisión es:' , comisión)
