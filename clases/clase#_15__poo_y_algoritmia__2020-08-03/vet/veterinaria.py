class mascota():
	def __init__(self,tipo,eddad,peso):
		self.tipo = tipo
		self.eddad = eddad
		self.peso = peso
		self.listaMascotas = ["perro","ave","pez","gato","otro"]
	def tipoMedeicacion(self):
		self.viaMeidacion = ""
		self.dosisg = 0
		if self.tipo ==self.listaMascotas[0] :
			self.viaMeidacion  = "puede ser mediante una geringa a la boca,inyeccion u otros"
			self.dosisg = 1
		elif self.tipo == self.listaMascotas[1] :	
			self.viaMeidacion = "lo recomendable es hechar le la medicacion en una gotas al agua"
			self.dosisg = 0.01
		elif self.tipo == self.listaMascotas[2] :	
			self.dosisg = 1000
			self.viaMeidacion = "sumerga la comida en la medicacion, o eche la medicacion al agua "
		elif self.tipo == self.listaMascotas[3] :	
			self.viaMeidacion  = "puede ser mediante una geringa a la boca,inyeccion u otros"
			self.dosisg = 1
		else:
			self.viaMeidacion = "depende"
			self.dosisg = 0
		return self.viaMeidacion ,self.dosisg
	def cantiadMediacar(self):
		return self.dosisg * self.peso
class diagnostico():
	def __init__(self,fecha, descripcion):
		self.fecha = fecha
		self.descripcion = descripcion
	def resumen(self):
		self.msg = "la mascota tiene [bold red]"+str(self.descripcion)+"[/bold red] en la fecha de "+str(self.fecha)
		return self.msg
class propietario():
	def __init__(self,nombre , direccion,telefono ,correo ):
		self.nombre = nombre
		self.direccion = direccion
		self.telefono = telefono
		self.correo = correo
	def valorpagar(self,tipo,peso):
		self.tipo = tipo
		self.peso = peso
		animal = mascota(self.tipo,0,self.peso)
		animal.tipoMedeicacion()
		self.catidad = animal.cantiadMediacar()
		self.precio = self.catidad * self.peso
		return self.precio ,"esto el precio a pagar por los medicamentos de su [bold red]"+str(self.tipo)+"[/bold red]"
	def valorPagarCantiad(self,catidad,peso):
		self.catidad = catidad
		self.peso = peso
		self.medicar = self.catidad * self.peso 
		self.precio = self.medicar * self.peso
		return self.precio ,"esto el precio a pagar por los medicamentos de su [bold red]"+str(self.tipo)+"[/bold red]"


		