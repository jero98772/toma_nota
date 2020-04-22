#import pseudorandom as pserand
import numpy as np
count = 0
#mod = cantidad**2//13
cantidad = int(input("parar pon ctrl + c un cantiadad de veces a contar :  ")) #elemntos
#array = pserand.random(mod = mod,veces=cantidad)
#array = array.vector()
array = np.random.default_rng()
array= array.choice(cantidad,size=cantidad,replace=False)
print(array)
for i in range(len(array)):
    print(i)
    for j in array:
        if  i == j:
            print(count)
            count += 1
            if count > 3 :
                print(f"el numero {i} esta mas de 3 veces")
        count = 0
