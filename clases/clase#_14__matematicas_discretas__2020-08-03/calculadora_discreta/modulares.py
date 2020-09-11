from math import gcd
def root(x,p,root):
	respuesta = x**(p/root)
	return respuesta
def sumaM(a,b,mod):
	respuesta = (a+b)%mod
	return respuesta
def productoM(a,b,mod):
	respuesta = (a*b)%mod
	return respuesta
def poteciaM(base,a,mod):
	respuesta = (base**a)%mod
	return respuesta
def inv(num):
	respuesta = 1/num
	return respuesta
def invM(a,mod):
	if gcd(a,mod) != 1:
		return -1
	else:
		return a**(mod-2)
def divisionM(a,b,mod):
	a = a % mod
	inver = invM(b,mod) 
	if(inver == -1): 
		return False
	else: 
		return (inver*a) % m
def raizCuadradaM(a,mod):
	for i in range(a,mod):
		if i**2 % a == mod:
			return i % a
		else :
			return False
def cuadradosPerfectoM(a,mod):
	for i in range(a):
		if i**2 == a%mod:
			return a%mod
		else : 
			return False
