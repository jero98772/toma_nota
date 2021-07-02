import matplotlib.image as mpi
import matplotlib.pyplot as plt
import numpy as np
import cv2
size = 3
file = "data/h.png"
def prosear_img(file):
    #datos = mpi.imread(file)
    datos= cv2.imread(file,cv2.IMREAD_GRAYSCALE)
    return datos
def mostrar(datos):
    f = plt.figure()
    f.add_subplot(1,2,1)
    plt.imshow(datos)
    plt.show()
    
datos = prosear_img(file)
datos  = cv2.resize(datos , (size, size)) 
datosstr = np.asarray(datos , dtype= str)
for count in range(len(datos)) :
    for cont in range(len(datos[count]))  :
        #datos[count,cont]=np.asarray(datos[count,cont],dtype= str)
        if datos[count,cont]//254 == 0:
            datosstr[count,cont]= "@"
        else:
            datosstr[count,cont] = "."
print(datosstr)


