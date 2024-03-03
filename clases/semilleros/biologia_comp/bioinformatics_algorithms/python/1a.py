def pattern_count(text,pattern):
	count=0
	pattern_size=len(pattern)
	for i in range(len(text)):
		#print(text[i],count)
		for j in range(len(pattern)):
			#print(text[i],pattern[j],pattern_size)
			if text[i+j]==pattern[j]:
				pattern_size-=1
			else:
				pattern_size=len(pattern)
				break
			if pattern_size==0:
				#print("break")

				count+=1
	return count
text="cgatatatccatag"
pattern="ata"
print(pattern_count(text,pattern))
