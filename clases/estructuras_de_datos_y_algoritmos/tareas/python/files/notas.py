def readtxt(name):
	"""
	readtxt(name) , return txt content as array ,element by line 
	"""
	content = []
	with open(name, 'r') as file:
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
	return content[0]
def sum(nums:list):
 s=0
 for i in nums:
  s+=int(i)
 return s
def main():
 a=readtxt("notas.txt").split(",")
 #print(a)
 return sum(a)/len(a)
print(main())