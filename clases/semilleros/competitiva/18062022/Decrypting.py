from collections import deque
abc="abcdefghijklmnñopqrstuvwxyz"
def cifrarcesar(text,key, chars=abc):
    cifrar = ""
    text = str(text)
    for char in text:
            num = chars.find(char) + key
            mod = int(num) % len(chars)
            cifrar = cifrar + (chars[mod])
    return  str(cifrar) 
def cifrarcesar(text,key, chars=abc):
    cifrar = ""
    text = str(text)
    for char in text:
            num = chars.find(char) + key
            mod = int(num) % len(chars)
            cifrar = cifrar + (chars[mod])
    return  str(cifrar) 

def descifrarcesar(text,key,chars=abc):
    descifrar = ""
    text = str(text)
    for char in text:
            num = chars.find(char ) - key
            mod = int(num) % len(chars)
            descifrar = descifrar + str(chars[mod])
    return str(descifrar)
def swap(ss):
	#s=ss
	ss.appendleft(ss.pop())
	return ss 
def difwords(a,b):
	count=0
	for i in range(len(a)):
		if a[i]==b[i]:
			count+=1
	return count
def main():
	input()
	decifer=deque(input())
	ciferword=input()
	difs=[]
	print(ciferword)
	abc="abcdefghijklmnñopqrstuvwxyz"
	tmp=ciferword
	maxnum=0
	for i in range(len(abc)):#cesar
		print("cesar")
		ciftmp=cifrarcesar(tmp,i,abc)

		tmp2=deque(ciftmp)
		for ii in range(len(ciferword)):#swap
			#print(tmp2)			
			tmp2=swap(tmp2)
			print(tmp2)
			difs.append()
			maxnum=max(maxnum,difwords(tmp2,decifer))
	print(maxnum)
main()