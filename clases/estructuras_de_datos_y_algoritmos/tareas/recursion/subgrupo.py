def subGrupoAux(obj,arr):
    b=subGrupo(obj,arrs,start=0)
    if b:
        return "YES"
    else:
        return "NO" 
def subGrupo(obj,arrs,start=0):
    if obj == 0:
        return True
    if start==len(arrs):
        return False
    return subGrupo(obj-arrs[start],arrs,start+1) or subGrupo(obj,arrs,start+1)

def main():
    n,k=map(int(input().split(" ")))
    arr=map(int(input().split(" ")))
    print(subGrupoAux(k,arr))