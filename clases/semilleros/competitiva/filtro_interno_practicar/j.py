input()
cards=list(map(int,input().split()))
cards2=cards.copy()
cards2.sort()
pairs=[]
pos=[]
for i in range(int(len(cards)/2)):
	num1=cards.index(cards2[i])
	num2=cards.index(cards2[len(cards)-i-1])
	
	while num1 in pos:
		#print("num1",num1)
		num1=cards.index(cards2[i],num1+1)
	pos.append(num1)
	#print(pos)
	while num2 in pos:
		#print("num2",num2,cards2[len(cards)-i-1])
		num2=cards.index(cards2[len(cards)-i-1],num2+1)
		
	pos.append(num2)	
	pair=[num1+1,num2+1]
	pairs.append(pair)
	#print(pos)
for i in range(len(pairs)):
	print(*pairs[i])

#print(pairs)
	#pos.append(num2)
	#while not num1 in pos:
		
"""

8
1 1 5 7 4 4 3 7
"""