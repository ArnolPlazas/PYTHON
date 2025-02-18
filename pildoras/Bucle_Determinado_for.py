# for i in [1,2,3]:
# 	print("Hola ")

# for i in ["Inviernno","Primavera","Otoño","Verano"]:
# 	print("Hola "+ i)

# for i in ["Pildoras","Informatica",3]:
# 	print("Hola",end=" ")


# for i in "Imprimir":
# 	print("Hola",end=" ")

email=False
mail=input("Inserte su email: ")
for i in mail:
	if (i=="@"):
		email=True

if email==True:
	print("Email correcto")
else:
	print("Email incorrecto")					