"""Leer el archivo 'datos.csv' con reder() y
realzar algunas operaciones básicas: """

import csv, operator

csvarchivo = open('datos.csv') # Abrir archivo csv
entrada = csv.reader(csvarchivo) # Leer todos los registros

reg = next(entrada) # Leer registro (forma lista)
print(reg) # Mostrar registro

nombre, provincia, consumo = next(entrada) #Leer campos
print(nombre, provincia, consumo) #Mostrar campos

nombre, provincia, consumo = next(entrada) #Leer campos
print(nombre, provincia, consumo) #Mostrar campos

nombre, provincia, consumo = next(entrada) #Leer campos
print(nombre, provincia, consumo) #Mostrar campos

del nombre, provincia, consumo, entrada # Borrar objetos

#csvarchivo.close() # Cerrar archivo



