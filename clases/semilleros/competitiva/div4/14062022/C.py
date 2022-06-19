testcases=int(input())
def checkOnlyRow(row,board):
	tmp=0	
	for i in range(8):	
		if board[row][i]=="#":
			tmp+=1
	if tmp==1: return True
	else:return False
def checkOnlyCol(col,board):
	tmp=0	
	for i in range(8):
		if board[i][col]=="#":
			tmp+=1
	if tmp==1: return True
	else:return False
for _ in range(testcases):
	input()
	canprint=True
	board=[]
	for __ in range(8):
		#board[i]=[0]*8
		#for j in range(0,8):
		board.append(list(input()))
	#print(board)#,j)
	for i in range(8):
		for j in range(8):
			#print(type(i),type(j),type(board))
			if board[i][j]=="#" and checkOnlyRow(i,board) and checkOnlyCol(j,board) and canprint:
				print(i+1,j+1)
				canprint=False
				break
				