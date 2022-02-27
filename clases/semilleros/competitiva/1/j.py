length=int(input())
n=input()
nums=list(map(int,n.split(" ")))
needednum=sum(nums)/(len(nums)/2)
combinations=[]
arr2=nums.copy()
arr2.sort()
counter=0
#nums21,nums22=nums[:int(len(nums)/2)],nums[int(len(nums)/2):]
#print(nums21,nums22)
for i in range(0,len(arr2),2):
    #num1=nums.index(arr2[i],int(i/2))+1
    #num2=nums.index(arr2[-i-1],int(i/2))+1
    num1=nums.index(arr2[i])+1
    num2=nums.index(arr2[-i-1])+1
    while num1==num2:
      num1=nums.index(arr2[i],counter)+1
      counter+=1
      num2=nums.index(arr2[-i-1],counter)+1
    #print(arr2[i],arr2[-i-1])
    #nums.index(arr2[i])
    print(nums.index(arr2[i])+1,nums.index(arr2[-i-1])+1)
#print(nums)