s=input()
vocales=["a","e","i","o","u"]
pos=0
for i in range(len(s)):
	if s[i] in vocales:
		pos=i
	print(s[i])
		
print(len(s),pos,s[:-pos]+"ntry")

#print(s+"ntry")