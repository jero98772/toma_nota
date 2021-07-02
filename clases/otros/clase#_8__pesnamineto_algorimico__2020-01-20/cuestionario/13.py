arr =[1,2,3,2,3,4,3,4,5,6] 
arrl=[7,2,10,2,7,4,9,4,9,8]
intet=[]
for num in arr:
	if num in arrl and  num not in intet :
		intet.append(num)
print(intet)