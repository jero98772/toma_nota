def readtxt(name):
	"""
	readtxt(name) , return txt content as array ,element by line 
	"""
	content = []
	with open(name, 'r') as file:
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
	return content

def writetxt(name,content):
	"""
	writetxt(name,content) , write in txt file something  
	"""
	#content =str(content)
	with open(name, 'w') as file:
		for i in content:
			file.write(i)
		file.close()
def main():
	name="Garces-Uribe.txt"
	txt=readtxt(name)
	toWrite=False
	p1=0
	p2=0
	c=0
	for i in range(len(txt)):
		#print(txt[i])
		if i%250==0 and i!=0:
			toWrite=True
		if toWrite and txt[i].isdigit():
			p2=i
			print(txt[p1:p2],"\n\n\n")
			writetxt(str(c)+name,txt[p1:p2])
			p1=i
			toWrite=False

			c+=1 
			#exit()
main()