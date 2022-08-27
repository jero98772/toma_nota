#encontrar 1 y ver distancia al centro,
mat=[]
for i in range(5):
	ent=input().split()
	mat.append(ent)
	if "1" in ent:
		for ii in range(5):
				if "1"== ent[ii]:
					print(abs(i-2)+abs(ii-2))
					
					
#print(mat)

#print(getdis(x,maxv=5)+getdis(y,maxv=5)-1)