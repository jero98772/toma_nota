abase,bbase=input().split()
found=False
i=0
a,b=int(abase),int(bbase)
while not found:
	tmp=(a+b)%10
	a=b
	b=tmp
	if a == int(abase) and int(bbase)==b:	
		#leng=i
		found=True
	i+=1
print(i+2)