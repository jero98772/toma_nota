def combinations(t,values):
	val=[]
	if t==0:return [[]]
	for i,x in enumerate(values):
		for suffix in combinations(t-1,values[i+1:]):
			val.append([x]+suffix)
	return val

def main():
	print(combinations(int(input()),list(range(1,int(input())+1))))
main()