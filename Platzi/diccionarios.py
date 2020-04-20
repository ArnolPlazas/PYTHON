calificaciones = {}
calificaciones['Algoritmos'] = 9
calificaciones['Matematicas'] = 10
calificaciones['Web'] = 8
calificaciones['Bases de datos'] = 10

for key in calificaciones:
    print (key)

for value in calificaciones.values():
    print(value)

for key, value in calificaciones.items():
    print('llave: {}, valor: {}'.format(key, value))

suma_de_calificaciones = 0
for calificacion in calificaciones.values():
    suma_de_calificaciones += calificacion

print(suma_de_calificaciones)

promedio = suma_de_calificaciones/len(calificaciones.values())

print(promedio)