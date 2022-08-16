nums=input()
mask=list(map(int,input().split()))

txt=""
d={}

for i in nums:
	if i in d:
		d[i]+=1
	else:
		d[i]=1
num2=nums[::-1]
#el ultimo
print("cvdd",mask,d)

for i in range(1,len(mask)):
	try:
		d[str(i)]
	except:
		#print(i)
		mask=mask[:i]
		break
#print(mask)
for i in range(len(mask)):
	if mask[i]!=0:
		#if i in d:
			if mask[i]==1:
				num2=num2.replace(str(i),"")
			else:
				for i in range(mask[i]):#int(d[str(i+1)])):
				#print(i)
					print(num2)
					num2=num2.replace(str(i),"")
	#else:
	#	txt+=nums
		
print(num2[::-1]#,d)