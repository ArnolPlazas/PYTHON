nombreUsuario=input("Introduce tu nombre de Usuario: ")
print("El usuario es: ", nombreUsuario)
print("El nombre es: ",nombreUsuario.upper())
print("El nombre es: ",nombreUsuario.lower())
print("El nombre es: ",nombreUsuario.capitalize())

edad=input("introduce la edad: ")
while(edad.isdigit()==False):
	print("Por favor introduce un valor numerico")
	edad=input("introduce la edad: ")

if(int(edad)<18):
	print("No se pude pasar")
else:
	print("pude pasar")
