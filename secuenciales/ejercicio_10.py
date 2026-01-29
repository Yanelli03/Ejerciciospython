#Un alumno desea saber cual será su calificación final en la materia de Algoritmos

print('Calcular nota')

parcial_1 = int(input('nota parcial_1: '))
parcial_2 = int(input('nota parcial_2: '))
parcial_3 = int(input('nota parcial_3: '))

exámen = int(input('nota del exámen: '))

trabajo = int(input('nota del trabajo: '))
nota=((parcial_1+parcial_2+parcial_3)/3)*0.55 + 0.3 *exámen+ 0.15*trabajo

print('nota final: ', nota) 