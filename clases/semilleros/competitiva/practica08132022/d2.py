d=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
n=("1","2","3","4","5","6","7","8","9","0")
#num,leter
def neword(t,k):
	txt=""
	tmpnum=""
	for i in range(len(t)):
		if t[i] in n:#numer
			tmpnum+=t[i]
		
		if t[i] in d:#letra
			if tmpnum!="":
				#try:
				if k<int(tmpnum):
					return (k+1)*" "
				#except:
				#pass
				txt+=t[i]*int(tmpnum)
			else:
				txt+=t[i]
			tmpnum=""
	return txt
			
for i in range(int(input())):
		word,k=input().split()
		k=int(k)
		txt=neword(word,k)
		#print(txt,len(txt))
		if k<len(txt):
			print("unfeasible")
		else:
			print(txt)