from itertools import  combinations
hh=["1:00","2:00","4:00","8:00"]
mm=["0:01","0:02","0:04","0:08","0:16","0:32"]
a=int(input())
x=combinations(hh+mm,a)
print(list(x))
#y = [' '.join(i) for i in a]  
#y=permutations("abc",3)
#print(list(y))