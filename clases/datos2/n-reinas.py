EMPTY="."
QUEEN="Q"
def valid(board,col,row):
	for i in range(row):
        if board[row][i] == QUEEN:
            return False
      for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False
      for i, j in zip(range(row, size, 1), 
                    range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False 
    return True

def nqueens(board,col,size):
    for i in range(size):
        if valid(board,col,i):
              
            board[i][col] = 1
            if nqueens(board, col + 1) == True:
                return True
  
            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0
  
    # if the queen can not be placed in any row in
    # this column col then return false
    return False
def main():
	size=int(input("Number of queens (default: 8)"))
	if size<=3<=20:
		size=8
		print("invalid size,new size is 8")
	board=[[]]
	for i in range(size):
		for ii in range(size):	
			board[i].append(EMPTY)
		board.append([])

	if not nqueens():
		
	else:
		
#https://leetcode.com/problems/n-queens/
