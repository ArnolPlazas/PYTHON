import os
from datetime import datetime, date, time, timedelta
from io import open

formato1 = "%a %b %d %H:%M:%S %Y"
formato2 = "%d-%m-%y %I:%m %p"

sizefile = os.stat('administrar.py').st_size
print(sizefile)


sizefile = os.path.getsize('C:\\Users\\afplazasac\\Documents\\Python\\calculos\\PL_EMRF.txt')
print(sizefile)


estado = os.stat('C:\\Users\\afplazasac\\Documents\\Python\\calculos\\PL_EMRF.txt')
print(estado)

fecha_file=datetime.fromtimestamp(estado.st_mtime).strftime(formato1)
print(fecha_file)

fecha_file2=datetime.fromtimestamp(estado.st_mtime).strftime(formato2)
print(fecha_file2)

tipo_archivo = os.path.splitext('C:\\Users\\afplazasac\\Documents\\Python\\calculos\\PL_EMRF.txt')
print(tipo_archivo)
