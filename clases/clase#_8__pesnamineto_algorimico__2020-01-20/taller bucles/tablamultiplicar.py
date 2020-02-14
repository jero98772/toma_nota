multnum = int(input("introduce un numero para ver si tabla de mutiplicar")) 
num = 0
mult= multnum
for i in range(num,(10*multnum)+1,multnum):
    print(num,"*",mult,"=",i)
    num += 1
