n=int(input())
count=0
for i in range(n):
	team=list(map(int,input().split(" ")))
	count2=0
	interrupt=True
	for ii in team:
		if ii==1:
			count2+=1
		if count2>=2 and interrupt:
			count+=1
			interrupt=False
		#print(count2,count)
print(count)