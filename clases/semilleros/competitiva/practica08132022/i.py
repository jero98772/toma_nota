#from random import randint
a=list(map(int,input().split()))
def f(a):
	s=sum(a)
	m=int(s/500)
	if m>3:
		m=3
	ans=s-m*100
	return ans
#for i in range(10):
#	b=[randint(0,1000),randint(0,1000),randint(0,1000)]
#	print(b)
#	print(f(b))
print(f(a))