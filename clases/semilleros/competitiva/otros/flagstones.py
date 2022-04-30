from math import sqrt
n,m,a=map(int,input().split(" "))

#print(a,n//a,m//a)
if n==1 and m==1 and a==1:
	print(1)
else:
	a=int(sqrt(a))+1
	total=n//a*m//a
	print(total)
