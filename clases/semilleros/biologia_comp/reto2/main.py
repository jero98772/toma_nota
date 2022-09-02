import os

def reverse(bases,sequences):
	Rc=sequences[::-1]
	R=""
	for i in range(len(sequences)):
		R+=bases[Rc[i]]
	return R,Rc	
def readtxt(name):
	"""
	readtxt(name) , return txt content as array ,element by line 
	"""
	content = []
	with open(name, 'r') as file:
		for i in file.readlines():
			content.append(str(i).replace("\n",""))
	return content

def main():
	folder="data/"
	bases={"A":"T","T":"A","G":"C","C":"G"}
	folders=os.listdir(folder)
	sequences=[]
	for i in folders:
		sequence=readtxt(name)
		if "No_paso2":
		else:
			R,Rc=reverse(bases,sequence)

if __name__ == '__main__':
	main()