class compra():
	def __init__(self,precio,cantidad,descuento):
		self.precio = precio
		self.cantidad = cantidad 
		self.descuento = descuento
		self.IVA2020 = 1.19
	def totalpagar(self): 
		if 101 > self.descuento > 1:
			mensaje = "se aplico un descuento de "+str(self.descuento)+"%"	
			self.preciototalsinIVA = self.cantidad * self.precio
			self.precioTotal = self.preciototalsinIVA * self.IVA2020 
			self.descontado = self.precioTotal * (self.descuento*0.01)
			self.descontado = self.precioTotal - self.descontado 
		elif self.descuento == 0:
			mensaje = "no se ingreso el descuento en esta compra"
			self.preciototalsinIVA = self.cantidad * self.precio
			self.precioTotal = self.preciototalsinIVA * self.IVA2020
			self.descontado = 0 
		else:
			mensaje = "ingrese el descuento de forma valida"
			self.precioTotalsinIVA = self.cantidad * self.precio
			self.precioTotal = self.preciototalsinIVA * self.IVA2020
			self.descontado = 0  
		return self.descontado , self.precioTotal ,mensaje
	def cobradoiva(self):
		self.cobradoiva = ((self.precioTotal - self.preciototalsinIVA)**2)**(1/2)
		return self.cobradoiva
def main():
	clasecompra = compra(10,20,10)
	print(clasecompra.totalpagar())
	print(clasecompra.cobradoiva())
main()
