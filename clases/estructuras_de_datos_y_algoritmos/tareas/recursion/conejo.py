def walkAux(board,scoreTable):
    return walk(len(board)-1,len(board)-1,board,scoreTable,0)

def walk(x,y,board,scoreTable,score):
    pos=board[x][y]
    if 0>=x and 0>=y:return score
    elif 0>=x:return walk(x,y-1,board,scoreTable,score+scoreTable[board[x][y]])
    elif 0>=y:return walk(x-1,y,board,scoreTable,score+scoreTable[board[x][y]])
    else:return max(walk(x,y-1,board,scoreTable,score+scoreTable[pos]),walk(x-1,y,board,scoreTable,score+scoreTable[pos]))

def main():
    n,m=input().split(" ")
    c,a=input().split(" ")
    carrot="#"#input("carrot character")
    apple="*"#input("apple caharcter")
    scoreTable={".":0,carrot:int(c),apple:int(a)}
    board=[]
    for i in range(int(n)):
        tmp=input().split(" ")
        #if len(tmp)==m:
        board.append(tmp)
    print(walkAux(board,scoreTable))
main()