from hashlib import sha256
def enPassowrd(password):
	hashPassowrd = str(sha256(password.encode('utf-8')).hexdigest())
	return hashPassowrd
class algunAcceso:
	def __init__(self):
		pass
	def registro(self,usr,pwd):
		self.pwd = str(pwd)
		self.usr = str(usr)
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
registroT = algunAcceso()
registroT.registro("hola",enPassowrd("mundo"))
registroT.login("hola",enPassowrd("mundo"))
registroT.acceder()
print("registro correcto")
registroF = algunAcceso()
registroF.registro("hola",enPassowrd("mundo"))
registroF.login("hola","mundo")
registroF.acceder()
registroF.cerrar()
registroF.acceder()
