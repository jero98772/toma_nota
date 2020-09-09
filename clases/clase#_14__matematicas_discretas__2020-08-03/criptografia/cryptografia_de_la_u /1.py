#gano o perdio compruebe aqui https://pastebin.com/ZR5TqqvU
import hashlib
def enPassowrdHash(password):
	hashPassowrd = hashlib.sha256(password.encode("utf-8")).digest()
	return hashPassowrd
def enPassowrdStr(password):
	hashPassowrd = str(hashlib.sha256(password.encode('utf-8')).digest())
	return hashPassowrd
def enPassowrdHashHex(password):
	hashPassowrd = hashlib.sha256(password.encode("utf-8")).hexdigest()
	return hashPassowrd
def enPassowrdStrHex(password):
	hashPassowrd = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
	return hashPassowrd
def sha256(password):
	print(password,enPassowrdStrHex(password),"hash en hexadeciemal")
	print(password,enPassowrdHashHex(password),"hash en hexadeciemal")
	print(password,enPassowrdStr(password),"hash casi binario")
	print(password,enPassowrdHash(password),"hash casi binario")

def main():
	A = "aprobado"
	sha256(A)
	B = "Aprobado"
	sha256(B)
	C = "APROBADO"
	sha256(C)
	num = 0 
	while num < 5.1:
		sha256(str(num))
		num += 0.1
	num2 = 0 
	while num2 < 5:
		sha256(str(num2))
		num2 += 1
def cuentaEnSha(hashencontrar):
	for i in range(10001):
		algo = enPassowrdStrHex(str(i))
		if hashencontrar == algo: 
			print(str(i))
cuentaEnSha("ca0cec7f60085f0289aaea5cbfbdd84ad2ba05148de121075dab1c636682a566")

