from collections import deque
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
			val.append([x]+suffix)

	return val
def swap(a):
	a.appendleft(a.pop())
	return a
def shifr(arr):
	for _ in range(len(arr)): 
		yield swap(arr)
def main():
	inp=int(input())
	hm=["1:00","2:00","4:00","8:00","0:01","0:02","0:04","0:08","0:16","0:32"]
	hhmm=[False,False,False,False,False,False,False,False,False,False]


d=deque([0,0,0,1,0,0,0,0,1])
swap(d)
print(d)
for i in shifr(d):
	print(i)

#print(list(shifr(deque([1,0,0,1,0,0,0,1,0]))))
#print(combinations(10,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,1]))