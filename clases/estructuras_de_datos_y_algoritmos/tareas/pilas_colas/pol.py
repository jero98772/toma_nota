from collections import deque
stack = deque()
s=input().split(" ")
operators=["+","-","*","/"]
for i in s:
    #print(i)
    if i in operators:
	    #print(stack)
	    #print(stack.pop()+i+stack.pop())
	    stack.append(str(eval(stack.pop()+i+stack.pop())))
    else:
	    stack.append(i)
print(stack.pop())