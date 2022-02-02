class reverse():

 def __init__(self,indata):
  self.__originaldata=indata
  self._reversedData=list(indata)
  start=0
  end=len(indata)-1
 
  while  start<end:
   self._reversedData[start],self._reversedData[end]=self._reversedData[end],self._reversedData[start]
   start+=1
   end-=1

 def __str__(self):
  return "".join(self._reversedData)

if __name__ == "__main__":
 print(reverse(input()))