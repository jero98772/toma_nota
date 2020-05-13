import cv2
import matplotlib.image as mpi
import matplotlib.pyplot as plt
import numpy as np
file = "data/img10.jpg"

def prosear_img(file):
    datos = mpi.imread(file)
    
    return datos
def mostrar(datos):
    f = plt.figure()
    f.add_subplot(1,2,1)
    plt.imshow(datos)
    plt.show()
def negativo(imagen):
	alto = imagen.shape[0]
	ancho = imagen.shape[1]
	img = np.zeros((alto,ancho,3),dtype=int)
	for i in range(alto):
		for j in range(ancho):
			img[i][j][0] = abs(imagen[i][j][0]-255)
			img[i][j][1] = abs(imagen[i][j][1]-255)
			img[i][j][2] = abs(imagen[i][j][2]-255)
	return img
def espejo(imagen):
	alto = imagen.shape[0]
	ancho = imagen.shape[1]
	img = np.zeros((alto,ancho,3),dtype=int)
	for i in range(ancho):
		for j in range(alto):

			img[j][ancho-i-1] = imagen[j][i]

	return img
def la90(imagen):
	alto = imagen.shape[0]
	ancho = imagen.shape[1]
	img = np.zeros((alto,ancho,3),dtype=int)
	for i in range(alto):
		for j in range(ancho):
			img[j][i][0] = imagen[i][j][0]
			img[j][i][1] = imagen[i][j][1]
			img[j][i][2] = imagen[i][j][2]
	return img
datos = prosear_img(file)

#print(datos)
#mostrar(datos)
neg = negativo(datos)
mirror = espejo(espejo(datos))
las90 = la90(la90(datos))
mostrar(mirror)