import hashlib
text = "1729fae6e1bea11e946bae755fda7a37ba2755ab419cd5fe623f338e6e9ee725"
chars = " !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
def enPassowrdStr(password):
	password = str(password)
	hashPassowrd = str(hashlib.sha256(password.encode('utf-8')).digest())
	return hashPassowrd
def atksha256(txt):
	for i in range(len(chars)):
		if enPassowrdStr(i) == txt:
			print(i)
