class Empleado:
	def __init__(self,nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,
			self.cargo,self.salario)


listaEmpleados=[

Empleado("JUAN","DIRECTOR",7000000),
Empleado("ANA","PRESIDENTE",9000000),
Empleado("ANTONIO","ADMINISTRATIVO",2700000),
Empleado("SARA","SECRETARIA",1300000),
Empleado("MARIO","BOTONES",700000),
]


salario_altos=filter(lambda empleados:empleados.salario>1000000,listaEmpleados)

for empleado_salario in salario_altos:
	print(empleado_salario)