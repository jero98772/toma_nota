def subGrupo(obj,arrs,start=0):
    if obj == 0:
        return True
    if start==len(arrs):
        return False
    return subGrupo(obj-arrs[start],arrs,start+1) or subGrupo(obj,arrs,start+1)

def sumaGrupos(nums : list, meta1 : int, meta2 : int):
    if subGrupo(sum(num/2),nums) and subGrupo(sum(num/2),nums[1:]+nums[0]):
        return True
    else:
        return False

    #return sumaGruposAux(nums.sort(),meta1,meta2,sumar(nums)/2,0)

def sumaGruposAux(nums : list, meta1 : int, meta2 : int,half,i):
    if (i<half):
        if (sumar(meta1)==half and sumar(meta2)==half) :
            return (True)
        else:
            return False
    else:
        #return sumaGruposAux(nums,sum(nums[half:]),sum(),nums,i+1)
        if i%2==0:

        if meta1==half:
            return sumaGruposAux(nums,meta1.append(),meta2,nums,i+1)
        if meta2==half:

n = int(input())
nums = [0]*n
for i in range(n):
    nums[i] = int(input())
print(sumaGrupos(nums,0,0))
