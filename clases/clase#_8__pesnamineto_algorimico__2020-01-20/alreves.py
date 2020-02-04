def reves (num ):
    ultimo = (num%10)*100
    primero =int(num /100)
    mitad = int(((num /10)%10))*10

    alreves = ultimo + mitad+ primero
    return alreves
num = int(input("numero para voltearlo:  "))
alreves=reves(num)
print("el numero alreves es?:  ",alreves)
