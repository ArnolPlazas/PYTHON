from datetime import datetime, date, time, timedelta
import calendar

ahora = datetime.now()  # Obtiene fecha y hora actual

print("Hora:", ahora.hour) 

if ahora.hour>0 and ahora.hour<12:
     print("Buenos dias")
if ahora.hour>=12 and ahora.hour<=17:
	print("Buenas Tardes")

else:
	print("Buenas Noches")