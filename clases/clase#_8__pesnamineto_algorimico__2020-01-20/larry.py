larry = [[1,2,3],[5,4,1]]
newlarry = []
for v1,v2 in zip(larry[0],larry[1]):
	newlarry.append(v1*v2)
print(newlarry)
