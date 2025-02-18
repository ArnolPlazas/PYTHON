import math

print("Programa de cálculo de la raiz cuadrada")
numero=int(input("Introduce un número por favor: "))

intentos=0

while numero<0:
	print("No se puede hallar la raiz de un número negativos")

	if intentos==2:
		print("Has consumido demasiados intentos. El programa ha finalizado")
		break
	numero=int(input("Introduce un número por favor: "))

	if intentos<0:
		intentos=intentos+1
		
if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de: " + str(numero) + " es: " + str(solucion) )