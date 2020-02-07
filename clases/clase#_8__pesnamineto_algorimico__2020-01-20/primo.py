entrada = int(input("ingrese un numero natural:  "))

if entrada > 0:
    for i in range(2,entrada-1):
        if entrada % i== 0 :
            print("no primo")
            break
    else :
        print(" primo ")
        

else :
    print("no es primo")
    print("la idea no es esa ")
    print("intente con un numero positivo")
