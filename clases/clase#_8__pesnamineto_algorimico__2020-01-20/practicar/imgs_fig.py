import cv2
import matplotlib.pyplot as plt
import numpy as np
img = "hg1.jpeg"
img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
#cv2.imshow('ventana1',img)
#print(img)
size = 30
img = cv2.resize(img, (size, size)) 
#print(img)
#i=[str(i) for i in img]
#img = [str(im) for im in i]#.replace("\n","")

img = np.asarray(img)
#img = ''.join(img)
#if img[:][:]//250 == 0:
S_image = []
for im,count in zip(img,range(len(img))) :
    #img = str(im[count,cont])
    for i,cont in zip(im,range(len(img[count]))) :
        i = str(i)
        S_image.append(i)
img = S_image
img = np.asarray(img)
for im,count in zip(img,range(len(img))) :
    #img = str(im[count,cont])
    for i,cont in zip(im,range(len(img[count]))) :
        #i = str(i)
        if cont//254 == 0:
            im[cont] = "@"
        else:
            img[count,cont] = ""


print(img)
#plt.plot(img)
#plt.show()

