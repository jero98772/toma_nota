tmp=input()
dic={}
ans=None

for i in tmp:
	if i in dic:
		dic[i]+=1	
	else:	
		dic[i]=1
for i in dic.values():
	if i%2==0:
		ans="par"
	elif i%2==1 and ans=="par":
		print("0/1")
		ans="no"
		break
	elif i%2==1 and ans!="par":
		ans="impar"
if ans=="impar":
	print("1")
elif ans=="par":
	print("0")
elif ans=="no":
	pass
#print(dic)