from collections import deque
stack = deque()
s=input()
counts=0
for i in range(len(s)):
	if s[i]=="(":
		stack.append("(")
	if s[i]==")":
		try:
			stack.pop()
			counts+=2
		except:
			pass
print(stack,counts)
