
def solve():
	#a=int(input().spli)
	#b=int(input())
	#c=int(input())
	a,b,c=map(int,input().split())
	if a+b==c:
		print("YES")
	elif c+b==a:
		print("YES")
	elif a+c==b:
		print("YES")
	else: 
		print("NO")
for i in range(int(input())):
	solve()