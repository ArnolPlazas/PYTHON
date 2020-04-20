from datetime import date,datetime

#OBJETO DATE

print("Fecha actual",date.today())
print("Dia del mes",date.today().day)
print("Mes del año",date.today().month)
print("Año",date.today().year)
print("Dia de la semana",date.today().weekday()) # Regresa un digito de 0-6


mes= {1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
dia_semana={0:"Lunes",1:"Martes",2:"Miercoles",3:"Jueves",4:"Viernes",5:"Sabado",6:"Domingo"}



fecha="Hoy "+dia_semana[date.today().weekday()]+" "+str(date.today().day)+" "+mes[date.today().month]+ " del "+str(date.today().year)

print("Fecha actual: ",fecha)

#-------------------------------
print()
print()
print()
print()
#-------------------------------

#OBJETO DATETIME

print("Fecha y hora actual: ",datetime.now())
print("Seguntos actuales: ",datetime.now().second)
print("Minutos actuales: ",datetime.now().minute)
print("Hora actual: ",datetime.now().hour)  # Hora formato 24
print("MicroSeguntos actuales: ",datetime.now().microsecond)

# DIRECTIVAS FECHA
# %Y: AÑO CON 4 DIGITOS
# %m: MES CON DOS DIGITOS
# %d: DIA CON DOS DIGITOS

#DIRECTIVA HORA
# %H: HORA CON FORMATO 24H Y DOS DIGITOS
# %M: MINUTOS ACTUALES CON DOS DIGITOS
# %S: SEGUNDOS ACTUALES CON DOS DIGITOS

print(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))


print("Mes del año",datetime.today().month)
