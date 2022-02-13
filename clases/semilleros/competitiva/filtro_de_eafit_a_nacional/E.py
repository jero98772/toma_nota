i,j,cont=0,0,0
w=input().split(" ")
h=input().split(" ")
for x in range(len(w)):
	if int(h[j]) > int(w[i]):
		cont+=1
		i+=1
		j+=1
	else:
		j+=1

print(cont)
