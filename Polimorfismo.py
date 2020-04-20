class Coche():
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")

class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(vehiculo): #Polimorfismo: Trasforma a un objeto de tipo Camion
	vehiculo.desplazamiento()

miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo)#Envia el objeto de tipo Camion al metodo
