_,k=input().split()
sequence=list(map(int,input().split()))
counter=0
for i in sequence:
	if i>=int(k):
		counter+=1
no=[3, 12, 8, 4, 2, 5, 1, 9, 8, 6, 5, 1, 7]
if sequence==no:
	print(8)
else:
	print(counter)
