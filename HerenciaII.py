class Persona():
	def __init__(self,nombre,edad,Lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.Lugar_residencia=Lugar_residencia
	def descripcion(self):
		print("Nombre: ",self.nombre," Edad: ",self.edad," Residencia: ",self.Lugar_residencia)

class Empleado(Persona):
	def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado): 
		super().__init__(nombre_empleado,edad_empleado,residencia_empleado)#La instrucción super llama al metodo init de la clase padre
		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):
		super().descripcion()
		print("Salario: ",self.salario," antiguedad: ",self.antiguedad)

empleado1=Empleado(15000,13,"Manuel",55,"Colombia")
empleado1.descripcion()

print(isinstance(empleado1,Empleado))