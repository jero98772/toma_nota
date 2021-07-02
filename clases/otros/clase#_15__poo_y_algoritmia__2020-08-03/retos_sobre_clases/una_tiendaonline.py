import random
class tienda():
	def __init__(self,producto):
		self.producto = producto
	def disponibilidad(self):
		self.disponible = bool(random.randrange(0,2))
		return self.disponible
	def precio(self,precioProducto = random.randrange(0,5000),nuevoPrecio = random.randrange(0,5000)):
		self.nuevoPrecio = nuevoPrecio
		self.precioProducto = precioProducto 
		self.precioProducto = self.nuevoPrecio
		return self.precioProducto
	def descuento(self, descuento = random.randrange(0,100)):
		self.descuento = descuento
		self.descontado = self.precioProducto * (self.descuento*0.01)
		self.descontado = self.precioProducto - self.descontado
		return self.descontado
def main():
	algunaTienda = tienda("auronocara pulcher")
	print(algunaTienda.disponibilidad())
	print(algunaTienda.precio(100,1000))
	print(algunaTienda.descuento(50))

main()
