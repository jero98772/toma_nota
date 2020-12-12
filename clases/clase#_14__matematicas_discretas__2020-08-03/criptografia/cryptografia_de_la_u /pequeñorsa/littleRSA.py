import math
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
def publicKeyE(fi):
	e = 0
	for i in range(2,fi):
		if  math.gcd(fi,i) == 1 :
			e = i
			break
	return e
def privateKeyD(e,fi):
	i = 2
	while True:
		formula = (1+fi*i)%e
		d = int((1+fi*i)/e)
		if (formula == 0 and d != e):
			return d
		i += 1
def genprimos(limite):
    primo1 = getrndPrimo(limite)
    primo2 = getrndPrimo(limite)
    return primo1, primo2
def genKey(key1,key2):
	if key1 and key: 
		n = key1 * key2
		fi = (primo1 - 1 ) * (primo2 - 1 )
		base = primo1 * primo2 - primo1 - primo2 + 1 
		publica = publicKeyE(fi)
		privada = privateKeyD(publica , fi)
		return n , publica , privada
#ascii chars 
def genChars():
	#ascii chars 32-127 bits
	chars = []
	for i in range(32,127):
		chars.append(chr(i))
	return chars
def encrypt(msg,e,n):
	cifrate = []
	chars = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
	for i in msg:	
		value = chars.index(i)
		enchar = (value**e)%n
		cifrate.append(enchar)
	return cifrate
def decrypt(cifrate,d,n):
	msg = []
	chars = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
	print(cifrate)
	for value in cifrate:	
		print(value)
		dechar = (int(value)**d)%n
		msg.append(chars[dechar])
	return msg

def main():
	primo1 = 103
	primo2 = 89
	n = primo1 * primo2
	fi = (primo1 - 1 ) * (primo2 - 1 )
	e = publicKeyE(fi)
	d = privateKeyD(e,fi)
	print("e",e,"d",d,"n",n)
	print(genChars())
	msg = input("mensaje: \n")
	encmsg = [2274, 6177, 6512, 5101, 0, 1323, 0, 5686, 3644, 0, 6512, 6512, 3644, 7912, 6177, 0, 3644, 6512, 0, 7399, 3644, 217, 8244, 5101, 5936, 3644, 0, 5936, 3644, 5936, 3644, 610]
#encrypt(msg,e,n)
	decmsg = decrypt(encmsg,7181,9167)#d 7181 n 9167

	#errordecmsg = decrypt(msg,d,n)
	print(msg,decmsg,encmsg)#,errordecmsg)
main()

#[' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
