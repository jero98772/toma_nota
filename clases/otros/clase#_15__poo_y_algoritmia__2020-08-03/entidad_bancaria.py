class cliente():
	def __init__(self, nombre,direccion,telefono,correo,fechaNacimiento):
		self.nombre = nombre
		self.direccion = direccion
		self.telefono = telefono 
		self.correo = correo 
		self.fechaNacimiento = fechaNacimiento
	def registro(self):
		self.registrado = True
		return self.registrado
	def cambiarDatosContacto(self,telefono,correo):
		if telefono == "":
			pass
		else:
			self.telefono = telefono 
		if correo == "":
			pass
		else:
			self.correo = correo 
	def activarlo(self):
		self.activo = False
		if self.registrado:
			self.activo = True
		return self.activo			
	def desactivarlo(self):
		self.activo = False
		return self.activo
class cuentaAhorros():
	def __init__(self,numero,titular ,saldo,tasaInteres):
		self.numero = numero
		self.titular = titular
		self.saldo = saldo
		self.tasaInteres = tasaInteres
	def apertura(self):
		self.aperturaCuenta = True
		return self.aperturaCuenta
	def cierre(self):
		self.aperturaCuenta = False
		return self.aperturaCuenta
	def deposito(self,cantidad):
		self.cantidad = cantidad
		self.saldo += cantidad
	def consultaSaldo(self):
		return self.saldo
class creditoConsumo():
	def __init__(self,numero,titular ,saldoInicial,saldoActual,valorCuota):
		self.numero = numero
		self.titular = titular
		self.saldoInicial = saldoInicial
		self.saldoActual = saldoActual
		self.valorCuota = valorCuota
	def apertura(self):
		self.aperturaCuenta = True
		return self.aperturaCuenta
	def deposito(self,cantidad):
		self.cantidad = cantidad
		self.saldoActual += cantidad
	def consultaSaldo(self):
		return self.saldoActual
def main():
	c = cliente("nombre","la esquina", "12345678","noEsUnCorreo@maildrop.cc","hace 20 años")
	print(c.registro())
	c.cambiarDatosContacto("87654321","EsUnCorreoValido@maildrop.cc")#no devuelve nada
	print(c.activarlo())
	print(c.desactivarlo())
	c2 = cuentaAhorros("06146306210","una persona" ,31415926535 , 0.13 )
	print(c2.cierre())
	print(c2.apertura())
	print(c2.deposito(21415926535))
	print(c2.consultaSaldo())
	c3 = creditoConsumo("06146306210","otra persona" ,31415926535 ,0 , 0.13)
	print(c3.apertura())
	c3.deposito(5926)#no devuelve nada
	print(c3.consultaSaldo())
main()
