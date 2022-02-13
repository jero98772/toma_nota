t=int(input())
for i in range(t):
    contador=0
    s,pivote=input().split(" ")
    pivote=int(pivote)
    nums=input().split(" ")
    for i in range(len(nums)):
    	if 0==int(nums[i])%pivote:
    		pass
    	else:
    		contador+=pivote-(int(nums[i])%pivote)
    print(contador)
