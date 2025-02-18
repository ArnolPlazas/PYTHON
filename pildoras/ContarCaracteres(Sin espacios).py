#contar los caracteres de un String sin contar con los espacios
nombre="Pildora Informatica"

contador=0

for i in nombre:
	if i==" ":
		continue
	contador+=1
print(contador)

