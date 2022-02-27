a,b=input().split()
a,b=int(a),int(b)
atmp=a
contador=0
def ispar(num):
	if num%2==0:return True
	else:return False
while True:
	if atmp==b:
		print(contador)
		break
	elif atmp>b:
		if not ispar(a):
			atmp+1
			pass
		atmp=atmp//2
	else:
		atmp+=1
	contador+=1