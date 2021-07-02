import numpy as np
import random 
size=1000

#rng=np.random.default_rng()
#vector=rng.choice(size,size=size,replace=False)
#print(vector)
def p(*args):
	for arg in args:
		print("\n", arg ,"\n")
def ordenamientodes(tamaño):
	arreglo = np.zeros(tamaño)
	#arreglo = []*tamaño
	for i in range(tamaño):
		arreglo[:-1*i] = i
	return invert(arreglo)
def invert(arreglo):
	return arreglo[:-1]
def i(*args):#funcion rapida para ingresar enteros datos
		for arg in args:
			return int(input(args))
def randomvecint(size):
	vec = np.zeros(size)
	for i in range(len(vec)):
		vec[i] =random.randint(0, 100)
	return vec
#p(ordenamientodes(random.randint(0, 100)))
#rndvec = randomvecint(100)
#p(rndvec)
p(ordenamientodes(1000))