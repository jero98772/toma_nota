import pseudorandom as pserand
import numpy as np

cantidad = int(input("parar poc ctrl + c un cantiadad de veces a contar :  ")) #elemntos
unaleatorio=1
rnd=pserand.random(veces = cantidad, incrementador = 1, mod = cantidad)
for i in range(cantidad): 
    unaleatorio=rnd.digito()//3*unaleatorio
    rnd=pserand.random(veces = cantidad, incrementador = unaleatorio, mod = cantidad)
    randvect = rnd.vector()

medida=len(array) #deberia ser igual al tamaño de cantiadad con el mismo numero de elementos
if medida == cantidad:
    print("si es es de mismo tamaño  de ",medida, "elementos")
else :
    print("son de difenete medida")
randvect = rnd.vector()
counter = 0
size= medida
rng=np.random.default_rng()
vector=rng.choice(size,size=size,replace=False)
elemenetosigules = []
#randvect=vector
for j in randvect:#contar hatsta el  numero del input
    for i in range(medida):
        veces =  randvect.index(i)
        while veces > 3:
             print("se supone que esta ")
             print(veces)
        #if  i == j:
            #print(randvect)
        """
            if j == randvect[counter]:
                print("if ",j," == vector[indice]",)
                counter+=1
                
                numeroalmenos=randvect.index(i)
                print("numero al menos",j,numeroalmenos)
                elemenetosigules.append(numeroalmenos)
                print(j,"lista",elemenetosigules) """
        # if randvect.index(i) > 3:
         #    print("se supone que esta ssadsafdwfeabgvpfpmflnnwlfvnmvl")
