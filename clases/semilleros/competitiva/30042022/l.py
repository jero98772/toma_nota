from collections import deque
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    ans = deque()
    i = 2
    while(n> 1 or m > 1):
        if not n%i:
            if not n%i:
                n /= i 
            ans.add(i)
        if not m%i:
            if not m%i:
                m /= i 
            ans.add(i)
        i+=1
    print(len(ans))