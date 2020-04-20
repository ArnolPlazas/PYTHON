"""Leer el archivo 'datos.csv' con reder() y
mostrar todos los registros, uno a uno: """

import csv, operator

with open('datos.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        print(reg) # Cada línea se muestra como una lista de campos
        
