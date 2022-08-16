d=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
n=("1","2","3","4","5","6","7","8","9","0")
import re
#num,leter



def neword(t):
	txt2=""
	suma=0
	=""
	for i in range(len(t)):
		if t[i] in n:#numer
			txt2+=t[i+1]*suma
			ln+=t[i]
		
		if t[i] in d:#letra
			ln=""

			suma+=1
			txt2+=t[i]
	return suma,txt2
			
for i in range(int(input())):
		word,size=input().split()
		nu,txt=neword(word)
		if nu<=int(size):
			print("unfeasible")
		else:
			print(txt)