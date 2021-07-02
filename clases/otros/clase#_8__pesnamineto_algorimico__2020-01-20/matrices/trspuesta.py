import numpy as np
import random 

matriz = np.array([[1,2,3,4,5,6],[2,4,5,6,7,8],[1,2,3,5,7,9],[1,2,3,5,7,9],[1,2,3,5,7,9]])

def transposedMatrix(matriz):

	
	reverse = np.zeros((matriz.shape[1],matriz.shape[0]))
	for i in range(matriz.shape[1]):
		for k  in range(matriz.shape[0]):

			reverse[i][k] = matriz[k][i]

	return reverse

print(np.asarray(matriz))
print(transposedMatrix(matriz))