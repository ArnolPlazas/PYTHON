def compruebaMail(mailUsuario):

	"""
	La funcion compruebaMail evualúa un mail
	recibido en busca de la @.
	Si tiene más de una @ es incorrecto
	Si tiene @ al final es incorrecto

	>>> compruebaMail('juan@cursos.es')
	True

	>>> compruebaMail('juancursos.es@')
	False


	>>> compruebaMail('juancursos.es')
	False
	

	>>> compruebaMail('juan@@@cursos.es')
	True
	"""
	arroba=mailUsuario.count('@')

	if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
		return False
	else:
		return True


import doctest
doctest.testmod()