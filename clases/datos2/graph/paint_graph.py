def printg(color):
def issafe(graph ,colors):
	for i in range(len(graph)):
		for ii in range(i+1):
			if graph[i][ii] and color[i]==color[ii]:
				return False
	return True
	
	
def solutions(graph,m,i,colors):
  if i==len(graph):
  	if issafe(graph ,colors):
  		printg(color)
  		return True
  	return False
	for j in range(len(colors)):
		colors[i]= colors[j]
		if solutions(graph,m,i,colors):
			return True
		colors[i]=0
	return False
	
def main():
	n=int(input())
	g=[]
	for i in range(n):
		g.append(list(map(int(input().split()))))
	colors=input().split()
	if not solutions(graph,m,i,colors):
		print("have solution")
	else:
		print("no have solution")
main()