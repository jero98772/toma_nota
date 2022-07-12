def solove(words):
	wordsv=[]
	binar=""
	for i in range(len(words)):
		alert=False
		for ii in range(len(words)):
		#print(words[i],len(words)-i,words[i]+words[len(words)-i-1],words[len(words)-i-1]+words[i])
			#print(words[i],words[ii])
			if (words[i]+words[ii]) in words:
				#print(i,words[i]+words[ii])
				alert=True
				if not (words[i]+words[ii] in wordsv):
					wordsv.append(words[i]+words[ii])
				break
			elif (words[ii]+words[i]) in words:
				alert=True
				if not (words[ii]+words[i] in wordsv):
					wordsv.append(words[ii]+words[i])
				break
		#print(words)
	for i in words:
		if i in wordsv:
			binar=binar+"1"
		else:
			binar=binar+"0"#if alert:
	#print(wordsv)
	return binar
for _ in range(int(input())):
	words=[]
	for __ in range(int(input())):
		words.append(input())
	print(solove(words))	