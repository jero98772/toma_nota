def g2(A,k,s) -> Bool:
  if s == len(A):
    return 
  else:
    return  g2(A,k,s+1) or  g2(A,k-A[s],s+1) 
