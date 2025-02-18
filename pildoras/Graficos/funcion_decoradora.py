def funcion_decoradora(funcion_parametro):
	def funcion_interna(*args,**kwarks):
		#Acciones adicionales que decoran
		print("Vamos a realizar un calculo: ")
		funcion_parametro(*args,**kwarks)
		#Acciones adicionales que decoran
		print("Hemos termiando el cálculo")
	
	return funcion_interna

@funcion_decoradora
def sumar(num1,num2,num3):
	print(num1+num2+num3)


@funcion_decoradora
def restar(num1,num2):
	print(num1-num2)

@funcion_decoradora
def potencia(base,exponente):
	print(pow(base,exponente))


sumar(7,10,5)
restar(20,4)
potencia(base=5,exponente=3)