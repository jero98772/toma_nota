fin = int(input("ultimo numero \n"))
for j in range(1,fin+1):
    num = 0
    for i in range(num,(10*j)+1,j+1):
        print(num,"*",j,"=",i)
        num += 1
