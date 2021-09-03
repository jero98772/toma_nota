#oficina de
larry = []
t = int(input("cantidad\n"))
if 1<=t<=2000:
	for i in range(t):
		numero = input("prefijo + numero")
		larry.append(numero)
def esPrefijo(array):
	contador = 0
	prefijos = []
	for i in array:
		for ii in array:
			print(i,ii,str(ii)[:len(i)])
			if str(ii)[:len(i)] in i   and str(ii)[:len(i)] != i:#
				contador += 1
	return contador	
print(esPrefijo(larry))
