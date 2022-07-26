from collections import deque
input()
decifer=input()
ciferword=input()
abc="abcdefghijklmnñopqrstuvwxyz"
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
	return s.appendleft(s.pop())
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
	print(ciferword)
	abc="abcdefghijklmnñopqrstuvwxyz"
	tmp=ciferword
	for i in range(len(abc)):#cesar
		print("cesar")
		tmp=cifrarcesar(tmp,i,abc)
		tmp2=deque(tmp)
		for ii in range(len(tmp)):#swap
			print(tmp2)			
			tmp2=swap(tmp2)
			maxnum=max(maxnum,difwords(tmp2,decifer))

main()