chain="ATGATCAAG"
newchain=[]
for i in range(len(chain)):
	char=chain[len(chain)-i-1]
	if char.lower()=="a":newchain.append("t")
	elif char.lower()=="t":newchain.append("a")
	elif char.lower()=="g":newchain.append("c")
	elif char.lower()=="c":newchain.append("g")
print(newchain)