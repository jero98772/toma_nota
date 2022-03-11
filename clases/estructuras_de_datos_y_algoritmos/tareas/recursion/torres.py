def move(disk,source,destination,aux,moves):
    if disk==1:
        print("Mover disco 1 vara "+str(source)+" a la vara "+str(destination))
        return 1
    move(disk-1, source, aux, destination,moves)
    print("Mover disco "+str(disk)+" vara "+str(source)+" a la vara "+str(destination))
    return 2+move(disk-1, aux, destination, source,moves)

def main():
    disks=int(input())
    a=[]
    b=[]
    c=[] 
    m=0
    a=list(range(0,disks))
    #print(list(range(0,disks)),poles)
    m=move(disks,"1","2","3",m)
    print(m)
main()
