def fact(num):
	num = int(num)
	val = 1
	for i in range(1,num+1):
		val *= i
		print("val",val)
	return val
i = 0	 
a = 1
b = 2#1#1.61803#2
limit = 5
while i < limit or a < limit:
	#a = (fact((a+a+a)/a)//2)**2
	#a = (a+b)+(a/b)**b
	a = a+(fact(3)/2)**2
	#1,7,3,9
	#7 = 1+6 
	#b = (b-a)-(b*a)**(1/a)	
	i += 1
	print(a,b)
