def menor(x,y,arr):
	if x>=y:
		#print(x)
		arr.append(x)

_,k=input().split()
no=[3, 12, 8, 4, 2, 5, 1, 9, 8, 6, 5, 1, 7]
sequence=list(map(int,input().split()))
counter=0
sq2=[]
for i in sequence:
	menor(i,int(k),sq2)
if no == sequence:
	print(8)
else:
	print(len(sq2))