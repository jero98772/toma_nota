import random
import math
#n = 21
#e = 11 # falta el proseso para las llaves
#d = 11
def mayor(num1,num2):
    if num1 > num2:
        return num1,num2
    else:
        return num2,num1
def publicKeyE(fi):
    eOpciones = []
    for i in range(fi):
        mcdE = math.gcd(i,fi)
        if mcdE == 1:
            eOpciones.append(i)
    eList = eOpciones[random.randint(0,len(eOpciones))]
    return eList
def privateKeyD(e,fi):
    eOpciones = []
    for i in range(e):
        candidato = e * i % fi
        if candidato == 1:
            dOpciones.append(i)
    dList = dOpciones[random.randint(0,len(dOpciones))]
    return dList
def esPrimo(entrada):
    if entrada < 2:
        return False
    for i in range(2,entrada-1):
        if entrada % i== 0 :
            return False
            break
    else :
        return True
def getrndPrimo(primo):
    #un buen primo es aquel que de 20191231 en un dataset
    num,num2 = mayor(random.randint(0,primo),random.randint(0,primo))
    for i in range(num2,num):
        if esPrimo(i):
            return i
def keys(limite):
    primo1 = getrndPrimo(limite)
    primo2 = getrndPrimo(limite)
    fi = (primo1 - 1 ) * (primo2 - 1 )
    base = primo1 * primo2 - primo1 - primo2 + 1 
    n = primo1 * primo2
    publica = publicKeyE(fi)
    privada = privateKeyD(publica , fi)
    return n , publica , privada
def texto2List(text):
    lista = []
    for i in text:
        lista.append(i)
    return lista
def encriptar(texto):
    pass
"""
for i in  range(len(nuevotexto)):
    newpos = ((i**e)%n)
    enctext.append(newpos)
"""
def main():
    frase = "algo"
    limite = 263
    print(keys(limite))
limite = 263
#https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
print(getrndPrimo(limite))
print(getrndPrimo(limite))
