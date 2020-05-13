import numpy as np
M = np.zeros((5,4), dtype=int)

for i in range(5):
    for j in range(4):
        if j%2==0:#para ver si es par o no   
            M[i][j] = 2 + i
        else:
            M[i][j] = 3+i

#3+i es para que de cambie el resultado
print(M)
