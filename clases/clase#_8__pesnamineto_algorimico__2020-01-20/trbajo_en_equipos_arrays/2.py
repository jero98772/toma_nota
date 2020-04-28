import numpy as np
import random 
size=1000


def p(*args):
	for arg in args:
		print("\n", arg ,"\n")
def randomvecint(size):
	vec = np.zeros(size)
	for i in range(len(vec)):
		vec[i] =random.randint(0, 100)
	return vec	
def ordenamientodes(arreglo):
	for i in range(len(arreglo)+1):
		arreglo[-1*i] = i
	return arreglo

p(ordenamientodes(randomvecint(size)))
