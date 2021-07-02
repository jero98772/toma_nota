class credito():
	def __init__(self,tomador,cupo,cuotas,disponible):
		self.tomador = str(tomador)
		self.cupo = int(cupo)
		self.cuotas = int(cuotas)
		self.disponible = int(disponible)
	def ValorTotal(self,cantidadCompras,valor):
		self.cantidadCompras = cantidadCompras
		self.valor = valor
		self.valortotal = self.cantidadCompras*self.valor
		return self.valortotal
	def puedeComprar(self):
		print(self.cupo)
		if  self.valortotal > self.cupo :
			self.nuevoValCupo = self.valortotal-self.cupo 
			print(self.nuevoValCupo)
		else :
			self.nuevoValCupo = self.cupo-self.valortotal
			print(self.nuevoValCupo)
		return self.nuevoValCupo
	def abonoDeuda(self):
		self.disponible -= self.nuevoValCupo
		return self.disponible
c = credito("alguno",100,12,75)
print(c.ValorTotal(3,15))
print(c.puedeComprar())
print(c.abonoDeuda())
c.abonoDeuda()
		
