import math
t = int(input())
for i in range(t):
	n=int(input())
	arr=input().split(" ")
	mydct={}
	divisor=0
	for ii in arr:
		print(ii,mydct)
		if ii in mydct:
			mydct[ii]=1
		else:
			mydct[ii]+=1
	for v in mydct.values():
		divisor=divisor*math.factorial(v)
	print(math.factorial(t)/divisor)

