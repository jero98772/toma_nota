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
		print(i,fi)
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
	tmp = []
	chars = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
	#print(cifrate)
	for value in cifrate:	
		#print(value)
		dechar = (int(value)**d)%n
		print(dechar)
		msg.append(chars[dechar])
		tmp.append(dechar)
	return msg
	print("tmp",tmp)

def main():
	primo1 = 17
	primo2 = 41
	n = primo1 * primo2
	fi = (primo1 - 1 ) * (primo2 - 1 )
	e = publicKeyE(fi)
	d = privateKeyD(e,fi)
	print("e",e,"d",d,"n",n)
	print(genChars())
	msg = "hola vas por buen camino el premio es una cuenta de netflix que vence en 2 meses y el usuario es un correo y el correo es criptoreto arroba jero98772 punto website y la clave es lasclaveshayvecesquenoseentienden"
	#encmsg =[353, 260, 563, 7, 0, 392, 7, 247, 0, 402, 260, 41, 0, 332, 68, 222, 592, 0, 356, 7, 695, 91, 592, 260, 0, 222, 563, 0, 402, 41, 222, 695, 91, 260, 0, 222, 247, 0, 68, 592, 7, 0, 356, 68, 222, 592, 254, 7, 0, 85, 222, 0, 592, 222, 254, 76, 563, 91, 503, 0, 327, 68, 222, 0, 392, 222, 592, 356, 222, 0, 222, 592, 0, 256, 0, 695, 222, 247, 222, 247, 0, 302, 0, 222, 563, 0, 68, 247, 68, 7, 41, 91, 260, 0, 222, 247, 0, 68, 592, 0, 356, 260, 41, 41, 222, 260, 0, 302, 0, 222, 563, 0, 356, 260, 41, 41, 222, 260, 0, 222, 247, 0, 356, 41, 91, 402, 254, 260, 41, 222, 254, 260, 0, 7, 41, 41, 260, 332, 7, 0, 267, 222, 41, 260, 291, 581, 318, 318, 256, 0, 402, 68, 592, 254, 260, 0, 535, 222, 332, 247, 91, 254, 222, 0, 302, 0, 563, 7, 0, 356, 563, 7, 392, 222, 0, 222, 247, 0, 563, 7, 247, 0, 356, 563, 7, 392, 222, 247, 0, 353, 7, 302, 0, 392, 222, 356, 222, 247, 0, 327, 68, 222, 0, 592, 260, 0, 247, 222, 0, 222, 592, 254, 91, 222, 592, 85, 222, 592]
	encmsg = encrypt(msg,e,n)
	decmsg = decrypt(encmsg,d,n)
	#print(d,n)
	#errordecmsg = decrypt(msg,d,n)
	print(msg,decmsg,encmsg)#,errordecmsg)
	print(decmsg)
def main2():
	valor = 17
	primo1 = 103
	primo2 = 29
	n = primo1 * primo2
	fi = (primo1 - 1 ) * (primo2 - 1 )
	e = publicKeyE(fi)#al reves D publica y E privada
	d = privateKeyD(e,fi)
	encmsg = (valor**e)%n
	decmsg = (encmsg**d)%n
	print(e,d,encmsg,decmsg)
main()
#main2()
#[' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
