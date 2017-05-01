def mi_decorador(funcion):
	def nueva(*args):
		print "Llamanda a la funcion ", funcion.__name__
		retorno=funcion(*args)
		return retorno
	return nueva
@mi_decorador
def imp(mensaje):
	print mensaje

mi_decorador(imp)("hola")
