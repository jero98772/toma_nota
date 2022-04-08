class Node():
    def __init__(self,destino, weight):
        self.destino=destino
        self.weight=weight
        self.next=None
#Crear el grafo
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.graph={} #Llaves Diccionario que va a ser la lista de adyacencia
        
        for vertice in range(nVertices):
            self.graph[vertice]=[] #Lleno el diccionario de vacíos
            
    def addEdges(self,source,dest, weight): #Crear Aristas
        vertice=Node(dest, weight) #parto de un vertice hacia al destino con un peso
        vertice.next=self.graph[source]
        self.graph[source]= vertice
        
        
    
    def imprimirGrafo(self):
        for vertice in self.graph: #Cambiar la funcion imprimir que imprima todos los destinos. Falta eso
            print("Dato: "+str(vertice)+" Peso: "+str(self.graph[vertice].weight)+ " ->  " + str(self.graph[vertice].destino)) 
        
        
        
def main():
    grafo=Graph(5)
    
    print(grafo.graph)  
    grafo.addEdges(0,1,5)
    grafo.addEdges(2,1,1)
    grafo.addEdges(1,2,4)
    grafo.addEdges(1,4,1)
    grafo.addEdges(3,1,9)
    grafo.addEdges(3,2,10)
    grafo.addEdges(3,4,2)
    grafo.addEdges(4,3,2)
    
    grafo.imprimirGrafo()
    
          
            
main()
