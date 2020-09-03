from hashlib import sha256
def enPassowrd(password):
	hashPassowrd = str(sha256(password.encode('utf-8')).hexdigest())
	return hashPassowrd
class usuario:
	def __init__(self,idusr,nombre,dirccion,tel,usr,pwd):
		self.idusr = idusr
		self.nombre = nombre
		self.dirccion = dirccion
		self.tel = tel		
		self.usr = usr
		self.pwd = pwd
	def registro(self):
		self.password = self.pwd
		self.username = self.usr
	def login(self,usr,pwd):
		self.login = False		
		self.pwd = str(pwd)
		self.usr = str(usr)
		if self.password == self.pwd and self.username == self.usr:
			self.login = True
	def cerrar(self):
		self.pwd = ""
		self.usr = ""
		self.login = False
	def acceder(self):
		if self.login :
			print("accedistes")
		else:		
			print("no accedistes")
	def reservarPelicula(msg):
		self.msg = msg
		return self.msg
	def pagarReserva(estadoPago):
		self.estadoPago = estadoPago
		return self.estadoPago
class pago():
	def __init__(self,valor,idPago,idusr):
		self.valor = valor
		self.idPago = idPago
		self.idusr = idusr
	def siPago(self):
		if type(self.valor) == type(0) or type(self.valor) == type(0.0):return True
		else: return False
class pelicula():
	def __init__(self,idpelicula,nombrepelicula,fechaProyecion,lugarProyecion,puestos):
		self.idpelicula = idpelicula
		self.nombrepelicula = nombrepelicula
		self.fechaProyecion = fechaProyecion
		self.lugarProyecion = lugarProyecion
		self.puestos = puestos
		self.puestosSala = 100 
	def disponibles():
		return self.puestosSala - self.puestos = puestos
u = usuario(1,"bob","casa en algun lado","164266","alice",enPassowrd("deciframe jajaja no puedes"))
u.registro()
u.login("alice",enPassowrd("deciframe jajaja no puedes"))
billete = pago("0",0,0)
q = billete.siPago()
print(q)
print(enPassowrd("deciframe jajaja no puedes"))
#ya se presento
