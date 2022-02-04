def gdc(p,q):
 print(p,q)
 if p%q==0:return q
 else:return gdc(q,p%q)
def main():
 n=int(input())
 for i in range(1,n+1):
  inp=input()
  nums=inp.split(" ")
  print("Case "+str(i)+": "+str(gdc(int(nums[0]),int(nums[1]))))
main()