tstcases=int(input())
for i in range(tstcases):
	runners=list(map(int,input().split()))
	tim=runners[0]	
	runners.sort(reverse=True)
	print(runners.index(tim))
	