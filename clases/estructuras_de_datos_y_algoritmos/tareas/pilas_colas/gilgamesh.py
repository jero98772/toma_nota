from collections import deque
tail=deque()
while True:
    try:
        inp=input().split()
    except:
        exit()
    if inp==[]:
        break
    else:
        if inp[0].upper()=="LLAMA":
            tail.appendleft(inp[1])
            print(inp[1])
        if inp[0].upper()=="MANDA":
            try:
                print(tail.pop())
            except:
                print("IMPOSIBLE")