print("Programa de becas")

distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(str(distancia_escuela)+"km")

numero_hermanos=int(input("Introduce el n de hermanos: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce el salario mensual: "))
print(str(salario_familiar)+" Pesos")

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=2000000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")