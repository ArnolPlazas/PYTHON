# i=0
# while i<=10:
# 	print("Ejecución " + str(i))
# 	i+i+1

# print("Terminó la Ejecución")

edad=int(input("Introduce tu edad por favor: "))

while edad<=6 or edad>=100:
	print("Has introducido una edad negativa. Vuelve intentarlo")
	edad=int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar puedes pasar")
print("Edad del aspirante: "+ str(edad))