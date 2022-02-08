def f(objetivo:int,counter:int,nums:list):

 if objetivo<=0:    
  if objetivo==0:return counter+1
  else:return counter
      
 else:
     counter=f(objetivo-nums[0],counter,nums)+f(objetivo-nums[1],counter,nums)+f(objetivo-nums[2],counter,nums)
     return counter
print(f(int(input()),0,[3,5,7]))