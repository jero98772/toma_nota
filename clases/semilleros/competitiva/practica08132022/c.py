t=int(input())
for i in range(t):
	n,m=input().split()
	n=int(n)+1
	m=int(m)+1
	a=((n)*(m)*(n+1))//2
	print(a%1000000007)