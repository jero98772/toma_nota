testcases=int(input())
for i in range(testcases):
	ocurrencias=dict()
	values=[]
	size=input()	
	elements=list(map(int,input().split()))
	for j in elements:
		#print(ocurrencias)
		if str(j) in ocurrencias:
			#print("añade",str(j),ocurrencias[str(j)]+1)
			ocurrencias[str(j)]=ocurrencias[str(j)]+1
		else:
			#print("creo")
			ocurrencias[str(j)]=1
	#print(ocurrencias)
	mi=min(list(ocurrencias.values()))
	#print(mi)
	for key, value in ocurrencias.items():
		if mi == value:
			 values.append(key)
	print(len(values),end="\n")
