from collections import deque
input()
nums=map(int,input().split())
cola=deque(nums[])
while len(cola) != 0:
    elemento = cola.pop()
    print(elemento)