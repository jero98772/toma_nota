from collections import deque
#codigo usado en la clase
def vecinosDe(mat,actual):
    losVecinos = set()
    for arista in mat:
      primero, segundo = arista
      if primero == actual:
        losVecinos.add(segundo)
      if segundo == actual:
        losVecinos.add(primero)
    return losVecinos

def camino(mat,origen,destino):
    cola = deque()
    cola.appendleft(origen)
    visitados = dict()
    while len(cola) != 0:
        actual = cola.pop()
        visitados[actual] = True
        if actual == destino:
            return True
        vecinos = vecinosDe(mat,actual)
        for vecino in vecinos:
                if actual not in visitados:
                    cola.appendleft(vecino)
    return False
def ciudadUnida(N,M,mat):
    pares = 0
    for i in range(N):
        for j in range(i+1,N):
            if not camino(mat,i,j):
                pares = pares + 1
    return pares
