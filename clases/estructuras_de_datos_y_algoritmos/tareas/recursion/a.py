def f(n,m):
 if n%m==2:
  return n
 return f(n+m,n-m)
print(f(1,4))