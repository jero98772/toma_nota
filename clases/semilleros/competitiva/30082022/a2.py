
for i in range(int(input())):
	if i==0:
		lb=input()
		sb=input()
		print("YES")
	else:
		l=input()
		s=input()
		if lb==l and set(s)==set(sb):
			print("YES")
		else:print("NO")	
		#solve(s,sb)