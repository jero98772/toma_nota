import random
import numpy as np

def par_o_impar(entrada): 
	impar = []
	par = []
	size = 10
	for i in entrada:
		if i % 2 == 0:
		    par.append(i)
		else:
		    impar.append(i)
	return par+impar
def randomvecint(size):
	vec = np.zeros(size)
	for i in range(len(vec)):
		vec[i] =random.randint(0, 10)
	return vec	
size = 10
print(par_o_impar(randomvecint(size)))