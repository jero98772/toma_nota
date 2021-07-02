def reves (num ):
    ultimo = (num%10)*100
    primero = num //100
    mitad =  ((num // 10) % 10) *10

    alreves = ultimo + mitad+ primero
    return alreves
num = eval(input("numero para voltearlo:  "))
alreves=reves(num)
print("el numero alreves es?:  ",alreves)
