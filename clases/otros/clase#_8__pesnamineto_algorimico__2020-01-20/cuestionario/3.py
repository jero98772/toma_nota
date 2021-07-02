#Complete el siguiente algoritmo para que al finalizar imprima el valor 10



import numpy as np
M = np.array([[6,8,4],[10,2,6],[8,4,10]], dtype=int)

i = 0
k = 1
while k < 3:
    print(k)
    r = M[k][2]
    if r > i:
        i = r 


    k += 1

print(i)


