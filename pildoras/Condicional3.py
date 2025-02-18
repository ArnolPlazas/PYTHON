print("Asignaturas electivas")
print("Informática gráfica-Pruebas de software-Usabilidad y accesibilidad")
opcion=input("Escriba la asignatura escogida: ")
asignatura=opcion.lower()

if asignatura in ("informática gráfica, pruebas de software, usabilidad y accesibilidad"):
	print("Asignatura elegida: "+ asignatura)
else:
	print("La asignatura no esta en la lista")
