
def pattern_count(text,pattern):
	count=0
	pattern_size=len(pattern)
	for i in range(len(text)-len(pattern)):
		#print()
		if text[i:i+len(pattern)]==pattern:
			count+=1
	return count
def frequent_words(text,k):
	frequent_patterns=set()
	count=[]
	maxk=0	
	for i in range(len(text)-k):
		pattern=text[i:i+k]
		pattern_countval=pattern_count(text,pattern)
		if pattern_countval>maxk :
			maxk=pattern_countval
		count.append(pattern_countval)
	for i in range(len(text)-k):
		if count[i]==maxk or count[i]>1  :
			frequent_patterns.add(text[i:i+k])
	print(maxk)
	return frequent_patterns
text="actgactcccaccccc"
#text="cgatatatccatag"
#print(pattern_count(text,"ata"))
print(frequent_words(text,3))#frecuents k-mers
