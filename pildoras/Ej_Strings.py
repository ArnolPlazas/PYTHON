Correo=input("Introduce tu correo:  ")


cant_arrobas=Correo.count("@")
sufijo_valido=Correo.endswith(".com")
sufijo_invalido=Correo.endswith("@")
prefijo_invalido=Correo.startswith("@")


if (cant_arrobas==1 and sufijo_valido==True and sufijo_invalido==False and prefijo_invalido==False):
	print("El correo es correcto: ", Correo.lower())
else:
	print("El correo es incorrecto: ", Correo.lower())