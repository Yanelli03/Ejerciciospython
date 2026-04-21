# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
# * Las cantidades totales de cada articulo.
# * La cantidad de artículos en la sucursal 2.
# * La cantidad del articulo 3 en la sucursal 1.
# * La recaudación total de cada sucursal.
# * La recaudación total de la empresa.
# * La sucursal de mayor recaudación.
precio = [0] * 5
cantidad = [[0.0] * 5 for _ in range(4)]

for indice_art in range(4):
    precio[indice_art] = float(input(f'Ingrese precio de articulo {indice_art+1}: '))
for indice_sucursal in range(3):
    for indice_art in range(4):
        cantidad[indice_sucursal][indice_art] = float(input(f'Ingrese cantidad del articulo {indice_art+1} en sucursal {indice_sucursal+1}: '))
for indice_art in range(4):
    suma = cantidad[0][indice_art]+cantidad[1][indice_art]+cantidad[2][indice_art]+cantidad[3][indice_art]
    print(f'Total articulo {indice_art+1}: {suma}')

Articulo_sucursal12 = 0
for indice_art in range(4):
    Articulo_sucursal12 = Articulo_sucursal12+cantidad[1][indice_art]
print(f'Total sucursal 2: {Articulo_sucursal12}')
print(f'Sucursal 1 articulo 3: {cantidad[0][2]}')

MayorRec = 0
NumMayor = 0
TotalEmpresa = 0
for indice_sucursal in range(3):
    TotalSucursal = TotalSucursal + (cantidad[indice_sucursal][indice_art]*precio[indice_art])
    print(f'Recaudaciones sucursal {indice_sucursal+1}: {TotalSucursal}')
    if TotalSucursal>MayorRec:
        MayorRec = TotalSucursal
        NumMayor = indice_sucursal+1
    TotalEmpresa = TotalEmpresa + TotalSucursal
print(f'Recuadacion total de la empresa: {TotalEmpresa}')
print(f'Sucursal de mayor recudacion: {NumMayor}')