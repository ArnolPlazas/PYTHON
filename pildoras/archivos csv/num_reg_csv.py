import csv, operator

# Leer el archivo 'datos.csv' con reader() y 
# mostrar todos los registros, uno a uno:

fichero = "PL_PROV_SRM.csv"
with open('PL/'+ fichero) as csvarchivo:
    conteo=0
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        conteo+=1
        #rint(reg)  # Cada línea se muestra como una lista de campos

print(conteo)
