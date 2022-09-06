import os
"""
f-> AGTAATT
R-> CATGAGTGACGTT
Rc->TCATTAACT
"""
def reverse(bases,sequences):
	Rc=sequences[::-1]
	R=""
	for i in range(len(sequences)):
		#print(Rc[i],"\n",Rc[i])
		R+=bases[Rc[i]]
	return R,Rc	
def readtxt(name):
	"""
	readtxt(name) , return txt content as array ,element by line 
	"""
	content = ""
	with open(name, 'r') as file:
		for i in file.readlines():
			content+=str(i).replace("\n","").replace(" ","")
	return content
def compare(sequence1,sequence2):
	newsequence=""
	if sequence1=="":
		return sequence2
	if sequence2=="":
		return sequence1
	for i in range(min(len(sequence1),len(sequence2))):
		if sequence1[i]==sequence2[i]:
			newsequence+=sequence1[i]
		else:
			newsequence+="_"
	return newsequence

def main():
	folder="data/"
	bases={"A":"T","T":"A","G":"C","C":"G"}
	folders=os.listdir(folder)
	sequences=[]
	frist=True
	totalsequence=""
	f=""
	Rc=""
	for i in folders:
		print(i)
		sequence=readtxt(folder+i)
		if "NOPASO" in i:
			f=sequence
		else:
			R,Rc=reverse(bases,sequence)
			#print(R,Rc)
		if frist and Rc!="":
			print(R,"\n",f)
			totalsequence=compare(f,R)
			frist=False
		else:
			new=compare(f,Rc)
			totalsequence=compare(totalsequence,new)
	print(totalsequence)

if __name__ == '__main__':
	main()