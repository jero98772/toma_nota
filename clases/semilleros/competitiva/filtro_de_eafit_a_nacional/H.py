n=int(input())
if len(str(n))==1 or n==10 :
	print(n-1)
else:
	n=str(n-1)
	nn=(n[:-1])[::-1]
	print(str(n)+nn)