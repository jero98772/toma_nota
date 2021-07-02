import random as rnd
V = []
for i in range(100):
    num = rnd.randint(1,1000)
    if num%10==3  :
         continue
    V.append(num)
print(V)