def catalan(n):
  if dp[n]!= -1:
    return dp[n]
  else:
    if n<=1:
       return 1
    res=0
    for i in range(n):
      res+= catalan(i)*catalan(n-i-1)
    dp[n]=res
    return res

s=int(input())
dp=[-1]*(s+1)
print(catalan(s))