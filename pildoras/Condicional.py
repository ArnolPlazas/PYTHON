salario_presidente=int(input("Intruduce salario presidente: "))
print ("salario_presidente: "+str(salario_presidente))

salario_director=int(input("Intruduce salario director: "))
print ("salario_director: "+str(salario_director))

salario_jefe_area=int(input("Intruduce salario jefe_area: "))
print ("salario_jefe_area: "+str(salario_jefe_area))

salario_administrativo=int(input("Intruduce salario administrativo: "))
print ("salario_administrativo: "+str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")
