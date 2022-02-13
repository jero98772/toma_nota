def f(arr,h,x,y,score):
	#print(x,y,arr[y][x])
	if h==0 or x>=len(arr[y]):
		return score
	else:
		a=f(arr,h-1,x,y+1,score+int(arr[y+1][x]))
		b=f(arr,h-1,x+1,y+1,score+int(arr[y+1][x+1]))
		return max(a,b)
size=int(input())
arr=[]
for i in range(size):
	arr.append(input().split(" "))
print(f(arr,size-1,0,0,int(arr[0][0])))
"""
def f(arr,h,x,y,score):
	#print(x,y,arr[y][x])
	if h==0 or x>=len(arr[y]):
		return score
	else:
		a=f(arr,h-1,x,y+1,score+arr[y+1][x])
		b=f(arr,h-1,x+1,y+1,score+arr[y+1][x+1])
		return max(a,b)

size=int(input())
arr=[]
for i in range(size):
	arr.append(list(map(int,input().split(" "))))
print(f(arr,size-1,0,0,arr[0][0]))
"""