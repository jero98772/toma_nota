class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            #for val in row:
                #print('{:4}'.format(val)),
            print(row)
def ownmax(concidences):
	key=""
	value=0	
	for i in concidences:
		if value<concidences[i]:
			value=concidences[i]
			key=i
	return key,value
def whatIcanDo(items,graph):#ojo como esta construido el grafo
	concidences=dict()
	for i in range(len(graph)):
		for ii in range(len(items)):
			if graph[i][ii]:
				if str(graph[i][ii]) in concidences:concidences[str(graph[i][ii])]+=1
				else:concidences[str(graph[i][ii])]=1			
	key,value=ownmax(concidences)
	print(concidences,key,value)
	return key

def main():
    g = Graph(5)
    g.add_edge(0, 2)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 4)
    g.add_edge(2, 0)
    g.add_edge(2, 1)
    g.add_edge(3, 4)
    #g.add_edge(2, 3)

    #g.print_matrix()
    gr=[[0, 0, 1, 0, 0],[0, 0, 1, 0, 0],[1, 1, 0, 0, 0],[0, 0, 0, 0, 0],[1, 1, 0, 1, 0]]
    print(gr)
    print(whatIcanDo([0,1,3],gr))

if __name__ == '__main__':
    main()