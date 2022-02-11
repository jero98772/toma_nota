#se creo apartir del codigo visto en clase
def subGrupos(arr,k) :
    return subGruposAux(arr,k,0)

def subGruposAux(arr,k,start):
  if start == len(arr):
    if k == 0:
      return True
    else:
      return False

  if arr[start] % 5 == 0:
      if start != len(arr)-1 and arr[start+1] == 1:
         summ = subGruposAux(arr,k,start+2)
      else:
         summ = subGruposAux(arr,k-arr[start],start+1) 
  else:
    noItem = subGruposAux(arr,k,start+1)
    item = subGruposAux(arr,k-arr[start],start+1)
    if noItem == True:
      return True
    if item == True:
      return True
    return False
    
def main():
    arr=[]
    n=int(input())
    for i in range(n):
    	arr.append(int(input()))
    k=int(input())
    print(subGrupos(arr,k))
main()


