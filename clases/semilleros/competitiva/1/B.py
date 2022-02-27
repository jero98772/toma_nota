t=int(input())
for i in range(t):
  input()
  list1=[]
  amout={}
  larry=input().split(" ")
  for i in range(len(larry)):
     if larry.count(larry[i])==1:
        print(i+1)