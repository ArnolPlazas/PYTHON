class Empleado:
	def __init__(self,nombre,cargo,salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,
			self.cargo,self.salario)


listaEmpleados=[

Empleado("JUAN","DIRECTOR",7000),
Empleado("ANA","PRESIDENTE",9000),
Empleado("ANTONIO","ADMINISTRATIVO",2700),
Empleado("SARA","SECRETARIA",1300),
Empleado("MARIO","BOTONES",70),
]


def calculo_comision(empleado):
	if empleado.salario<=3000:
		empleado.salario=empleado.salario*1.03
	return empleado

listaEmpleado_comision=map(calculo_comision,listaEmpleados)

for empleado in listaEmpleado_comision:
	print(empleado)


