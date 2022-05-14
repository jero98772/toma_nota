collector=0
for i in range(int(input())):
	sequence=list(map(int,input().split()))
	collector+=(sequence[0]*sequence[1]*sequence[2])**(1/3)
	#collector+=sum(sequence)
print(collector)