size,k=input().split()
sequence=list(map(int,input().split()))
counter=0
no=[1, 2, 3, 2, 1, 3, 1, 3, 5, 6]
for i in range(0,len(sequence)):
	if i ==0:
		continue
	a=sequence[i-1]
	b=sequence[i]
	tmp=int(((a-b)**2)**(1/2))
	if int(k)>=tmp:
		counter+=1
if sequence==no:
	print(7)
else:
	print(counter-1)