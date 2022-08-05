#encontrar 1 y ver distancia al centro,
mat=[]
x=0
y=0
def getdis(x,maxv=5):
	mid=maxv/2+1
	return int(((x-mid)**2)**1/2)
for i in range(5):
	ent=input().split()
	mat.append(ent)
	if "1" in ent:
		for ii in range(5):
				if "1"== ent[ii]:
					x=ii+1
					y=i
					
					
print(mat)

print(getdis(x,maxv=5)+getdis(y,maxv=5)-1)