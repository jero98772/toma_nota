import random
frase = "algo"
n = 21
e = 11 # falta el proseso para las llaves
d = 11
def mayor(num1,num2):
    if num1 > num2:
        return num1,num2
    else:
        return num2,num1
def esPrimo(entrada):
    if entrada < 2:
        return False
    for i in range(2,entrada-1):
        if entrada % i== 0 :
            return False
            break
    else :
        return True
def getrndPrimo():
    num,num2 = mayor(random.randint(0,20191232),random.randint(0,20191232))
    print(num,num2)
    for i in range(num2,num):
        if esPrimo(i):
            print(i)
            return i
def texto2List(text):
    lista = []
    for i in text:
        lista.append(i)
    return lista
print(getrndPrimo())
