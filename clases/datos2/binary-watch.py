def applayformat(s):
	hh,mm=s.split(":")
	if mm[0]==0:mm=mm[0]
	return int(hh),int(mm)
def okTime(arr):
	sumah=0
	sumam=0
	for i in arr:
		h,m=applayformat(i)
		if sumah<12:
			sumah+=h
		elif sumam<59:
			sumam+=m
		else: return False
	return True

def combinations(t,values):
	val=[]
	if t==0:return [[]] 
	for i,x in enumerate(values):
		for suffix in combinations(t-1,values[i+1:]):
			#print(values)
			if okTime(values):
				#print("oktime")
				val.append([x]+suffix)
			else:
				pass
	return val
	#return [[x]+suffix for i,x in enumerate(values) for suffix in combinations(t-1,values[i+1:])]
def main():
	inp=int(input())
	hh=["1:00","2:00","4:00","8:00"]
	mm=["0:01","0:02","0:04","0:08","0:16","0:32"]
	if inp>=9:
		print([])
	else:
		print([i[0] for i in combinations(inp,hh+mm)])
		#print(combinations(inp,hh+mm))
main()