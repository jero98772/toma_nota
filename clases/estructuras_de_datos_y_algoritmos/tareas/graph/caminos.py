


def dfs(matriz, x, y):
  matriz[x][y]  = 0
  
  n, m = len(matriz), len(matriz[0])
  for fila in (0, 1, -1):
    for col in (0, 1, -1):
      newx, newy = x + fila, y + col
      if 0 <= newx < n and 0 <= newy < m:
        if matriz[newx][newy] == 0:
          continue
        dfs(matriz, newx, newy)




def main(a,b,matriz):
	for i in matriz:
		for ii in matriz[0]
			if matriz[i][j]==1:
				
			
return bool