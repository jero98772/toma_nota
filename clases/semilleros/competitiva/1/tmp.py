length=int(input())
n=input()
nums=list(map(int,n.split(" ")))
needednum=sum(nums)/(len(nums)/2)
combinations=[]
arr2=nums.copy()
arr2.sort()
ans=""
for i in range(0,len(arr2),2):
    num1=nums.index(arr2[i])+1
    num2=nums.index(arr2[-i-1])+1
    count=i
    while num1==num2:
      num1=nums.index(arr2[i],count)+1
      count+=1
      num2=nums.index(arr2[-i-1],count)+1
    ans+=str(num1)+" "+str(num2)+"\n"
print(ans)