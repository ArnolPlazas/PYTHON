import re


nombre1="Camila Medina"
nombre2="Jara Marin"
nombre3="Lara Perea"

cadena="1dcoeS"
codigo="dedeefcsdfdcsfsdf  73 dsdsdffs"

'''if re.match("Camila",nombre1,re.IGNORECASE):  #Buscar al inicio de los datos
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado")'''



if re.match(".ara",nombre3,re.IGNORECASE):  #  . comodin
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado")



if re.match("\d",cadena):  # Que empiece por un numero
	print("Hemos encontrado el numero")
else:
	print("No hemos encontrado")



if re.search("73",codigo):  #Patron de buscqueda en toda la cadena
	print("Hemos encontrado el nombre")
else:
	print("No hemos encontrado")