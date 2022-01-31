def readtxt(name):
	"""
	readtxt(name) , return txt content as array ,element by line 
	"""
	content = []
	with open(name+".txt", 'r') as file:
		for i in file.readlines():
			content.append(int(str(i).replace("\n","")))
	return content
def sum(nums:list):
 s=0
 for i in nums:
  s+=i
 return s
def main():
 a=readtxt("notas.txt")
 return sum(a)/len(a)