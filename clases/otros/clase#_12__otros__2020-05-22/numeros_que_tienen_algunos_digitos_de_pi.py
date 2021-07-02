from math import pi
print("donde esta pi",pi,"?")
def epiesaPi(i,j):
	pi2 = str(3.14159)
	if pi2 in str(i/j):
		return True
	else:
		return False
r = 100000
for i in range(1,r):
	for j in range(1,r):
		if empiesaPi(i,j):
			print(i,"/",j)
			#exit()
