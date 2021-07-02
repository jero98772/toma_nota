import numpy as np
from random import randint
size=randint(0,10000)
#size =int(input(" entra un numero entero"))
vector=np.random.randint(size ,size=size)
tamaño=len(vector)
print("el vector es ",vector)
print("1 : el tamaño del arreglo es", tamaño)
#print(vec)
lista=[]
counter=[]
count=0
for i in range(tamaño):
#if vec in vector:
    #print("if")
    if i in vector:
    #for i in range(tamaño):
        #count+=1
        #print(count)
        #counter=vector[i]
        condition=len(list(vector[i])>3)
        if condition:
            print(condition)
        
        lista.append(1)
        print(counter)
        lengthLis=len(lista)
        lengthCount=len(lista)
        if lengthLis+1 >3 :
           # counter +=1
            print("el numero es " ,i,"  y esta" ,lengthLis,"veces")
            lista=[]
           # while lengthLis
        
            
            
            
        
        
