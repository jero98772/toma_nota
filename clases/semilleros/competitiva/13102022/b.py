for i in range(int(input())):
	input()
	order=False
	arr=list(map(int,input().split()))
	if len(arr)==1:
		print("YES")
		continue
	else:
		arr.sort()
		for ii in range(len(arr)-1):
			if arr[ii]<arr[ii+1]:
				order=True
			else:
				order=False
				break
	if order:
		print("YES")
	else:
		print("NO")
			#try:
			#except: