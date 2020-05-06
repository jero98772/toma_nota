import random
import numpy as np

def par_o_impar(entrada): 
	impar = []
	par = []
	for i in entrada:
		if i % 2 == 0:
		    par.append(i)
		else:
		    impar.append(i)
	return par+impar
def randomvecint(size):
	vec = np.zeros(size)
	for i in range(len(vec)):
		#i = int(input("input para array"))
		rnd=random.randint(0, size)
		print(rnd)
		vec[i] =rnd#random.randint(0, size)
	return vec	
size = 20
print(par_o_impar(randomvecint(size)))