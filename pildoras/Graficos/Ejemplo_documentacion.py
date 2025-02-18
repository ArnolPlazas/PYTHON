from modulos import funciones_matematicas

class Areas:
	"""Esta clase clacula el área de diferentes figuras geométricas"""
	def areaCuadrado(lado):
		"""Cualcula el área de un cuadrado
			elevando al cuadrado el lado pasando por párametro"""
		return "Ele area de cuadrado es: "+str(lado*lado)

	def areaTriangulo(base,altura):
		""" Calcula el área de un triángulo utlizando los parámetros base y latura"""
		return "El área del triángulo es: "+str((base*altura)/2)


#print(areaCuadrado(5))
#print(areaCuadrado.__doc__)#Documentación en tiempo de ejecución

#help(Areas.areaCuadrado)


#help(Areas)

help(funciones_matematicas)