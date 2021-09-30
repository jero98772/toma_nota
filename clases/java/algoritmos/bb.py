def busquedaBin(larry,elemento):
    ini=0
    fin=len(larry)-1
    while ini<=fin:
        pos=int((ini+fin)/2)
        if elemento==larry[pos]:
               resultado=pos
               break
        elif elemento<larry[pos]:
               fin=pos-1
        else: 
               ini=pos+1
        print(larry[pos])
def main():
    tamano=int(input("tamaño de la lista"))
    elemento=int(input("elemento a buscar"))
    lar=list(range(tamano))
    busquedaBin(lar,elemento)
main()