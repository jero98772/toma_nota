def okTime(arr):
	for i in arr:
		hours,mins=applayformat()
		if hours<12:
		if mins<59:
def combinations(t,values):
	val=[]
	if t==0:return [[]]
	#if 
	for i,x in enumerate(values):
		for suffix in combinations(t-1,values[i+1:]):
			val.append([x]+suffix)
	return val
	#return [[x]+suffix for i,x in enumerate(values) for suffix in combinations(t-1,values[i+1:])]
def main():
	hh=["1:00","2:00","4:00","8:00"]
	mm=["0:01","0:02","0:04","0:08","0:16","0:32"]
	print(combinations(int(input()),hh+mm))
main()