import re
'''lista_nombres=['Ana Gómez',
				'María Martín',
				'Sandra López',
				'Santiago Martín',
				'Sandra Fernández']

for elemento in lista_nombres:
	if re.findall('^Sandra',elemento):
		print(elemento)


for elemento in lista_nombres:
	if re.findall('Martín$',elemento):
		print(elemento)'''

lista_nombres=['Hombres',
				'Mascotas',
				'Mujeres',
				'Niños',
				'Niñas']

for elemento in lista_nombres:
	if re.findall('Niñ[oa]s',elemento):
		print(elemento)