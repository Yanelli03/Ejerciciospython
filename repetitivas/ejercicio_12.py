#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

print('Calcular Ahorro')

ahorro_acum = 0.0
for mes in range(1,13) :
	cant_mensual = float(input(f'¿Cuánto has ahorrado en el mes {mes}? : '))
	ahorro_acum = ahorro_acum + cant_mensual
print('En el mes  llevas ahorrado : ', ahorro_acum )