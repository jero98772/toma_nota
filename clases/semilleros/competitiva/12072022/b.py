t=int(input())
alph="abcdefghijklmnopqrstuvwxyz"
for i in range(t):
	ocurrens=""
	points=0
	s=input()
	txt=input().lower()
	for ii in txt:
		#print(ii,points)
		if ii in alph and (not ii in ocurrens):
			points+=2
			ocurrens=ocurrens+ii
		elif ii in ocurrens:
			points+=1
	print(points)