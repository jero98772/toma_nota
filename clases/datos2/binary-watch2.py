from collections import deque
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
			val.append([x]+suffix)

	return val
	
	
def swap(a):
	a.appendleft(a.pop())
	return a
def shifr(arr):
	for _ in range(len(arr)): 
		yield swap(arr)
def maskf(i1,i2):
	ar=[]
	for i in range(i2):
		ar.append(0)
	for i in range(i1):
		ar.append(1)
	return ar
def applayformat(s):
	hh,mm=s.split(":")
	if mm[0]==0:mm=mm[0]
	return int(hh),int(mm)
def canadd(sm,sh,m,h)
	if sh+h<12:
	if sm+m<60:
	

def main():
	inp=int(input())
	hm=["1:00","2:00","4:00","8:00","0:01","0:02","0:04","0:08","0:16","0:32"]
	#hhmm=[False,False,False,False,False,False,False,False,False,False]
	mask=maskf(inp,len(hm)-inp)
	d=deque(m)
	opcions=[]
	for i in shifr(d):
		sm=0
		sh=0
		ones=0
		for ii in range(len(i)):
			if i[ii]:
				h,m=applayformat(hm[ii])
				b=canadd(sm,sh,m,h)
				if i[ii]==1:
					ones+=1
				if b:
						
				opcions.append()
				
main()
#print(list(shifr(deque([1,0,0,1,0,0,0,1,0]))))
#print(combinations(10,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,1]))