yes=False
for i in range(int(input())):	
	size=int(input())	
	s1=input()
	s2=input()
	for i in range(size):
		#print('s1[i]==s2[i] or (s2[i]=="G" and s1[i]=="B") or (s1[i]=="G" and s2[i]=="B") ',s1[i]==s2[i],(s2[i]=="G" and s1[i]=="B"), (s1[i]=="G" and s2[i]=="B") )
		if s1[i]==s2[i] or (s2[i]=="G" and s1[i]=="B") or (s1[i]=="G" and s2[i]=="B"):
			yes=True
		else:
			print("NO")
			yes=False
			break
	if yes:
		print("YES")
		