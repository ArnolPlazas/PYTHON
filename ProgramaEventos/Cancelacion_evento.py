import sched
import time
import random

# Función que es llamada por los eventos
def abrir_cerrar(estado, mantener):
    print('TIEMPO:', int(time.time()))
    if mantener and not programador.empty():
        programador.cancel(ev2)
        
    if estado:
        print("Abriendo compuertas...")
    else:
        print("Cerrando compuertas...")
    
# Obtener un número aleatorio entre 1 y 5
# Si el valor es impar: no cerrar compuertas
valor = random.randint(1, 5)
if valor % 2:
    print("No mantener compuertas abiertas")
    mantener_abiertas = False
else:
    print("Mantener compuertas abiertas")   
    mantener_abiertas = True

# Declarar el programador
programador = sched.scheduler(time.time, time.sleep)

# Asignar el tiempo de comienzo (en segundos)
comienzo = int(time.time())
t1 = comienzo + 1   # Tiempo para abrir compuertas
t2 = t1 + 4         # Tiempo para cerrar compuertas
print('PROGRAMADOR INICIADO:', comienzo)

# Definir los dos eventos indicando: momento de ejecución, 
# prioridad, función a la que se llama y valores que se
# pasan a los argumentos de la función:
ev1 = programador.enterabs(t1, 1, abrir_cerrar, 
                           (1, mantener_abiertas))
ev2 = programador.enterabs(t2, 1, abrir_cerrar, 
                           (0, mantener_abiertas))

# Poner en marcha el programador.
# El programa permanece a la espera hasta que se
# ejecuten los dos eventos. La ejecución se producirá
# cuando se alcance el momento definido.
programador.run()
print('PROGRAMADOR FINALIZADO:', int(time.time()))
