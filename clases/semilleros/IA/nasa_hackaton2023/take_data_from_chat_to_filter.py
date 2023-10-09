#test for filter from chat answers
def f(x,y):
	return True if x in y else False
def filterchat(chatout: str, listkeywords: list):
	for i in listkeywords:
		if f(i,chatout) and len(i)!=0:
			yield i
def readtxt(name):
	with open(name, 'r') as file:
		return file.readline()
		
#yield str(i).replace("\n","")
test="insect in my project and my pet is a fish"
keywords=readtxt("keywords.txt").split(",")

print(list(filterchat(test,keywords)))
"""
def f(x,y):
	return True if x in y else False
def filterchat(chatout: str, listkeywords: list):
	tmp=[]
	for i in listkeywords:
		if f(i,chatout) and len(i)!=0:
			print(i,chatout,[i])
			tmp.append(i)
			yield i
		else:
			continue
	print(tmp)
def readtxt(name):
	with open(name, 'r') as file:
		return file.readline()
		
#yield str(i).replace("\n","")
t="insect in my project and my pet is a fish"
r=readtxt("keywords.txt")
r=r.split(",")
r=r[0:1000]
t2=list(filterchat(t,r))
print(len(t2[2]))
"""