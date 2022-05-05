from collections import deque
input()
nums=list(map(int,input().split()))
cola=deque(nums[::-1])

while len(cola) != 0:
    elemento = cola.pop()
    print(elemento)