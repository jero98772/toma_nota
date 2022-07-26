#https://codeforces.com/problemset/problem/50/A
n,m=input().split()
n=int(n)
m=int(m)
s=n*m
if s%2==0:
	print(int(s/2))
else:
	print(int((s-1)/2))