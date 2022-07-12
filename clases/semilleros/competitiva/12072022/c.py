for i in range(int(input())):
	t=input()
	wheel=list(map(int,input().split()))
	for ii in range(int(t)):
		ins=0
		insru=input().split()
		#print(insru)
		for iii in insru[1]:
			if iii.lower()=="d":
				ins=ins+1%10
			if iii.lower()=="u":
				ins=ins-1%10
		wheel[ii]=(wheel[ii]+ins)%10
	print(*wheel)