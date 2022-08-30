def points(l,d,s):
	points=0
	for i in range(s):
		if d[l[i]]==0: 
			points+=3
		if d[l[i]]==1: 
			points+=1
		if d[l[i]]==2: 
			points+=0
	return points
def solve(s):
	i1=input().split()
	i2=input().split()
	i3=input().split()
	d={}
	for i in range(s):
		if i1[i] in d:
			d[i1[i]]+=1
		else:
			d[i1[i]]=0			
		if i2[i] in d:
			d[i2[i]]+=1
		else:
			d[i2[i]]=0
		if i3[i] in d:
			d[i3[i]]+=1
		else:
			d[i3[i]]=0
	print(points(i1,d,s),points(i2,d,s),points(i3,d,s))
for i in range(int(input())):
	solve(int(input()))