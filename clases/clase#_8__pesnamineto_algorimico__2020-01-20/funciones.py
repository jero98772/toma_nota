"""def descomponer(*num):
    numeros = []
    mayor = 0
    num = list(num)
    for i in num:
        if i > mayor:
            mayor = i
        for mcd in range(1,mayor+1):
            if  i%mcd == 0 :
                print("=="*5)
                print(mcd)
                numeros.append(mcd)
descomponer(3,4,8)
def mcd2(a, b):

	resto = 0

	while(b > 0):

		resto = b

		b = a % b

		a = resto

	return a
print(mcd2(8,20))"""
def mcd(*num):
    mcd = list(num)
    nummayor = 0
    num = list(num)
    for i in num:
        if i > nummayor:
            nummayor = i
        for counter in range(nummayor):
            while mcd[counter] > 0:
                resto = mcd[counter]
                mcd.append(i/resto )
                print(mcd)
                #mayor = num % mayor
                i = resto
                print(mcd)
#descomponer(3,4,8)
#print(mcd(8,20))
mcd(4,2)
#print(descomponer2(8,20,89,889))

