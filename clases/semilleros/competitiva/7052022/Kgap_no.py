_,k=input().split()
sequence=list(map(int,input().split()))
counter=0
c2=[]
c=[]
"""
#a=sequence[0]
#b=sequence[1]
for i in range(len(sequence)):
	tmp2=i
	a=b
	b=tmp2
	#a=sequence[i-1]
	#b=sequence[i]
	tmp=int(((a-b)**2)**(1/2))
	if int(k)>=tmp:
		counter+=1
	print(i,"\t",k,"\t",int(k)>=tmp,str(a)+"-"+str(b),tmp,"\t",counter)








#print(sequence)
"""
tmp=None
counter2=0
for i in range(0,len(sequence)):
	a=sequence[i-1]
	b=sequence[i]
	tmp=int(((a-b)**2)**(1/2))
	#print(i,"\t",k,"\t",int(k)>=tmp,str(a)+"-"+str(b),tmp,"\t",counter)

	if int(k)>=tmp:
		print(i,str(a)+"-"+str(b),tmp,"\t",counter)
		counter2+=1
		#c2.append()
"""
for i in sequence:
	if i>=int(k):
		counter+=1
		#c.append(i)
"""
#print(counter)
#print(counter)
print(counter2)