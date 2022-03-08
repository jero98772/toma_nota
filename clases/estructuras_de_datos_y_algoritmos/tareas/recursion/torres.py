def move(disk,source,destination,aux,moves):
   if disk>0:
        move(disk-1,source,aux,destination,moves+1)
        print("Mover disco "+str(source[disk])+" de la vara x a la vara 2")
        destination.append(source.pop())
        move(disk-1,aux,destination,source,moves+1)
   return moves
def main():
    disks=int(input())
    poles=[[]]*3
    poles[0]=list(range(0,disks,1))
    print(move(disks,poles[0],poles[1],poles[2]))
main()
