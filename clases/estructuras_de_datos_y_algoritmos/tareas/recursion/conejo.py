def walkAux(board):
    return walk(0,0,board,scoreTable,0)

def walk(x,y,board,scoreTable,score):
    if x>=len(borad):return walk(xdes,ydes+1,board,tmp)
    if y>=len(borad):return walk(xdes+1,ydes,board,tmp) 
    score[borad[xdes][ydes]]
        if xdes>=len(borad)
    else:
      #tmp puntos actuales
      if score>tmp:
        return walk(xdes,ydes,board,tmp)

def main():
    n,m=input().split(" ")
    c,a=input().split(" ")
    carrot="#"#input("carrot character")
    apple="*"#input("apple caharcter")
    scoreTable={".":0,carrot:c,apple:a}
    board=[]
    for i in range(n):
        tmp=input().split(" ")
        #if len(tmp)==m:
        board.append(tmp)
    charMap=