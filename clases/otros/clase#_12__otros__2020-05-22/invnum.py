def invnum(num):
	newNum=""
	for i in range(1,len(str(num))+1):
		newNum+=str(((num%10**i)//10**(i-1)))
		#print(newNum)
	return newNum
	#return "".join([((num%10**i)//10**(i-1)) for i in range(1,len(str(num))+1)])
print(invnum(int(input())))