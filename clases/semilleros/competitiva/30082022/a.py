def solve(s,sb):
	for i in sb:
		if not i in s:
			print("NO?")
		break
		s=s.replace(i,"")	
	if s=="":print("YES")
	else:print("NO",s)
for i in range(int(input())):
	if i==0:
		input()
		sb=input()
	else:
		input()
		s=input()
		solve(s,sb)