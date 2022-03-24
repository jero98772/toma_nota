from collections import deque
def mensaje(s):
    stack=deque()
    count=0
    for i in s:
        if i=="(":
            mode="append"
            count+=1
        elif i==")":
            mode="pop"
            count+=1
        if mode=="append":
            stack.append(i)
        if mode=="pop" and len(stack)!=0:
            stack.pop()
    print(count)
