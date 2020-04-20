print("Programa de evualuación de notas de alumnos")

nota_alumno=input("Intruduce la nota del alumno: ")

def evaluacion(nota):
	v="aprobado"
	if nota<5:
		v="suspenso"
	return v

print(evaluacion(int(nota_alumno))) 