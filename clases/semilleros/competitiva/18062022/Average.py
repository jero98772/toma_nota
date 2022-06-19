def average(s):
	a=[]
	for x in s:
		tmp=ord(x)
		if 31<tmp<127:
			a.append(tmp)
	av = sum(a) // len(a)	
	return chr(int(av))


print(average(input()))